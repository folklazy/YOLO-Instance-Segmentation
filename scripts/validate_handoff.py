"""Read-only checks for curated hashes, aggregate arithmetic and local links."""
from pathlib import Path
from collections import Counter
from decimal import Decimal
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))


def validate(source_workspace=None):
    sources=json.loads((ROOT/'provenance/SELECTED_FILES.json').read_text())
    for record in sources:
        if sha(ROOT/record['destination']) != record['destination_sha256']:
            raise ValueError('Curated file hash differs: '+record['destination'])
        if source_workspace and sha(source_workspace/record['original_path']) != record['source_sha256']:
            raise ValueError('Original file hash differs: '+record['original_path'])
    m=read_csv(ROOT/'results/mots20/MASTER_17_MODELS.csv')
    c=read_csv(ROOT/'results/cctv600/MASTER_17_MODELS.csv')
    if len(m)!=17 or len(c)!=17 or {r['checkpoint'] for r in m}!={r['model'] for r in c}:
        raise ValueError('Model roster differs')
    if Counter(r['family'] for r in m)!={'YOLO26':5,'YOLO11':5,'YOLOv8':5,'YOLOv9':2}:
        raise ValueError('Unexpected family support')
    for dataset,rows in [('mots20',m),('cctv600',c)]:
        for row in rows:
            tp,fp,fn=(int(row[k]) for k in ['tp','fp','fn'])
            denominators={'precision':tp+fp,'recall':tp+fn,'f1':2*tp+fp+fn}
            numerators={'precision':tp,'recall':tp,'f1':2*tp}
            for name in denominators:
                expected=Decimal(numerators[name])/Decimal(denominators[name])
                if abs(expected-Decimal(row[name])) > Decimal('1e-12'):
                    raise ValueError('Count/ratio mismatch')
            latency=row['pipeline_ms_mean' if dataset=='mots20' else 'adapter_mean_ms']
            if abs(Decimal(row['fps'])-Decimal(1000)/Decimal(latency)) > Decimal('1e-10'):
                raise ValueError('FPS/latency mismatch')
            if dataset=='mots20':
                if row['frames']!='2862' or row['gt_instances']!='26894' or tp+fn!=26894:
                    raise ValueError('MOTS GT population differs')
            elif row['images']!='600' or row['gt_people']!='769' or tp+fn!=769 or row['clean_rounds']!='3':
                raise ValueError('CCTV GT/timing completeness differs')
    checkpoints=json.loads((ROOT/'models/MANIFEST.json').read_text())['checkpoints']
    if {r['model_id'] for r in checkpoints}!={r['checkpoint'] for r in m}:
        raise ValueError('Checkpoint manifest differs from roster')
    selected=[r for r in checkpoints if r['selected']]
    binding=json.loads((ROOT/'configs/selected_yolo26x.json').read_text())
    if len(selected)!=1 or selected[0]['sha256']!=binding['checkpoint_sha256']:
        raise ValueError('Selected checkpoint binding differs')
    model_rows={r['checkpoint']:r for r in m}
    if max(m,key=lambda r:Decimal(r['mask_map50_95']))['checkpoint']!='yolo26x-seg.pt':
        raise ValueError('MOTS winner differs')
    if max(c,key=lambda r:Decimal(r['box_ap50_95']))['model']!='yolov9e-seg.pt':
        raise ValueError('CCTV winner differs')
    for row in c:
        if row['parameters']!=model_rows[row['model']]['parameters']:
            raise ValueError('Checkpoint parameter count mismatch')
    # The two studies publish different frontier encodings. Recompute membership
    # from unrounded canonical values, and compare to the recorded representation.
    for dataset,rows,accuracy,latency,model_key in [
            ('mots20',m,'mask_map50_95','inference_ms_mean','model'),
            ('cctv600',c,'box_ap50_95','inference_mean_ms','model')]:
        expected=set()
        for row in rows:
            dominated=any(Decimal(other[accuracy])>=Decimal(row[accuracy]) and
                          Decimal(other[latency])<=Decimal(row[latency]) and
                          (Decimal(other[accuracy])>Decimal(row[accuracy]) or
                           Decimal(other[latency])<Decimal(row[latency])) for other in rows)
            if not dominated:
                expected.add(row[model_key])
        frontier=read_csv(ROOT/f'results/{dataset}/PARETO_FRONTIER.csv')
        recorded={r['model'] for r in frontier if r.get('nondominated','True')=='True'}
        if expected!=recorded:
            raise ValueError('Recorded frontier differs: '+dataset)
    checked_links=0
    for document in ROOT.rglob('*.md'):
        if '.git' in document.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)',document.read_text()):
            if target.startswith(('http://','https://','#','mailto:')):
                continue
            path=target.split('#')[0]
            if not (document.parent/path).exists():
                # Byte-frozen reference protocol retains original workspace links.
                if 'reference' in document.parts:
                    continue
                raise ValueError('Missing local Markdown target: '+str(document)+': '+target)
            checked_links+=1
    return dict(status='PASS',selected_copy_hashes=len(sources),model_rows=34,
                P_R_F1_formula_checks=102,FPS_formula_checks=34,
                decimal_frontiers_checked=2,local_links_checked=checked_links,
                model_inference_calls=0,original_sources_checked=source_workspace is not None)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-workspace',type=Path)
    args=parser.parse_args()
    print(json.dumps(validate(args.source_workspace),indent=2))
