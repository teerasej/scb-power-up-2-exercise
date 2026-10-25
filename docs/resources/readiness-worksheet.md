---
prev: false
next: false
---

# Readiness worksheet — ทบทวน Agent ที่เราสร้าง

## Practice 1: เปรียบเทียบผลที่คาดหวังกับผลจริง

<PracticeIllustration id="readiness-p01" />

**Primary target:** เปรียบเทียบ Expected Result กับ Actual Result จากสิ่งที่สังเกตระหว่างทำ Exercise

1. เลือกตัวอย่างจาก Instructions, Knowledge, Prompt, flow และ Topic ตามที่ได้ทำจริง
2. บอก `Expected Result` และ `Actual Result` ของแต่ละตัวอย่างจากสิ่งที่สังเกต
3. หากยังไม่ได้ทดลองส่วนใด ให้บอกตามตรงว่ายังไม่ได้ทดสอบ และไม่สรุปจากหน้าตา Agent

**Checkpoint:** อธิบายความต่างระหว่างผลที่คาดหวังกับผลที่เกิดขึ้นจริงได้ และรู้ว่าส่วนใดยังต้องทดลอง

## Practice 2: ระบุ approval point

<PracticeIllustration id="readiness-p02" />

**Primary target:** อธิบายสิ่งที่คนต้องตรวจก่อนส่งต่อ

1. ใช้ CASE-201 บอกข้อเท็จจริง ข้อมูลที่ขาด ผู้ตรวจทาน และ action ที่ต้องยืนยัน
2. อธิบายการ review body/ผู้รับก่อนกด Test ใน flow designer และชี้ guard ปลายทางใน flow
3. อธิบายว่าการเลือก ตรวจแล้ว ใน Topic เป็นคำตอบของผู้ใช้ ไม่ใช่หลักฐานว่าเนื้อหาถูกตรวจจริงหรือส่งแล้ว

**Checkpoint:** ระบุจุดตรวจทั้งเนื้อหาและปลายทางได้ และหยุดทดสอบส่งได้หากยังไม่แน่ใจ

## Practice 3: เล่าเส้นทางที่เชื่อมกัน

<PracticeIllustration id="readiness-p03" />

**Primary target:** อธิบายการส่งต่อข้อมูลระหว่าง components ของ Agent

1. ใช้ [Demo run sheet](demo-run-sheet.md) เลือก Presenter/Operator และ Observer
2. แสดง case notes → Prompt input/output → reviewed body → designer flow inputs → ผลจริง แล้วแสดง Review Readiness เป็นบทสนทนาฝึกอีกส่วนหนึ่ง
3. ให้ Observer เลือกอีกคำตอบใน Review Readiness แล้วเทียบ Message หรือดูกรณี invalid recipient ใน flow designer ตามที่ได้ทดสอบจริง

**Checkpoint:** แยกได้ว่า Prompt จัดสรุป, designer Test รัน flow และ Topic ให้คำแนะนำตามคำตอบ โดยไม่อ้างความสำเร็จที่ยังไม่มีหลักฐาน

## Practice 4: บันทึก gap และการตรวจครั้งต่อไป

<PracticeIllustration id="readiness-p04" />

**Primary target:** ระบุงานแก้ไขที่มีเจ้าของและเกณฑ์ตรวจซ้ำ

1. เติม Gap list จาก failure, Blocked หรือส่วนที่ยังไม่ได้ทดสอบ หากไม่พบ functional gap ให้จดสิ่งที่ยังต้องยืนยันก่อนใช้งานต่อ
2. ระบุ Must fix before demo หรือ Improve later พร้อม owner และวิธีตรวจซ้ำ

**Checkpoint:** มีงานถัดไปที่ตรวจได้ ไม่ใช้ความสวยของคำตอบแทนผลการทดสอบจริง และใช้เฉพาะเกณฑ์ที่ผู้สอนยืนยันแล้ว

<DownloadFile file="readiness-worksheet.md">ดาวน์โหลดแบบฟอร์ม Markdown</DownloadFile>
