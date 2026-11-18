# สิทธิ์ของโค้ด dependencies และข้อมูล

Ultralytics ที่ใช้อยู่มี LICENSE แบบ GNU Affero General Public License version3 ใน installed distribution และมีทางเลือกเงื่อนไขจากผู้พัฒนา upstream ผู้รับงานต้องตรวจข้อผูกพันของ dependency/code/weights ตามรูปแบบใช้งานก่อนเผยแพร่ระบบต่อ

Checkpoint URLs ใน models/MANIFEST.json เป็น URLs ที่บันทึกจริงใน source checkpoint manifests การมี URL และ hash ไม่ได้ให้สิทธิ์เผยแพร่ weights เพิ่มใน repo นี้ การใช้ dataset และภาพ MOTS20 ต้องอ้างเงื่อนไขของผู้จัดทำ ส่วนภาพ CCTV และ annotation ของบริษัทใช้ช่องทาง private ที่เจ้าของอนุญาต

โค้ดโครงงานที่คัดมามี provenance ชี้ต้นทางของผู้ใช้ การจัดส่งมอบนี้ไม่ได้กำหนดใบอนุญาตใหม่แทนเจ้าของ และไม่มีการคัด source ของไลบรารี Ultralytics เข้า repo นี้ ระบบใช้ dependency ที่ติดตั้งแยกไว้ การพิจารณา license สำหรับ distribution/deployment เป็นงานของเจ้าของ release
