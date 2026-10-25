---
description: "Exercise 5: Topics — รู้จักบทสนทนาแบบเลือกเส้นทาง"
prev: {"text": "Exercise 4: Agent flow", "link": "/exercises/04-agent-flow"}
next: {"text": "ทดลองบันทึกผลด้วย Test log", "link": "/resources/test-log"}
---

# Exercise 5: Topics — รู้จักบทสนทนาแบบเลือกเส้นทาง

<ExerciseCover image="05-topics" alt="เจ้าหน้าที่ถามสถานะการตรวจสรุปและเลือกคำแนะนำตามคำตอบของผู้ใช้" position="50% center" />

เรามีสรุป CASE-201 และได้ฝึก Agent flow ใน Exercise 4 แล้ว คราวนี้ลองทำ Topic เล็ก ๆ บน Service Request Assistant ตัวเดิม เหมือนเจ้าหน้าที่หน้าเคาน์เตอร์ที่ถามหนึ่งคำถาม แล้วเลือกคำแนะนำให้ตรงกับคำตอบครับ

**ผลลัพธ์:** Topic ชื่อ Review Readiness ที่มีหนึ่งคำถาม สองตัวเลือก และข้อความตอบกลับตามแต่ละตัวเลือก กิจกรรมนี้ให้คำแนะนำเรื่องการตรวจสรุป โดยไม่มีการส่ง email

> **Harness / access:** ใช้ Copilot Studio **standard harness** และสิทธิ์สร้าง/แก้ไข Topics ซึ่งต้องตรวจสอบก่อนเริ่มอบรม กิจกรรมนี้ไม่ต้องใช้ starter Topic หรือ Outlook connection

## Prerequisites

- Service Request Assistant ตัวเดิม และสรุป CASE-201 ที่เก็บไว้จาก Exercise 3

## Practice 1: สร้างคำถามและคำแนะนำสองเส้นทาง

<PracticeIllustration id="ex05-p01" />

**Primary target:** ให้คำตอบของผู้ใช้เลือก Message ที่ตรงกันใน Topic

1. เปิด Agent ตัวเดิม
2. ไปที่หน้า `Topics` เลือก `Add a topic` > `From blank` แล้วตั้งชื่อ

   ```text
   Review Readiness
   ```

3. ที่ Trigger แบบ `The agent chooses` ใส่คำอธิบายว่า Topic จะถูก agent เรียกใช้ในกรณีไหนบ้าง

   ```text
   Use when the user wants to check whether the brief is ready. Ask whether the facts have been reviewed, then provide guidance based on the answer. This topic does not send email or call a flow.
   ```

4. ใต้ Trigger เพิ่ม `Ask a question` node แล้ววางคำถาม

   ```text
   ตรวจสอบข้อเท็จจริงในสรุป CASE-201 แล้วหรือยัง?
   ```

5. ตั้ง `Identify` เป็น `Multiple choice options` เพิ่มสองตัวเลือกทีละค่า คงตัวแปรที่ระบบสร้างใน `Save user response as` ไว้ตามเดิม

   - **ตัวเลือกแรก**

     ```text
     ตรวจแล้ว
     ```

   - **ตัวเลือกที่สอง**

     ```text
     ยังต้องแก้
     ```

6. ใช้ branch ของแต่ละตัวเลือกที่แสดงบน canvas แล้วเพิ่ม `Send a message` หนึ่งข้อความต่อ branch หากยังไม่เห็นทางแยก ให้ผู้สอนช่วยตรวจ canvas ก่อนทำต่อ

   - **branch ตรวจแล้ว**

     ```text
     ก่อนส่งต่อ ให้ตรวจ Case ID ข้อเท็จจริง ข้อมูลที่ยังขาด และผู้รับอีกครั้ง การเลือกคำตอบนี้ยังไม่ได้ส่ง email
     ```

   - **branch ยังต้องแก้**

     ```text
     แก้สรุป CASE-201 ให้ตรงกับบันทึก ระบุข้อมูลที่ยังขาดให้ชัดเจน แล้วตรวจข้อเท็จจริงอีกครั้งก่อนส่งต่อ
     ```

7. กด `Save`
8. ตรวจว่า Topic มีหนึ่ง Question สองตัวเลือก และสอง Message โดยไม่มี tool/action สำหรับส่งข้อมูล
9. กลับไปหน้า `Overview` ของ Agent แล้วเพิ่ม guideline นี้ต่อท้าย `Instructions` โดยเก็บข้อความเดิมไว้

   ```text
   ## Review readiness guideline
   - Use the Review Readiness topic when the user asks to check whether the brief is ready. This check must not send email or call the sending flow.
   ```

   แทนชื่อ `Review Readiness` ในข้อความด้วยการอ้างอิง Topic จริง โดยลบเฉพาะชื่อ วางเคอร์เซอร์ที่เดิม แล้วกด `+ Add` เพื่อเลือก Topic `Review Readiness` จากนั้นกด `Save`

10. เริ่ม session ใหม่ใน `Test your agent` ส่งข้อความนี้ แล้วเลือก **ตรวจแล้ว** ตรวจว่าข้อความตรงกับ branch แรก

   ```text
   ช่วยตรวจความพร้อมของสรุป CASE-201
   ```

11. เริ่ม session ใหม่ ส่งข้อความทดสอบเดิมจากขั้น 10 ที่แสดงด้านล่าง แล้วเลือก **ยังต้องแก้** ตรวจว่าข้อความตรงกับ branch ที่สอง ดูเส้นทางที่ทำงานจริงใน canvas/activity หาก Topic ไม่ทำงาน ให้ผู้สอนช่วยตรวจ Trigger

   ```text
   ช่วยตรวจความพร้อมของสรุป CASE-201
   ```


### Checkpoint

เลือก **ตรวจแล้ว** และ **ยังต้องแก้** ในคนละ session แล้วเห็น Message ที่ตรงกับตัวเลือก ชี้ Question และสองเส้นทางบน canvas ได้

## สิ่งที่ควรจำ

Topic ช่วยกำหนดเส้นทางบทสนทนา ส่วน flow จาก Exercise 4 เป็นเครื่องมือทำงานที่เราได้ทดสอบด้วยตนเอง การเลือกคำตอบใน Topic นี้ไม่ได้เรียก flow และไม่ได้รับรองว่าเนื้อหาผ่านการตรวจจริง


[กลับสารบัญ](/) | [ทดลองบันทึกผลด้วย Test log](/resources/test-log)
