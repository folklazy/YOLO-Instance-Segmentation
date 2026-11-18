# Acceptance checklist — YOLO Instance Segmentation

## Content selection
- [ ] Confirm actual source workspace/repo inventories, branches and commits.
- [ ] Classify each candidate artifact: shipping / evidence / exploratory / obsolete / sensitive.
- [ ] Include only reviewed code, tests, configs, results and documentation.
- [ ] Link to original full experiment reports instead of copying large logs/caches.

## Domain gates
- [ ] ผลรวมทุกตารางตรงกับ canonical source และมี commit SHA/report path
- [ ] Protocol เทียบ fair จริง; แยก inference timing จาก pipeline timing
- [ ] ภาพ/GT mask alignment ตรวจสอบได้; rights ของ CCTV เหมาะสม
- [ ] ข้อมูลที่ยังขาดแสดง NOT_VERIFIED ไม่ใส่ตัวเลขประมาณ

## Engineering/provenance
- [ ] Ensure README is accurate and all internal/external links work.
- [ ] Record source SHA / release version / environment / license/rights where relevant.
- [ ] Verify all imported code has tests or an evidenced smoke run.
- [ ] No secrets, unauthorized CCTV imagery, unverifiable numbers or silently edited canonical metrics.
- [ ] Preserve originals and record a migration summary with before/after checks.
- [ ] Update status in Project Hub only after evidence exists.
- [ ] Delete temporary `tasks/ACTIVE_TASK.md` **only after** acceptance and durable handoff summary.
