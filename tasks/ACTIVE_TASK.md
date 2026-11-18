# ACTIVE TASK — Initial curated handoff for YOLO Instance Segmentation

**Status:** OPEN (temporary task brief; do not delete until validation + acceptance).

## Objective
Build the clean delivery package for YOLO Instance Segmentation from the owner's completed but mixed historical VS Code/SSH workspaces and GitHub evidence. This repo was newly created and is **not** proof that the original work has migrated.

## Sources to inspect
- [MOTS20 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)
- [CCTV600 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study)
- [Largest MOTS20](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark)
- [MOTS20 2nd largest](https://github.com/folklazy/YOLO_Second_Largest_Seg_MOTS20_Benchmark)
- [MOTS20 Medium](https://github.com/folklazy/YOLO_Medium_Seg_MOTS20_Benchmark)
- [MOTS20 Small](https://github.com/folklazy/YOLO_Small_Seg_MOTS20_Benchmark)
- [MOTS20 Nano](https://github.com/folklazy/YOLO_Nano_Seg_MOTS20_Benchmark)

The owner may also have local-only files on the SSH machine. Find paths only by read-only inspection; do not assume or invent them.

## Work sequence
1. ทำ inventory โครงสร้าง MOTS20/CCTV600 study และ tier repos พร้อม sha/branches
2. แยก papers, authoritative reports, numeric files, visual evidence, scripts และ artifact ทดลอง
3. เสนอ curated layout และสำเนาเฉพาะไฟล์ที่ตรวจรับรองใน Repo นี้
4. จัด summary TH แบบ short + technical + qualitative พร้อมลิงก์หลักฐานที่ตรวจสอบได้

## Mandatory restrictions
- ไม่ retrain/rerun benchmark โดยอัตโนมัติ
- ไม่คัดลอก prediction cache ขนาดใหญ่หรือ checkpoint ออกจากแหล่งเดิมโดยไม่ตรวจ license/ขนาด
- ไม่แก้ canonical CSV หรือ metric จากการทดลองเดิม
- This task does not authorize deleting experiment directories, modifying original benchmark values, uploading restricted company CCTV, changing visibility, full retraining or large downloads.
- If a choice changes the selected model, interface, source-of-truth or rights exposure, stop and get owner approval.

## Final evidence to leave behind
- `docs/SOURCE_INVENTORY.md` completed with exact paths/commits/hashes
- Updated curated README/scope/quality checklist
- Relevant source files/tests/evidence index with verified links
- Short handoff summary: changed files, verifications, limitations, unresolved tasks
- Update Hub if separately authorized

## Cleanup after verified completion
After owner acceptance, preserve findings in permanent documents and delete **this task file only**. Do not delete `AGENTS.md`, results, provenance or audit files.
