# Detector integration contract 0.1.0

Source of truth คือส่วน detector ของแอป commit `8e4dfce9ca54d7bab40a1c56552c4c29f1c40176` และไฟล์ host SHA256 `9bd186aee6ed4f27710d9fbfb1ca57803c80010c39c6bf4518731b9456ac0edd` ค่า checkpoint และ arguments อยู่ใน [selected_yolo26x.json](../configs/selected_yolo26x.json)

## Interface

`PersonSegmenter(checkpoint, device='cuda:0', expected_sha256=SELECTED_CHECKPOINT_SHA256)` ตรวจไฟล์และ hash ก่อนสร้าง Ultralytics model ผู้เรียกเตรียม checkpoint โดยตรง ส่วน `predict_rgb(rgb, confidence=0.25)` รับ uint8 RGB H×W×3 และคืน dict

| Field | Shape / ความหมาย |
|---|---|
| masks | bool N×H×W บนภาพต้นฉบับ แต่ละ plane เป็นผลของบุคคลหนึ่ง detection |
| boxes | N×4 float, xyxy pixel coordinates บนภาพต้นฉบับ |
| scores | N ค่า detection confidence |
| class_ids | N int64 ทั้งหมดเป็น person0 |
| original_wh | [W,H] |

เมื่อไม่พบคน masks มี shape0×H×W, boxes0×4 และ scores0 ข้อมูลเรียงตาม native output เก็บ instance planes แยกกัน และใช้ index ภายในภาพเป็น identity สำหรับผูก crop/การแสดงผล ยังไม่มี identity ข้ามเฟรมใน contract นี้

## Settings ที่ตรวจตรงกับ app

Person0, imgsz640, confidence0.25โดย default, NMS IoU0.7, max_det200, retina_masks=True, half=False, augment=False, verbose=False, save=False และแปลง RGB→BGR ก่อนส่ง array เข้า Ultralytics `predict` ตัว app ไม่ override rect/NMS/end2end ดังนั้น package เก็บ native default ตาม version ที่ตรึงไว้

Process initialization ตั้ง torch threads2 และปิด CUDA matmul/cudnn TF32 ตาม initialize ของ app

Runtime export เป็น packaging extraction ใหม่ที่ตรวจจาก kwargs และ geometry contracts ด้วย CPU fixtures การยืนยัน hard-mask equivalence บน GPU ของ export นี้ยังเป็น NOT_RUN ในรอบจัดส่งมอบ ผล benchmark ใช้ source runtime ที่อ้างใน reference และ source archives ตาม scientific bindings เดิม

## Research interface

MOTS20 evaluator ใช้ `yolo_instance_segmentation.mots20.metrics` กับ loader `mots20.mots` โดยเปลี่ยนเป็น relative import เท่านั้น เมื่อต้อง reproduce frozen AP ให้ส่ง `max_dets=200` เข้า `ap_metrics` อย่างชัดเจนตาม config ของ benchmark CCTV reference มี package `cctv600` พร้อม scoring, packet, loader และ source dependencies เดิมใต้ `reference/cctv600/src` การใช้ CLI เต็มต้องคืน source workspace/tier/dataset layout ตามคู่มือ

Research config ใช้ floor0.001/cap1000, square640และ common NMS path เพื่อเทียบ checkpoints ส่วน app operating config อยู่ใน binding ด้านบน ผู้พัฒนาปลายทางควร pin package version, checkpoint hash และ configuration ไปพร้อมกัน
