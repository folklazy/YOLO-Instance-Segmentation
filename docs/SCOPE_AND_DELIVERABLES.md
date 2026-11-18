# Scope & deliverables — YOLO Instance Segmentation

## Purpose
ชุดส่งมอบด้านการศึกษาและเปรียบเทียบ YOLO Person Instance Segmentation จากงาน benchmark ที่ทำเสร็จแล้ว โดยเก็บผลจริงที่ตรวจสอบได้และเหตุผลการเลือก YOLO26x-Seg

## Deliverables
- เปรียบเทียบ YOLO26, YOLO11, YOLOv9, YOLOv8 และขนาดที่ใช้ทดลองจริง (user-reported 17 variants; verify roster).
- บันทึก MOTS20/CCTV Protocol: dataset split, GT, ignore handling, masking, preprocessing, NMS, AP conf floor, maxDet, timing methodology.
- แยก AP50/AP75/mAP50–95, Precision/Recall/F1, TP-only mask IoU/Dice, latency/FPS, GPU memory, model parameters.
- ทำตาราง Pareto/near-tie/per-sequence ที่คำนวณจาก saved canonical results โดยไม่เปลี่ยนค่าดั้งเดิม.
- แสดงภาพ success/failure ที่เผยแพร่ได้และอธิบายเชิงคุณภาพโดยไม่อ้าง architecture superiority เกิน evidence.
- ส่งมอบ checkpoint manifest + inference adapter + contract เฉพาะที่ตรวจว่าถูกใช้งานจริง พร้อมเหตุผลเลือก YOLO26x-Seg.

## Out of scope / risks
- ไม่ retrain/rerun benchmark โดยอัตโนมัติ
- ไม่คัดลอก prediction cache ขนาดใหญ่หรือ checkpoint ออกจากแหล่งเดิมโดยไม่ตรวจ license/ขนาด
- ไม่แก้ canonical CSV หรือ metric จากการทดลองเดิม

## Definition of done
- ผลรวมทุกตารางตรงกับ canonical source และมี commit SHA/report path
- Protocol เทียบ fair จริง; แยก inference timing จาก pipeline timing
- ภาพ/GT mask alignment ตรวจสอบได้; rights ของ CCTV เหมาะสม
- ข้อมูลที่ยังขาดแสดง NOT_VERIFIED ไม่ใส่ตัวเลขประมาณ

## Interface to the final project
Only export the minimal verified runtime module, configuration, schema, model/checkpoint manifest, test fixtures and documentation needed by [Final End-to-End Project](https://github.com/folklazy/A-Comparative-Study-of-YOLO-Based-Instance-Segmentation). Archive research outputs stay in their original repos unless there is a clear and approved reason to bundle them.

Before release, register exact source commits, package/API versions and rights in the [Project Hub](https://github.com/folklazy/Human-Body-Extraction).
