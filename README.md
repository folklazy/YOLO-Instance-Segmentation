# YOLO Instance Segmentation

ชุดส่งมอบโค้ด YOLO person instance segmentation ผลเปรียบเทียบ pretrained checkpoints และเหตุผลการใช้ **YOLO26x-Seg** ในโครงงาน Human Body Extraction

ตรวจจัดส่งมอบ 19 พฤศจิกายน 2026 โดยตรวจ workspace จริงและ GitHub ต้นทาง 12 repositories มี **17 checkpoints ต่อ dataset** จาก YOLO26/YOLO11/YOLOv8 ตระกูลละ 5 ขนาด และ YOLOv9 e/c อีก 2 ขนาด ผลเดิมและ source archives ตรวจย้อนกลับได้จาก [inventory](docs/SOURCE_INVENTORY.md)

| ผลที่ตรวจจาก canonical tables | Dataset / Metric | ค่า |
|---|---|---:|
| YOLO26x-Seg ซึ่งผู้ใช้เลือกไว้ | MOTS20 Mask mAP50–95 | 60.373% |
| YOLO26x-Seg | CCTV600 Box AP50–95 | 67.201% |
| YOLOv9e-Seg ได้ Box AP สูงสุดใน CCTV600 | CCTV600 Box AP50–95 | 67.808% |
| YOLO26x-Seg ได้ Recall สูงสุดใน CCTV600 | bbox IoU0.50 / confidence0.25 | 81.144% |

YOLO26x เป็น frozen selection เดิม มี Mask AP สูงสุดใน MOTS20 และใช้ checkpoint SHA256 เดียวกับ detector ของเว็บที่ตรวจบนเครื่อง ส่วน CCTV600 แสดงข้อแลกเปลี่ยนกับ YOLOv9e ซึ่งมี Box AP/F1 สูงกว่า อ่านเหตุผลการเลือกและข้อจำกัดใน [รายงานวิจัย](docs/RESEARCH_REPORT_TH.md)

## อ่านตามหน้าที่

- [สรุปผู้บริหาร](SUMMARY_TH.md) สำหรับการส่งมอบและพรีเซนต์
- [รายงานวิจัยและข้อค้นพบ](docs/RESEARCH_REPORT_TH.md) ครอบคลุม protocol, metrics, ผล 17 ตัว, scaling, Pareto และข้อจำกัด
- [วิเคราะห์ภาพจริงที่มีหลักฐานเดิม](docs/QUALITATIVE_ANALYSIS_TH.md) ครอบคลุม success, failure, การบดบัง ขนาด แสง และมุมกล้อง
- [วิธีติดตั้งและทำซ้ำ](docs/REPRODUCIBILITY_TH.md) พร้อมขอบเขตของ CPU tests และหลักฐาน GPU เดิม
- [Integration contract](docs/INTEGRATION_CONTRACT.md) สำหรับการใช้ detector กับโปรเจกต์ปลายทาง
- [Evidence index](docs/EVIDENCE_INDEX.md), [file inventory](provenance/FILE_INVENTORY.csv), [source/copy hashes](provenance/SELECTED_FILES.json)
- [ผลตรวจส่งมอบ](docs/QUALITY_GATES.md) และ [CHANGELOG](CHANGELOG.md)

## โค้ดที่ใช้ต่อได้

```python
from yolo_instance_segmentation import PersonSegmenter

model = PersonSegmenter('/path/to/yolo26x-seg.pt', device='cuda:0')
# rgb เป็น numpy.uint8 รูป H×W×3 ตาม RGB
result = model.predict_rgb(rgb)
# masks N×H×W, boxes N×4, scores N, class_ids N, original_wh [W,H]
```

จัดเตรียม local weights ตาม [manifest](models/MANIFEST.json) และ environment ตามคู่มือก่อนเรียกโมเดล package ตรวจ checkpoint hash ก่อนโหลด ตัวอย่าง CLI รับไฟล์ใหม่และบันทึก NPZ ที่ path ใหม่

```bash
python scripts/predict_person.py --checkpoint /path/to/yolo26x-seg.pt \
  --image /path/to/new-image.jpg --output /path/to/private/persons.npz --device cuda:0
```

ตัวอย่างนี้เป็นคำสั่งใช้งานสำหรับผู้รับงาน การจัดส่งมอบรอบนี้ตรวจ imports/CPU contracts/evaluators โดยอาศัยหลักฐาน inference ของต้นทางสำหรับผลวิจัย รายละเอียดสถานะอยู่ใน quality gates

## โครงสร้าง

```text
src/yolo_instance_segmentation/   detector ที่แยกจากส่วน YOLO ของเว็บ + MOTS20 mask evaluator/loader
reference/cctv600/                source/scorer/packet/loader/tests ของ benchmark ที่เก็บครบ dependency
configs/                         ค่า detector ที่เว็บใช้จริงและ source binding
models/                          checkpoint manifest
results/mots20/                  aggregate CSV และกราฟ
results/cctv600/                 aggregate CSV และกราฟ
scripts/                         CLI และตัวตรวจส่งมอบ
tests/                          CPU acceptance และ metric regressions
docs/                           ขอบเขต รายงาน วิธีทำซ้ำ และดัชนีหลักฐาน
provenance/                      inventory, source heads, file hashes และ validation
```

โค้ดใน reference ใช้ layout และ scientific bindings ของงานต้นฉบับ การทำ benchmark เต็มให้อ้าง source commit และคำสั่งในคู่มือ ส่วน package หลักมี interface แยกเพื่อใช้ detector ต่อได้

## สิทธิ์และ artifact ภายนอก

[Third-party notices](THIRD_PARTY_NOTICES.md) ระบุ Ultralytics AGPL-3.0 และประเด็นการรับ weights/data ภาพ CCTV, annotation รายภาพ, dense predictions, credentials และ checkpoints เก็บภายนอก Git ชุดนี้ กราฟที่นำมาเก็บเป็น aggregate plots ภาพ MOTS20 ประกอบอ้างไปยังหลักฐานที่เผยแพร่อยู่แล้ว

[Project Hub](https://github.com/folklazy/Human-Body-Extraction) · [Final integrated project](https://github.com/folklazy/A-Comparative-Study-of-YOLO-Based-Instance-Segmentation)

สถานะงานชั่วคราวอยู่ใน [ACTIVE_TASK](tasks/ACTIVE_TASK.md) และรอ owner acceptance ก่อนปิดไฟล์นั้น
