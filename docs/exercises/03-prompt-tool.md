---
description: "Exercise 3: Prompt tool — Service Request Assistant"
prev: {"text": "Exercise 2: Knowledge", "link": "/exercises/02-knowledge"}
next: {"text": "Exercise 4: Agent flow", "link": "/exercises/04-agent-flow"}
---

# Exercise 3: Prompt tool — เลือกรูปแบบสรุปด้วย entity

<ExerciseCover image="03-prompt-tool" alt="นำโน้ตชุดเดียวกันมาจัดเป็นเอกสารสองรูปแบบ ทั้งแบบกระชับและแบบละเอียด" position="50% center" />

ผู้ช่วยคนเดิมมี Instructions และคู่มือแล้ว เราจะเพิ่มเครื่องมือที่เปลี่ยนโน้ต CASE-201 เป็น email body โดยเลือกแบบกระชับหรือแบบละเอียด เหมือนสั่งเครื่องดื่มที่มีช่องเลือกขนาด: **input** คือช่องในใบสั่ง, **entity** ช่วยรู้ว่าคำที่บอกหมายถึงตัวเลือกใด, และค่าที่เก็บไว้จะถูกส่งให้ Prompt ใช้ครับ

**ผลลัพธ์:** Prompt tool ที่รับ CaseNotes และ BriefStyle พร้อม email body ที่ตรวจแล้วสำหรับ Exercise 4

> **License:** ต้องตรวจสอบสิทธิ์ Copilot Studio, native Prompt, model/region และ capacity ก่อนเริ่มอบรม ไม่ถือว่ามี Microsoft 365 Copilot แล้วจะใช้ทุกความสามารถได้

## Prerequisites

- Service Request Assistant จาก Exercise 2 มีคู่มือหลักสามฉบับเป็น `Ready` และนำ Conflict notice ออกแล้ว
- <DownloadFile file="case-notes-03.txt">Case notes 03</DownloadFile>, <DownloadFile file="format-service-brief-prompt.txt">Prompt template</DownloadFile>, <DownloadFile file="agent-3-instructions.txt">Instructions หลัง Exercise 3</DownloadFile>
- <DownloadFile file="test-log.csv">Test log</DownloadFile>

---

## Practice 1: สร้าง Prompt ที่รับข้อมูลสองช่อง

<PracticeIllustration id="ex03-p01" />

**Primary target:** สร้าง Prompt ที่ใช้ input chips จริงเพื่อจัดบันทึกเป็น email body

1. เปิด Agent ตัวเดิม ไปที่ `Tools` > `Add a tool` > `Prompt` หาก UI มี `New tool` ให้เลือก Prompt จากรายการนั้น
2. ตั้งชื่อ Prompt

   ```text
   Format Service Brief
   ```

3. ใน Prompt editor ใช้ `Add content` สร้าง input ชนิด `Text` สองตัว ตั้งชื่อแยกกันดังนี้

   - **Input สำหรับบันทึก**

     ```text
     CaseNotes
     ```

   - **Input สำหรับรูปแบบ**

     ```text
     BriefStyle
     ```

4. วางเนื้อหาจาก Prompt template ลงในช่องคำสั่ง เพิ่ม input chip `CaseNotes` ใต้บรรทัด `Case notes:` และ input chip `BriefStyle` ใต้บรรทัด `Brief style:` ไม่ใช้ชื่อ input ที่พิมพ์เป็นข้อความแทน chip
5. ในส่วนทดสอบของ Prompt ใส่เนื้อหาจาก Case notes 03 ใน `CaseNotes` แล้วกรอก `BriefStyle`

   ```text
   Concise
   ```

6. กด `Test` ตรวจหัวข้อ Case ID / Request / Confirmed facts / Missing information / Next questions และตรวจวันที่ยื่นกับชนิดเอกสารที่ยังขาด
7. เปลี่ยนเฉพาะ `BriefStyle` แล้วทดสอบอีกครั้ง

   ```text
   Detailed
   ```

8. เปรียบเทียบว่ารายละเอียดเปลี่ยนได้ แต่ข้อเท็จจริงยังเหมือนเดิม แล้ว `Save` > `Add and configure` ตาม UI ที่ปรากฏ

### Checkpoint

Prompt รับ input สองช่องและสร้าง body ได้ทั้งสองแบบ การทดสอบตรงใน Prompt editor ยืนยันการทำงานของ Prompt แต่ยังไม่ได้ทดสอบการรู้จำ entity ในบทสนทนา

---

## Practice 2: ให้ input รู้จัก BriefStyle entity

<PracticeIllustration id="ex03-p02" />

**Primary target:** เชื่อม input ของ Tool กับ closed-list entity เพื่อรับตัวเลือกและคำพ้อง

1. ที่ Agent เปิด `Settings` > `Entities` แล้วเลือกสร้าง entity ชนิด `Closed list`
2. ตั้งชื่อ entity

   ```text
   BriefStyle
   ```

3. เพิ่ม `List items` ทีละค่า และเพิ่มคำพ้องใน `Synonyms` แยกแต่ละคำ

   - **ค่าหลักรายการแรก**

     ```text
     Concise
     ```

     **คำพ้องคำแรก**

     ```text
     สั้น
     ```

     **คำพ้องคำที่สอง**

     ```text
     กระชับ
     ```

   - **ค่าหลักรายการที่สอง**

     ```text
     Detailed
     ```

     **คำพ้องคำแรก**

     ```text
     ละเอียด
     ```

     **คำพ้องคำที่สอง**

     ```text
     แบบละเอียด
     ```

4. คง `Smart matching` เป็น Off แล้ว `Save` เพื่อทดลองจากรายการและคำพ้องที่เรากำหนดเอง
5. กลับไป `Tools` > `Format Service Brief` เปิดส่วน `Inputs` ที่แถว `BriefStyle` เลือก `Fill using` เป็น `Dynamically fill with AI`
6. เลือก `Customize` ของ input นี้ ตั้ง `Identify as` เป็น entity `BriefStyle` ที่สร้างไว้ แล้วใส่ Description

   ```text
   Required brief style selected by the user: Concise or Detailed. Ask the user to choose if no style was supplied. Do not invent a default.
   ```

7. คง `CaseNotes` เป็น input ข้อความ ตั้ง Description เพื่อให้รู้ว่าต้องรับอะไร

   ```text
   The complete fictional case notes supplied by the user. Preserve the notes as source data; do not add missing facts.
   ```

8. ในรายละเอียด Tool ตั้ง Description แล้ว `Save`

   ```text
   Formats supplied fictional case notes into a Thai training email body using the user's selected brief style. Returns content for review; never sends email.
   ```

### Checkpoint

แสดงให้คู่ฝึกดูได้ว่า entity ถูกผูกกับ `BriefStyle` ในหน้าตั้งค่า Tool ไม่ใช่เพียงเพิ่มชื่อ entity ลงในข้อความ Prompt

> **Tip:** `Text` ใน Prompt editor คือชนิด input ส่วน `Identify as` ใน Tool configuration ช่วยตีความสิ่งที่ผู้ใช้บอก ทั้งสองส่วนทำคนละหน้าที่

---

## Practice 3: ตรวจค่าที่ Agent ส่งให้ Prompt

<PracticeIllustration id="ex03-p03" />

**Primary target:** ตรวจการเรียก Tool และค่ารูปแบบที่รู้จำจากบทสนทนา

1. เปิด `Instructions` ของ Agent แล้วเพิ่มกติกาต่อไปนี้ โดยคงข้อความจาก Exercises 1–2

   ```text
   Use Format Service Brief when the user asks to format supplied notes as an email body.
   Collect CaseNotes and the user's BriefStyle before calling it. Ask for a style if it is missing.
   Show its output for review. Formatting and revision never send email.
   ```

2. `Save` เริ่ม session ใหม่ใน `Test your agent` วาง Case notes 03 แล้วต่อท้ายคำขอนี้

   ```text
   ใช้ Format Service Brief จัด CASE-201 เป็น email body แบบกระชับ สำหรับ review ยังไม่ต้องส่ง
   ```

3. เปิด activity ของการทดสอบ ตรวจว่ามี Tool call จริง ดู input `CaseNotes` และ `BriefStyle` คำว่า กระชับ ควรเชื่อมกับ `Concise` บันทึกค่าที่เห็นจริงเป็น T01 และ T08 หากดู input ไม่ได้ให้ระบุ gap ไม่อนุมานจากหน้าตาคำตอบ
4. เริ่ม session ใหม่ วางบันทึกเดิมแล้วขออีกแบบ

   ```text
   ใช้ Format Service Brief จัด CASE-201 เป็น email body แบบละเอียด สำหรับ review ยังไม่ต้องส่ง
   ```

5. ตรวจ input และผลลัพธ์เทียบกับต้นฉบับ ทั้งสองแบบต้องไม่แต่งวันที่ยื่น ผลตรวจระบบ หรือกำหนดเสร็จ
6. เลือก body ฉบับที่ต้องการ ตรวจข้อเท็จจริงแล้วเก็บในโน้ตส่วนตัว แยก body ออกจากบทสนทนาและคำอธิบายของ Agent
7. เทียบ Instructions ปัจจุบันกับ <DownloadFile file="agent-3-instructions.txt">snapshot หลัง Exercise 3</DownloadFile> เก็บผลที่ยังไม่ผ่านใน <DownloadFile file="gap-list.csv">Gap list</DownloadFile>

### Checkpoint

เห็นค่าที่ส่งเข้า Prompt และมี body ฉบับที่ review แล้ว การ format ยังไม่ส่ง email

## Summary และสิ่งที่จะใช้ต่อ

Agent มีเครื่องมือจัดรูปแบบแล้ว แต่ยังไม่มีเครื่องมือส่ง ใน Exercise 4 เราจะนำ body ที่ตรวจแล้วไปเป็น input ทดสอบของ Agent flow เก็บ Agent และ Prompt ตัวเดิมไว้ครับ

[กลับสารบัญ](/) | [Exercise 4: Agent flow](/exercises/04-agent-flow)
