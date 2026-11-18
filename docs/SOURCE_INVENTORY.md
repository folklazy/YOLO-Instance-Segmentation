# Source inventory และการคัดเลือก

ตรวจ 12 Git repositories ต้นทาง โดย HEAD ทุกแห่งตรง remote main ณ เวลาตรวจ และตรวจ branch refs, tracked changes, untracked files และ symlinks ด้วย inventory ก่อนคัดไฟล์

| Repository | Branch / HEAD | Untracked | Remote main ตรง |
|---|---|---:|---|
| [YOLO_Instance_Segmentation_CCTV600_Scaling_Study](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study/tree/072e205f7d61fa52ec301da50cc65d96451572b7) | main / `072e205f7d61fa52ec301da50cc65d96451572b7` | 0 | True |
| [YOLO_Instance_Segmentation_MOTS20_Scaling_Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/tree/5551593459646fe42494958192e5410805ab4b48) | main / `5551593459646fe42494958192e5410805ab4b48` | 1 | True |
| [YOLO_Large_Seg_CCTV600_Benchmark](https://github.com/folklazy/YOLO_Large_Seg_CCTV600_Benchmark/tree/9106881f5a9885383db48da94ae173e97acfb7fc) | main / `9106881f5a9885383db48da94ae173e97acfb7fc` | 0 | True |
| [YOLO_Large_Seg_MOTS20_Benchmark](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark/tree/172e21b9f2996bae74fb591cfdd1740e6e92dd46) | main / `172e21b9f2996bae74fb591cfdd1740e6e92dd46` | 78 | True |
| [YOLO_Medium_Seg_CCTV600_Benchmark](https://github.com/folklazy/YOLO_Medium_Seg_CCTV600_Benchmark/tree/27d909e73e31904f5761bca9533e2b31a491e3b3) | main / `27d909e73e31904f5761bca9533e2b31a491e3b3` | 0 | True |
| [YOLO_Medium_Seg_MOTS20_Benchmark](https://github.com/folklazy/YOLO_Medium_Seg_MOTS20_Benchmark/tree/40df395545754be0847f6aa144ffb59f63389af6) | main / `40df395545754be0847f6aa144ffb59f63389af6` | 0 | True |
| [YOLO_Nano_Seg_CCTV600_Benchmark](https://github.com/folklazy/YOLO_Nano_Seg_CCTV600_Benchmark/tree/f480d7a1b78ad2a1d48991f2a37cf9feda244f3b) | main / `f480d7a1b78ad2a1d48991f2a37cf9feda244f3b` | 0 | True |
| [YOLO_Nano_Seg_MOTS20_Benchmark](https://github.com/folklazy/YOLO_Nano_Seg_MOTS20_Benchmark/tree/c4ceca0aaba1982d10cfa3fe9d4209baab0dba96) | main / `c4ceca0aaba1982d10cfa3fe9d4209baab0dba96` | 0 | True |
| [YOLO_Second_Largest_Seg_CCTV600_Benchmark](https://github.com/folklazy/YOLO_Second_Largest_Seg_CCTV600_Benchmark/tree/f8829cf11a66c035bea1a9a6106d3fca5cbf9074) | main / `f8829cf11a66c035bea1a9a6106d3fca5cbf9074` | 0 | True |
| [YOLO_Second_Largest_Seg_MOTS20_Benchmark](https://github.com/folklazy/YOLO_Second_Largest_Seg_MOTS20_Benchmark/tree/3c0bd7845166d23df1eb52d312e24fad930f9298) | main / `3c0bd7845166d23df1eb52d312e24fad930f9298` | 0 | True |
| [YOLO_Small_Seg_CCTV600_Benchmark](https://github.com/folklazy/YOLO_Small_Seg_CCTV600_Benchmark/tree/b49325b06c7956b7bae82ba923401652686fea28) | main / `b49325b06c7956b7bae82ba923401652686fea28` | 0 | True |
| [YOLO_Small_Seg_MOTS20_Benchmark](https://github.com/folklazy/YOLO_Small_Seg_MOTS20_Benchmark/tree/56adbc9f8dfcbbfe37c9a254cb04007650427617) | main / `56adbc9f8dfcbbfe37c9a254cb04007650427617` | 0 | True |

MOTS20 Largest มี runtime/evaluator และ requirements บางไฟล์อยู่เฉพาะเครื่อง จึงคัดจาก workspace พร้อม SHA256 และระบุ LOCAL_ONLY ใน manifest การมีชื่อ branch ตรงกับ remote ยังไม่ครอบคลุมไฟล์ untracked เหล่านี้

| หมวด | วิธีจัดการ |
|---|---|
| Production / Reusable Code | Extract detector เฉพาะส่วน YOLO ของเว็บ, MOTS mask scorer/loader และ CCTV reference package พร้อม tests |
| Research Evidence | คัด aggregate CSV และกราฟตามบทบาท พร้อม source/copy hashes |
| Documentation | เขียนเอกสารส่งมอบตามหน้าที่ เชื่อมรายงานต้นฉบับแบบ commit-pinned |
| Experimental / Exploratory | เก็บ pilot/debug/source variants ที่ต้นทาง พร้อมเหตุผลใน inventory |
| Generated / Large Artifacts | คง checkpoints, raw predictions, caches และ raw logs ภายนอก repository |
| Sensitive / Restricted | เก็บภาพและ annotations CCTV, per-image records และ secrets ในพื้นที่ private |

## ไฟล์และการตรวจย้อนหลัง

[FILE_INVENTORY.csv](../provenance/FILE_INVENTORY.csv) ให้คำตัดสิน candidate สาธารณะครบ 1,205 รายการ ส่วน inventory ทุกไฟล์ 73,991 รายการเก็บ private ที่ logical location `YOLO-Instance-Segmentation.local/curation-20261119/FILE_INVENTORY.csv` รวม 12 repos และ Person_Segmentation_Pilot; checkpoint inventory มี metadata แยกใน models/MANIFEST.json

[SELECTED_FILES.json](../provenance/SELECTED_FILES.json) ระบุตำแหน่งเดิม commit/branch สถานะ LOCAL_ONLY, destination, SHA256 และ transformation ทุกไฟล์ที่คัดมา ส่วน code/config ของ runtime ที่ extract ใหม่มี source binding ใน configs/selected_yolo26x.json และ tests เทียบ kwargs กับ binding นี้

โค้ด CLI, integration contract และ acceptance tests ที่เขียนใหม่เป็น packaging additions สำหรับ API0.1.0 ผลโมเดลและผล benchmark อ้างการรันเดิมตาม source commits

## Layout ที่เลือก

package หลักแยกจาก reference benchmark เพื่อให้ integration ใช้เฉพาะ inference contract ได้ CCTV reference เก็บ modules ที่อ้างกันครบและรักษา config/scientific bindings เดิม ผู้รับงานทำ replay ที่ต้องใช้ private artifacts ผ่าน source workspace ตามคู่มือ reproducing ส่วน CPU synthetic tests ใช้ reference ได้จาก clone นี้

## สิ่งที่คงไว้ต้นทาง

รายงาน tier หลายภาษา, source snapshots, debug manifests, branch histories และข้อมูลรายภาพยังอยู่ต้นทาง เลือกเชื่อมผ่าน [evidence index](EVIDENCE_INDEX.md) เพื่อรักษาบริบทของข้อสรุปเดิมและการแก้ผลก่อนหน้า
