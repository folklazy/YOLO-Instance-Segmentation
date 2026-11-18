# YOLO Instance Segmentation

> **Curated delivery repository — content migration pending verification.** The project owner reports that implementation/research work was completed in older VS Code/SSH workspaces and source repos, but this new repository does not yet claim a fully packaged release.

ชุดส่งมอบด้านการศึกษาและเปรียบเทียบ YOLO Person Instance Segmentation จากงาน benchmark ที่ทำเสร็จแล้ว โดยเก็บผลจริงที่ตรวจสอบได้และเหตุผลการเลือก YOLO26x-Seg

**PUBLIC — metadata and approved code/docs only.** Never publish restricted company footage or secrets.

## เป้าหมายการส่งมอบ

- เปรียบเทียบ YOLO26, YOLO11, YOLOv9, YOLOv8 และขนาดที่ใช้ทดลองจริง (user-reported 17 variants; verify roster).
- บันทึก MOTS20/CCTV Protocol: dataset split, GT, ignore handling, masking, preprocessing, NMS, AP conf floor, maxDet, timing methodology.
- แยก AP50/AP75/mAP50–95, Precision/Recall/F1, TP-only mask IoU/Dice, latency/FPS, GPU memory, model parameters.
- ทำตาราง Pareto/near-tie/per-sequence ที่คำนวณจาก saved canonical results โดยไม่เปลี่ยนค่าดั้งเดิม.
- แสดงภาพ success/failure ที่เผยแพร่ได้และอธิบายเชิงคุณภาพโดยไม่อ้าง architecture superiority เกิน evidence.
- ส่งมอบ checkpoint manifest + inference adapter + contract เฉพาะที่ตรวจว่าถูกใช้งานจริง พร้อมเหตุผลเลือก YOLO26x-Seg.

## Existing sources (read-only starting points)

- [MOTS20 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)
- [CCTV600 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study)
- [Largest MOTS20](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark)
- [MOTS20 2nd largest](https://github.com/folklazy/YOLO_Second_Largest_Seg_MOTS20_Benchmark)
- [MOTS20 Medium](https://github.com/folklazy/YOLO_Medium_Seg_MOTS20_Benchmark)
- [MOTS20 Small](https://github.com/folklazy/YOLO_Small_Seg_MOTS20_Benchmark)
- [MOTS20 Nano](https://github.com/folklazy/YOLO_Nano_Seg_MOTS20_Benchmark)

**Important:** these references are candidates, not proof that all content is current, supported or safe to move. Agent must verify files and commits before copying.

## เอกสารสำคัญ

- [AGENTS.md](AGENTS.md) — read first; permanent agent rules
- [Scope & deliverables](docs/SCOPE_AND_DELIVERABLES.md) — exact responsibilities and exclusions
- [Source inventory](docs/SOURCE_INVENTORY.md) — existing source pointers and audit template
- [Quality gates](docs/QUALITY_GATES.md) — acceptance checklist
- [Active task](tasks/ACTIVE_TASK.md) — first-pass work brief; delete **only after** verified completion and durable handoff
- [Project Hub](https://github.com/folklazy/Human-Body-Extraction)
- [Final End-to-End Repository](https://github.com/folklazy/A-Comparative-Study-of-YOLO-Based-Instance-Segmentation)

## Release status

| Stage | Status |
|---|---|
| Historical experiments / implementation | Reported complete by project owner; specific commits to be audited |
| Clean delivery repository | Initialized |
| Source migration and code/package verification | **Pending** |
| Actual tests and release evidence in this repository | **Not verified yet** |

Only claim numbers and performance backed by linked canonical files. Do not make up final file counts, model parameters or deployment commands.
