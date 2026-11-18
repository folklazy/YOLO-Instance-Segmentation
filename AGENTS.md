# AGENTS.md — YOLO Instance Segmentation

## Mission
ชุดส่งมอบด้านการศึกษาและเปรียบเทียบ YOLO Person Instance Segmentation จากงาน benchmark ที่ทำเสร็จแล้ว โดยเก็บผลจริงที่ตรวจสอบได้และเหตุผลการเลือก YOLO26x-Seg

## Read before any change
1. `README.md`
2. `docs/SCOPE_AND_DELIVERABLES.md`
3. `docs/SOURCE_INVENTORY.md`
4. `docs/QUALITY_GATES.md`
5. `tasks/ACTIVE_TASK.md` if present
6. Corresponding source repos' own `AGENTS.md` and exact workspace files.

## Scientific and source integrity
- Confirm source file paths, git status, commit hashes, actual selected implementation, checkpoint/version and report provenance before claiming anything is final.
- Treat old experiments as **read-only evidence**. Preserve canonical metrics, raw annotations, source hashes, logs and model artifacts; do not delete or silently regenerate them.
- Do not assume the newest-named folder is what the final app runs. Verify actual imports/config/checkpoints in the running project.
- Preserve prior git histories; use links/evidence manifests rather than bulk-duplicating research data.
- Separate confirmed facts, derived analysis, inference and TODO/NOT_VERIFIED.

## Scope and permissions
- ไม่ retrain/rerun benchmark โดยอัตโนมัติ
- ไม่คัดลอก prediction cache ขนาดใหญ่หรือ checkpoint ออกจากแหล่งเดิมโดยไม่ตรวจ license/ขนาด
- ไม่แก้ canonical CSV หรือ metric จากการทดลองเดิม
- Do not edit the Hub, Final repo or any other repository without a separate scoped task.
- Do not download large models/datasets, install packages, run full benchmarks/training, move/delete originals or change repository visibility without authorization.
- No API keys, passwords, tokens, DB credentials or company imagery in public commits. **PUBLIC — metadata and approved code/docs only.** Never publish restricted company footage or secrets.

## Required work product
- ทำ inventory โครงสร้าง MOTS20/CCTV600 study และ tier repos พร้อม sha/branches
- แยก papers, authoritative reports, numeric files, visual evidence, scripts และ artifact ทดลอง
- เสนอ curated layout และสำเนาเฉพาะไฟล์ที่ตรวจรับรองใน Repo นี้
- จัด summary TH แบบ short + technical + qualitative พร้อมลิงก์หลักฐานที่ตรวจสอบได้

## Done means
- ผลรวมทุกตารางตรงกับ canonical source และมี commit SHA/report path
- Protocol เทียบ fair จริง; แยก inference timing จาก pipeline timing
- ภาพ/GT mask alignment ตรวจสอบได้; rights ของ CCTV เหมาะสม
- ข้อมูลที่ยังขาดแสดง NOT_VERIFIED ไม่ใส่ตัวเลขประมาณ
- Preserve a durable summary of findings, source SHAs, changed paths, test results, known issues and a reproducibility note.
- Record relevant decisions/limitations in docs and the Project Hub if authorized.
- Remove **only** `tasks/ACTIVE_TASK.md` after owner acceptance and saved evidence; never remove permanent `AGENTS.md`, provenance or historical artifacts.
