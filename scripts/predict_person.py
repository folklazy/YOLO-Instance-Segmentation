"""Explicit one-image inference; requires local weights and a fresh output file."""
import argparse
from pathlib import Path
import sys
import numpy as np
from PIL import Image

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from yolo_instance_segmentation import PersonSegmenter


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--image',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--device',default='cuda:0')
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Choose a fresh output path')
    with Image.open(args.image) as image:
        rgb=np.asarray(image.convert('RGB'))
    detector=PersonSegmenter(args.checkpoint,device=args.device)
    result=detector.predict_rgb(rgb)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('xb') as stream:
        np.savez_compressed(stream,**result)
    print(f'people={len(result["scores"])} output={args.output}')


if __name__=='__main__':
    main()
