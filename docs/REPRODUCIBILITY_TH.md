# การเตรียมเครื่องและทำซ้ำ

## Environment ที่มีหลักฐาน

source manifests บันทึก Python3.12.3, PyTorch2.14.0+cu130, torchvision0.29.0+cu130, CUDA runtime13.0, Ultralytics8.4.160, NumPy2.5.3, pycocotools2.0.11, OpenCV5.0.0.93 และ Tesla T4 Exact environment record อยู่ใน source repos และ [recorded-environment.txt](../requirements/recorded-environment.txt) รุ่น CUDA runtime แยกจากชื่อ GPU และ driver version

รอบจัดส่งมอบใช้ environment เดิมบน server ตรวจ imports และ `torch.cuda.is_available()` ได้จริง ไม่มีการเปลี่ยน packages ใช้ existing compatible Python ที่มี dependencies ก่อนรันคำสั่งต่อไปนี้ ผู้รับงานบนเครื่องใหม่จัดเตรียม PyTorch/CUDA build ที่เข้ากันได้กับฮาร์ดแวร์ก่อนติดตั้ง dependencies

## ใช้ source โดยตรง

```bash
export PYTHONPATH="$PWD/src:$PWD/reference/cctv600/src"
python -m unittest discover -s tests -v
python -m unittest discover -s reference/cctv600/tests -v
python scripts/validate_handoff.py
python scripts/predict_person.py --help
```

MOTS known-GT regression ใช้ dataset ภายนอก หากไม่มีจะรายงาน skipped อย่างชัดเจน กำหนด `YOLO_SOURCE_WORKSPACE=/path/to/source-workspace` เพื่อใช้ `datasets/MOTS/MOTS/train` ของเดิม มีอีกหนึ่ง historical-runner summary test ที่อ้าง source pilot และถูกระบุ skipped ใน curated suite เพราะอยู่นอก export contract

ติดตั้งเฉพาะ package ของ repo นี้ลง environment ที่เตรียมแล้วได้ด้วย `python -m pip install --no-deps --no-build-isolation -e .` เมื่อมี setuptools ที่เข้ากันได้ การติดตั้งไม่รวม external datasets/weights

## Runtime และ weights

`models/MANIFEST.json` มี source URLs ที่อ่านจาก manifests ต้นทาง 17 checkpoints พร้อม hashes โดย hash ของ selected yolo26x ตรวจใหม่กับไฟล์บนเครื่อง ส่วนอีก16อ้าง source manifests ที่เก็บไว้ Checkpoint selected SHA256 `92b3de0065766a17180d6219858717dc9d03cdce8a3ca9576c97fd75aabb64f3` ขนาด142,129,861bytes

รับไฟล์จากช่องทางที่เจ้าของอนุญาต ตรวจ hash ก่อนใช้ และเตรียมรูปที่คุณมีสิทธิ์เข้าถึง จากนั้นใช้ CLI ใน README ผล NPZ คง masks/boxes/scores/class_ids/original_wh การส่งมอบรอบนี้ไม่เรียกคำสั่ง inference ตัวอย่างนั้น

## ทำ benchmark เดิมซ้ำ

ใช้ source commits จาก [SOURCE_REPOSITORIES.json](../provenance/SOURCE_REPOSITORIES.json) วาง MOTS20/CCTV600 และ17weights ตาม manifests ต้นทาง คืน layout tier repositories ให้ตรงกับ `SOURCE_MANIFEST.json` หรือ scientific binding ของ run ที่จะ reproduce แล้วใช้ original entry points

| Dataset | จุดเริ่มอ่านคำสั่ง | ขอบเขต |
|---|---|---|
| MOTS20 | [Largest source protocol](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark/blob/172e21b9f2996bae74fb591cfdd1740e6e92dd46/EXPERIMENT_PROTOCOL.md) และ src/benchmark.py ของแต่ละ tier | 5 tiers /17models/2,862frames ตาม frozen config |
| CCTV600 | [Study source README](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/blob/072e205f7d61fa52ec301da50cc65d96451572b7/README.md) และ scripts/study.py --help | quality600 + timing3×100 พร้อม resource guards |

ตัวอย่างลำดับคำสั่งสำหรับ **fresh reproduction workspace** ที่ clone ต้นทางตาม commit และจัดเตรียมข้อมูล/weights แล้ว ให้เลือก RUN_ID ใหม่สำหรับแต่ละรอบ

```bash
# MOTS20 Largest; source phases ใช้ argument ตำแหน่ง phase และ run ID
python YOLO_Large_Seg_MOTS20_Benchmark/src/benchmark.py preflight REPRO_RUN_ID
python YOLO_Large_Seg_MOTS20_Benchmark/src/benchmark.py full REPRO_RUN_ID
python YOLO_Large_Seg_MOTS20_Benchmark/src/benchmark.py timing REPRO_RUN_ID

# CCTV600; prepare คืนตำแหน่ง fresh run directory ให้ใช้ต่อใน launch/status
python YOLO_Instance_Segmentation_CCTV600_Scaling_Study/scripts/study.py prepare \
  --manifest /path/to/accepted600_manifest.csv
python YOLO_Instance_Segmentation_CCTV600_Scaling_Study/scripts/study.py launch \
  --run-dir /path/to/prepared-run-directory
python YOLO_Instance_Segmentation_CCTV600_Scaling_Study/scripts/study.py status \
  --run-dir /path/to/prepared-run-directory
```

ทั้งห้า MOTS20 tiers มี config/entry point ของตัวเองตาม source inventory ต้องใช้ source versions และ guard policies ที่ตรงกันก่อนรันตารางรวม คำสั่ง benchmark ข้างต้นอ่านจาก source CLI จริงและเป็นคู่มือสำหรับการทำซ้ำในอนาคต สถานะการตรวจใหม่ของรอบจัดส่งมอบยังจำกัดตาม quality gates

สำหรับการอ่านคะแนนและตรวจ aggregate ใช้ CSV ใน results ได้โดยไม่ต้องมีภาพหรือ weights canonical metrics ของ source จะไม่ถูกเขียนทับโดยตัวตรวจ handoff สำหรับเอกสารนี้ คำสั่ง launch ต้นทางเป็นคู่มือทำซ้ำเมื่อผู้ใช้เตรียมสิทธิ์ข้อมูลและทรัพยากรครบ

## ระดับการรับรอง

Existing results คือผล GPU ที่เก็บจากรอบเดิม ส่วน newly verified ใน repo นี้คือ file hashes, roster/aggregate consistency, imports, detector contract บน CPU และ synthetic actual-packet→scorer tests การทดลอง GPU inference ของ extracted package และ full rerun บนเครื่องใหม่ยังเป็น NOT_RUN รักษาข้อจำกัดนี้ในการรายงานความพร้อม release
