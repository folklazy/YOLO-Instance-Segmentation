# ขอบเขตและสิ่งส่งมอบ

ชุดส่งมอบนี้ดูแลเฉพาะ YOLO Person Instance Segmentation ในเจ็ด-repository architecture ของ Project Hub ประกอบด้วย reusable selected detector, frozen research evaluators/reference source, canonical aggregate results, model manifest และเอกสารวิจัย/วิธีทำซ้ำ

Runtime interface 0.1.0 แยกส่วน detector จาก host ของเว็บเดิม โดยตรวจค่าพารามิเตอร์ geometry และ checkpoint bindings งาน benchmark ของ MOTS20/CCTV600 เก็บ source commits และ file hashes ของแต่ละ tier ชัดเจน

ภาพ/annotation CCTV, model weights และ bulk predictions/logs ใช้ artifact locations ภายนอก ข้อมูลที่มีสิทธิ์เผยแพร่ใน repo นี้เป็น metadata, code, reports และ aggregate plots ส่วน Hub, Final, Parsing, Color และ Platform คงเป็นขอบเขตของงานแยกตามคำสั่งผู้ใช้

ผู้รับงานตรวจจาก README → SUMMARY → RESEARCH_REPORT → EVIDENCE_INDEX → REPRODUCIBILITY แล้วดูผล tests และข้อจำกัดใน QUALITY_GATES ต้องให้ owner ตรวจรับก่อนปิด tasks/ACTIVE_TASK.md
