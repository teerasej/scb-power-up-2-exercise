---
prev: false
next: false
---

# Readiness worksheet — ทบทวน Agent ที่เราสร้าง

## Practice 1: ทบทวนหลักฐาน

**Primary target:** แยกผลที่ตรวจแล้วจากส่วนที่ยังไม่ได้ทดสอบ

1. เปิด Test log ของ Service Request Assistant เลือกตัวอย่างจาก Instructions, Knowledge, Prompt, flow และ Topic ตามที่ได้ทำจริง
2. บอก Expected, Actual และที่เก็บ source/tool/run evidence ของแต่ละตัวอย่าง
3. ถ้าไม่มี Actual ให้ใส่ Not run ไม่สรุปจากหน้าตา Agent และระบุ instructor evidence แยกจากผลของตน

**Checkpoint:** เห็นว่าส่วนใดตรวจแล้ว ส่วนใดยังต้องทดสอบ และมี boundary case ที่ตรวจได้ตามกิจกรรมที่ทำ

## Practice 2: ระบุ approval point

**Primary target:** อธิบายสิ่งที่คนต้องตรวจก่อนส่งต่อ

1. ใช้ CASE-201 บอกข้อเท็จจริง ข้อมูลที่ขาด ผู้ตรวจทาน และ action ที่ต้องยืนยัน
2. ชี้จุด preview และ Send now ใน Topic พร้อม guard ปลายทางใน flow
3. อธิบายว่า Email entity ช่วยรู้จำอีเมล แต่ไม่ได้อนุญาตให้ส่งไปทุกอีเมล

**Checkpoint:** ระบุจุดตรวจทั้งเนื้อหาและปลายทางได้ และรู้วิธียกเลิกก่อนเรียก flow

## Practice 3: เล่าเส้นทางที่เชื่อมกัน

**Primary target:** อธิบายการส่งต่อข้อมูลระหว่าง components ของ Agent

1. ใช้ [Demo run sheet](demo-run-sheet.md) เลือก Presenter/Operator และ Observer
2. แสดง case notes → Prompt input/output → reviewed body → Topic variables → flow inputs → ผลจริง
3. ให้ Observer ตรวจหนึ่ง boundary เช่น Cancel แล้วบอกสิ่งที่เห็นจาก activity และ mailbox

**Checkpoint:** อธิบายได้ว่า flow ที่ Topic เรียกคือ flow ตัวเดิมจาก Exercise 4 โดยไม่อ้างความสำเร็จที่ยังไม่มีหลักฐาน

## Practice 4: บันทึก gap และการตรวจครั้งต่อไป

**Primary target:** ระบุงานแก้ไขที่มีเจ้าของและเกณฑ์ตรวจซ้ำ

1. เติม Gap list จาก failure, Blocked หรือส่วนที่ยัง Not run หากไม่พบ functional gap ให้จดสิ่งที่ยังต้องยืนยันก่อนใช้งานต่อ
2. ระบุ Must fix before demo หรือ Improve later พร้อม owner และหลักฐานที่จะใช้ retest

**Checkpoint:** มีงานถัดไปที่ตรวจได้ ไม่ใช้ความสวยของคำตอบแทน evidence; บันทึกเฉพาะเกณฑ์ที่ผู้สอนยืนยันแล้ว

<DownloadFile file="readiness-worksheet.md">ดาวน์โหลดแบบฟอร์ม Markdown</DownloadFile>
