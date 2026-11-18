# วิเคราะห์ภาพจากผลการทดลองเดิม

ภาพต่อไปนี้เป็น saved prediction comparisons ที่มีอยู่ก่อนรอบจัดส่งมอบ ตรวจไฟล์จริงบนเครื่องแล้วและอ้างภาพจาก commit ต้นทางโดยตรง การเลือกกรณีเป็น diagnostic หลังเห็นผล มีทั้ง control, ความต่าง และ common failure

## MOTS20 — ความต่างของ coverage

![YOLO26x versus l, case1](https://raw.githubusercontent.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/5551593459646fe42494958192e5410805ab4b48/outputs/visualizations/yolo26x_vs_yolo26l/v1/case_01_comparison.png)

กรณี MOTS20-02/000336 ใช้ original/GT และผลบนเฟรมเดียวกัน YOLO26x มี TP11/FP0/FN1 ส่วน l มี TP8/FP2/FN4 จาก panel แสดงคนหลายขนาดและคนหน้าฉากที่บังกันบางส่วน ทั้งคู่คืนรูปร่างคนหลักได้ แต่ coverage ของคนในฉากต่างกัน Source diagnostic ระบุว่าบางคนผ่าน confidence ใน x แต่ไม่ผ่านใน l การตัดสินจากภาพ overlay อย่างเดียวอาจมองข้ามคนเล็กที่อยู่ลึกในฉาก

การเห็นผลต่างในเฟรมนี้รองรับคำอธิบายระดับ output/threshold ของสอง checkpoints การแยกผล architecture และข้อมูลฝึกต้องอาศัยการทดลองควบคุมเพิ่มเติม [รายงานและ source evidence](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/5551593459646fe42494958192e5410805ab4b48/YOLO26X_VS_YOLO26L_VISUAL_TH.md)

## MOTS20 — เก็บคนครบเท่ากันแต่ทายเกินต่างกัน

![Near-tie case3](https://raw.githubusercontent.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/5551593459646fe42494958192e5410805ab4b48/outputs/visualizations/near_tie_26s_11x_v9e/v1/case_03_comparison.png)

กรณี MOTS20-11/000450 แสดง TP9/FN0 ของ YOLO26s, YOLO11x และ YOLOv9e โดย v9e มี FP2 ใน panel ส่วนที่ดูเป็นคนครบจึงยังมี extra masks เพิ่มเป็นภาระ downstream ในบริเวณอื่นของฉาก การดู Recall ร่วมกับ Precision และ masks ช่วยอธิบายความต่างนี้ได้ [แหล่งวิเคราะห์](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/5551593459646fe42494958192e5410805ab4b48/NEAR_TIE_26S_11X_V9E_VISUAL_TH.md)

## MOTS20 — shared failure และคุณภาพขอบเขต

![Shared failure case5](https://raw.githubusercontent.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/5551593459646fe42494958192e5410805ab4b48/outputs/visualizations/yolo26x_vs_yolo26l/v1/case_05_comparison.png)

กรณี MOTS20-09/000263 มีคนเดินผ่านกันและบังกันบางส่วน x และ l ได้ TP9/FP2/FN4 เท่ากัน แม้มี predicted silhouette อยู่ในบริเวณคนจริง ผลอาจไม่ผ่าน confidence/IoU ของ GT คนนั้น Source diagnostic เก็บ candidate/matching เพิ่มไว้ จึงต้องใช้หลักฐานนั้นประกอบเพื่อแยกการพลาดคนออกจาก mask ที่ซ้อนคนผิดเจ้าของ ขอบขาและช่วงคนติดกันเป็นพื้นที่ที่ตรวจดูจากภาพประกอบได้ แต่ผล TP-only IoU เฉลี่ยของทั้ง dataset ยังใช้แทน mask ของคนทุกคนในภาพไม่ได้

## CCTV600 — ขนาด แสง มุมกล้อง และการบดบัง

เปิดดู private Case C ของ Largest จริงในการจัดส่งมอบรอบนี้ ภาพเป็นกล้องมุมสูง มีพื้นที่มืดสลับแสงจ้า โครงสร้างและพืชบังบางส่วน คนมีขนาดเล็กและรายละเอียดจำกัด ทั้งสี่ checkpoints กลุ่ม Largest มี TP0/FP0/FN3 ตาม annotation bbox ที่เข้าเกณฑ์เดียวกัน ข้อมูลนี้แสดง failure ร่วมในกรณีดังกล่าว แต่ภาพเดียวแยกสาเหตุของขนาด blur แสง และมุมกล้องออกจากกันไม่ได้

Case A ตรวจคนถูกตัดด้วยขอบภาพและ Case B ตรวจคนหลังโครงสร้างบัง ตามรายงานเดิมทุกโมเดลกลุ่ม Largest จับ eligible GT ครบในสองกรณีนั้น โดย Case B มี unmatched FP ของ YOLO11x ส่วน Case D เป็นภาพไม่มี eligible GT ตามขอบเขตที่รับรอง ผลของกรณีเหล่านี้จึงต้องอ่านคู่กับ inventory และ ignore policy

[รายละเอียดและตำแหน่ง private gallery](https://github.com/folklazy/YOLO_Large_Seg_CCTV600_Benchmark/blob/9106881f5a9885383db48da94ae173e97acfb7fc/PRESENTATION_SUMMARY_TH.md) มี manifest ผูก packet/input hashes และ ROI เดียวกันทุกโมเดล ภาพ CCTV และ annotation ไม่ถูกคัดเข้าชุดส่งมอบ public นี้

## Coverage ของการวิเคราะห์

Small persons, occlusion และ segmentation boundaries มีตัวอย่าง MOTS20 ที่ตรวจภาพจริง แสงจ้า/มืด มุมกล้องสูง และภาพเบลอใช้ CCTV Case C เป็นตัวอย่างร่วมของความยาก ส่วนหลักฐานเชิงเหตุแยกปัจจัยแต่ละข้อยังเป็น NOT_VERIFIED การคัดกรณีเหล่านี้ใช้เพื่ออธิบายพฤติกรรม จึงไม่ใช้ประมาณอัตรา failure ของ dataset ทั้งชุด

ภาพ MOTS20 อ้างไปยังงานเดิมที่เผยแพร่อยู่แล้ว ไม่บรรจุภาพ dataset เพิ่มใน repo นี้ ผู้รับงานตรวจเงื่อนไขของ dataset เมื่อจะนำภาพไปเผยแพร่ในบริบทอื่น
