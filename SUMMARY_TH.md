# สรุปสำหรับส่งมอบ — YOLO Person Instance Segmentation

งานเปรียบเทียบ pretrained YOLO26, YOLO11, YOLOv9 และ YOLOv8 รวม 17 checkpoints แบ่งห้ากลุ่มขนาดบน Tesla T4 โดยใช้ FP32, batch1 และ input640 ภายในแต่ละ dataset ตรึง population และเงื่อนไขเดียวกัน

MOTS20 ใช้ 2,862 เฟรมและ 26,894 GT person instances รายเฟรม มี person masks จึงใช้ Mask AP ส่วน CCTV600 ใช้ 600 ภาพ มี eligible visible person boxes 769 คน จึงใช้ Box AP การรายงานแยก metric และ dataset ชัดเจน

| จุดตัดสิน | ผลจาก canonical statistics |
|---|---|
| ความสอดคล้อง mask บน MOTS20 | YOLO26x mAP 60.373%, Recall 84.629% |
| ค่าใช้จ่ายของ YOLO26x บน MOTS20 | forward 72.458 ms/ภาพ, pipeline 109.639 ms/ภาพ |
| Box AP บน CCTV600 | YOLOv9e 67.808%, YOLO26x 67.201% |
| Coverage บน CCTV600 | YOLO26x TP 624, FP 113, FN 145; YOLOv9e TP 612, FP 53, FN 157 |
| ตัวเลือกที่ผู้ใช้ freeze และระบบเว็บใช้อยู่ | YOLO26x-Seg; exact checkpoint hash ตรวจใหม่ตรง manifest |

เหตุผลคง YOLO26x คือ selection ที่ยึด Mask AP ของงานเดิมและความต้องการเก็บบุคคลให้ downstream ส่วนผล CCTV600 เพิ่มหลักฐานเรื่อง Recall พร้อมเผย trade-off ของ false positives และต้นทุนประมวลผล การเลือกนี้ยังต้องพิจารณาเงื่อนไข deployment ของผู้รับงาน

ชุดส่งมอบประกอบด้วย portable detector extraction, evaluators/loaders, reference source พร้อม tests, aggregate results และ provenance วิธีอ่านและผลทั้งหมดอยู่ใน [รายงานวิจัย](docs/RESEARCH_REPORT_TH.md) การทดสอบ GPU เดิมกับการตรวจแพ็กเกจใหม่แยกสถานะใน [quality gates](docs/QUALITY_GATES.md)
