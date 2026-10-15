---
description: "Exercise 5: Topics — รู้จักบทสนทนาแบบเลือกเส้นทาง"
prev: {"text": "Exercise 4: Agent flow", "link": "/exercises/04-agent-flow"}
next: {"text": "ทบทวนหลักฐานและ gap", "link": "/resources/readiness-worksheet"}
---

# Exercise 5: Topics — รู้จักบทสนทนาแบบเลือกเส้นทาง

<ExerciseCover image="05-topics" alt="เจ้าหน้าที่ถามสถานะการตรวจสรุปและเลือกคำแนะนำตามคำตอบของผู้ใช้" position="50% center" />

เรามีสรุป CASE-201 และได้ฝึก Agent flow ใน Exercise 4 แล้ว คราวนี้ลองทำ Topic เล็ก ๆ บน Service Request Assistant ตัวเดิม เหมือนเจ้าหน้าที่หน้าเคาน์เตอร์ที่ถามหนึ่งคำถาม แล้วเลือกคำแนะนำให้ตรงกับคำตอบครับ

**ผลลัพธ์:** Topic ชื่อ Review Readiness ที่มีหนึ่งคำถาม สองตัวเลือก และข้อความตอบกลับตามแต่ละตัวเลือก กิจกรรมนี้ให้คำแนะนำเรื่องการตรวจสรุป โดยไม่มีการส่ง email

> **Harness / access:** ใช้ Copilot Studio **standard harness** และสิทธิ์สร้าง/แก้ไข Topics ซึ่งต้องตรวจสอบก่อนเริ่มอบรม กิจกรรมนี้ไม่ต้องใช้ starter Topic หรือ Outlook connection

## Prerequisites

- Service Request Assistant ตัวเดิม และสรุป CASE-201 ที่เก็บไว้จาก Exercise 3
- <DownloadFile file="test-log.csv">Test log</DownloadFile> สำหรับ Q01–Q03

## Practice 1: สร้างคำถามและคำแนะนำสองเส้นทาง

**Primary target:** ให้คำตอบของผู้ใช้เลือก Message ที่ตรงกันใน Topic

1. เปิด Agent ตัวเดิม ไปที่ `Topics` เลือก `Add a topic` > `From blank` แล้วตั้งชื่อ

   ```text
   Review Readiness
   ```

2. ที่ Trigger แบบ `The agent chooses` ใส่คำอธิบายว่า Topic นี้ใช้เมื่อใด หากเป็น `User says a phrase` ให้ใช้ข้อความทดสอบในขั้น 7 เป็น trigger phrase โดยให้ผู้สอนช่วยตรวจตาม UI ที่ปรากฏ

   ```text
   ใช้เมื่อผู้ใช้ต้องการตรวจความพร้อมของสรุป CASE-201 โดยถามว่าตรวจข้อเท็จจริงแล้วหรือยัง แล้วให้คำแนะนำตามคำตอบ Topic นี้ไม่ส่ง email และไม่เรียก flow
   ```

3. ใต้ Trigger เพิ่ม `Ask a question` แล้ววางคำถาม

   ```text
   สรุป CASE-201 ผ่านการตรวจข้อเท็จจริงแล้วหรือยัง?
   ```

4. ตั้ง `Identify` เป็น `Multiple choice options` เพิ่มสองตัวเลือกทีละค่า คงตัวแปรที่ระบบสร้างใน `Save user response as` ไว้ตามเดิม

   - **ตัวเลือกแรก**

     ```text
     ตรวจแล้ว
     ```

   - **ตัวเลือกที่สอง**

     ```text
     ยังต้องแก้
     ```

5. ใช้ branch ของแต่ละตัวเลือกที่แสดงบน canvas แล้วเพิ่ม `Send a message` หนึ่งข้อความต่อ branch หากยังไม่เห็นทางแยก ให้ผู้สอนช่วยตรวจ canvas ก่อนทำต่อ

   - **branch ตรวจแล้ว**

     ```text
     ก่อนส่งต่อ ให้ทบทวน Case ID ข้อเท็จจริง ข้อมูลที่ขาด และปลายทางอีกครั้ง การตอบข้อนี้ยังไม่ได้ส่ง email
     ```

   - **branch ยังต้องแก้**

     ```text
     กลับไปแก้สรุป CASE-201 ให้ตรงกับโน้ต แยกข้อมูลที่ยังไม่มี แล้วตรวจข้อเท็จจริงใหม่ก่อนส่งต่อ
     ```

6. ให้แต่ละ branch จบหลัง Message ของตน ไม่เชื่อมสองข้อความให้แสดงต่อกัน แล้ว `Save` ตรวจว่า Topic มีหนึ่ง Question สองตัวเลือก และสอง Message โดยไม่มี tool/action สำหรับส่งข้อมูล
7. เริ่ม session ใหม่ใน `Test your agent` ส่งข้อความนี้ แล้วเลือก **ตรวจแล้ว** ตรวจว่าข้อความตรงกับ branch แรก บันทึก Q01

   ```text
   ช่วยตรวจความพร้อมของสรุป CASE-201
   ```

8. เริ่ม session ใหม่ ส่งข้อความเดิม แล้วเลือก **ยังต้องแก้** ตรวจว่าข้อความตรงกับ branch ที่สอง บันทึก Q02 ดูเส้นทางที่ทำงานจริงใน canvas/activity หาก Topic ไม่ทำงาน ให้บันทึก gap และให้ผู้สอนตรวจ Trigger
9. ให้ผู้สอนช่วยตรวจ Q03 โดยเริ่ม session ใหม่ เข้า Topic แล้วตอบคำที่ไม่ตรงกับตัวเลือก เช่นข้อความนี้ สังเกตการถามใหม่หรือ fallback ตามค่าจริง ต้องไม่ถือว่าผู้ใช้เลือก **ตรวจแล้ว** และต้องไม่มี flow call หรือ email เพิ่ม

   ```text
   ขอข้ามคำถามนี้
   ```

### Checkpoint

เลือก **ตรวจแล้ว** และ **ยังต้องแก้** ในคนละ session แล้วเห็น Message ที่ตรงกับตัวเลือก ชี้ Question และสองเส้นทางบน canvas ได้ หากยังไม่มีผลจริงให้คง `Not run` หรือบันทึก `Blocked`

## สิ่งที่ควรจำ

Topic ช่วยกำหนดเส้นทางบทสนทนา ส่วน flow จาก Exercise 4 เป็นเครื่องมือทำงานที่เราได้ทดสอบด้วยตนเอง การเลือกคำตอบใน Topic นี้ไม่ได้เรียก flow และไม่ได้รับรองว่าเนื้อหาผ่านการตรวจจริง

Topics และ Question nodes ในกิจกรรมนี้อยู่ใน **standard harness** ส่วน **GitHub Copilot harness** มีวิธีสร้างและควบคุม Agent ต่างออกไป ไม่ต้องสร้าง Topic นี้ซ้ำใน harness นั้น ผู้สอนจะเปรียบเทียบให้ดูใน demonstration ตาม [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview)

หากต้องเทียบสถานะ Instructions ใช้ <DownloadFile file="agent-5-instructions.txt">Instructions หลัง Exercise 5</DownloadFile> ไฟล์นี้เป็นจุดเทียบข้อความ ไม่ได้สร้าง Topic ให้โดยอัตโนมัติ

[กลับสารบัญ](/) | [ทบทวนหลักฐานและ gap](/resources/readiness-worksheet.md)
