# ผลตรวจส่งมอบ YOLO Instance Segmentation

ตรวจ 19 พฤศจิกายน 2026 สถานะ **PASS_WITH_DISCLOSED_LIMITATIONS / รอ owner acceptance** ผลตรวจนี้รับรองการคัดจัดส่งมอบและ CPU contracts ตามขอบเขตด้านล่าง หลักฐานตัวเลขและ log hashes อยู่ใน [VALIDATION.json](../provenance/VALIDATION.json)

| ประเด็น | ผลตรวจจริง | ขอบเขตการรับรอง |
|---|---|---|
| Inventory / Git | 12 source repos; HEAD, branch refs, remote main และ tracked/untracked status ตรวจแล้ว | ไฟล์ local-only ระบุแยกใน provenance ไม่ถือว่าอยู่บน GitHub แล้ว |
| Original integrity | HEAD/status 12 repos และ source hashes 1,205 ไฟล์ไม่เปลี่ยน | ไม่ลบ ย้าย หรือแก้ originals; ไม่ bulk rehash dense predictions |
| Copy integrity | Source/destination hashes ของไฟล์ที่เลือก 55 รายการตรง manifest | Transformation ระบุชัด รวม extraction และ relative import |
| Results | 34 model rows ตรงกับ tier sources; P/R/F1 102 สูตร, FPS34 สูตร และ Pareto2 ชุดผ่าน | คำนวณตรวจจากค่าเต็ม ไม่เปลี่ยน canonical CSV |
| Roster / weights | 17 checkpoints ต่อ dataset; selected YOLO26x hash ตรวจจากไฟล์จริง | อีก16ตรวจความตรงกันของ historical manifests ไม่อ้างว่า rehash weights ใหม่ |
| Runtime / MOTS tests | 24 cases: ผ่าน23 ข้าม1 | CPU fixtures, evaluator และหนึ่ง external known-GT regression; test ที่ข้ามเป็น historical runner-summary นอก package |
| CCTV reference tests | 14 cases ผ่านทั้งหมด | Synthetic actual packet→scorer→reporter, matching/ignore/strict completeness; ไม่มี model inference |
| Imports / packaging | 11 modules, CLI help, wheel build และ import จาก wheel ผ่าน | ใช้ environment เดิม ไม่ติดตั้ง dependency หรือย้าย environment |
| Detector extraction | Checkpoint binding, process flags, RGB/BGR, kwargs, dimensions, empty/invalid outputs ตรวจผ่าน CPU contracts | GPU output parity ของ extracted package เป็น **NOT_RUN**; benchmark results เป็นผลเดิมจาก source runtime |
| Timing | แยก model forward, pipeline/adapter และ dedicated timing ตาม source | ไม่ใช้เวลาจัดส่งมอบแทนผล benchmark; รักษาข้อจำกัดระหว่าง datasets/sessions |
| Qualitative evidence | ตรวจภาพเดิม MOTS20 และ CCTV แบบ private พร้อมคำอธิบายที่จำกัดตามหลักฐาน | การตรวจตัวอย่างไม่ใช่การตรวจ alignment ทุกภาพซ้ำ |
| Publication | เก็บ aggregate plots เท่านั้น; ภาพ MOTS20 เชื่อมหลักฐานเดิม | ไม่เผยแพร่ภาพ/annotation/per-image records CCTV, weights, prediction caches หรือ secrets |
| Links / references | Internal links45 ตรวจอัตโนมัติ; source commit/file links36 ตรวจ Git objects ต้นทางและ remote refs | ไม่อ้างว่าเรียก HTTP ทุก third-party URL ใหม่; byte-frozen reference protocol คง relative links ของ layout ต้นฉบับ |

รวม tests ที่ไม่ซ้ำ **38 กรณี: ผ่าน37 ข้าม1 ล้มเหลว0** เป็นการตรวจด้านซอฟต์แวร์และส่งมอบ ไม่ใช่ผล GPU benchmark รอบใหม่ ตรวจเครื่องปัจจุบันพบ Tesla T4 15,360MiB และ CUDA ใช้งานได้ แต่รอบนี้ไม่มี model-frame calls

## สิ่งที่ผู้รับงานต้องทราบ

- [Integration contract](INTEGRATION_CONTRACT.md) แยก app operating settings จาก frozen research settings ชัดเจน ไม่รับรองว่า route ทั้งสองให้ output เหมือนกัน
- การทำ benchmark เต็มซ้ำต้องมี datasets/weights และ source-workspace layout ตาม [Reproducibility](REPRODUCIBILITY_TH.md) ข้อมูล private ไม่รวมใน public clone
- ผลวิจัยเดิมและข้อจำกัด PASS_WITH_WARNINGS ของต้นทางยังคงอยู่ การตรวจส่งมอบไม่เปลี่ยนสถานะทางวิทยาศาสตร์ย้อนหลัง
- การรับสิทธิ์ weights/data และ Ultralytics อ้างตาม [Third-party notices](../THIRD_PARTY_NOTICES.md) การไม่รวม CCTV images เป็นวิธีรักษาขอบเขตสิทธิ์ของชุดเผยแพร่
- Hub และ Final repository ไม่ถูกแก้ในรอบนี้ ตามขอบเขตผู้ใช้และ AGENTS.md
- เก็บ [ACTIVE_TASK](../tasks/ACTIVE_TASK.md) ไว้จน owner ตรวจรับ แล้วจึงลบเฉพาะ task file ตาม workflow
