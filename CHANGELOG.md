# Changelog

## 0.1.0 — 19 พฤศจิกายน 2026

ตรวจ inventory ก่อนคัดไฟล์จาก 12 research repositories และ pilot เดิม คัด aggregate tables/plots พร้อม SHA256 และคง source archives ไว้ตามเดิม เพิ่ม detector extraction ที่ผูก YOLO26x กับ app source, reusable MOTS evaluator/loader และ CCTV reference dependencies พร้อม CPU tests

เพิ่มสรุปผู้บริหาร รายงานวิจัย/insights วิเคราะห์ภาพจริง วิธีทำซ้ำ และ integration contract คงความต่าง Mask AP ของ MOTS20 กับ Box AP ของ CCTV600 และข้อจำกัดของ runtime/timing scopes ไว้ในเอกสาร

ตรวจ CPU 38 กรณี: ผ่าน37 ข้าม1 พร้อมเหตุผล ตรวจ source12repos/1,205file hashes, ตาราง34แถว, packaging wheel/import และ curated hashes ผ่าน ไม่มี model inference หรือ benchmark ใหม่ การเทียบ GPU output ของ extracted runtime ยังเป็น NOT_RUN

รอ owner acceptance ก่อนลบ tasks/ACTIVE_TASK.md หลักฐานส่งมอบและ source revisions อยู่ใน provenance และ docs/QUALITY_GATES.md
