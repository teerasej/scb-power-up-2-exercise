---
title: ดาวน์โหลดไฟล์ฝึก
prev: false
next: false
---

# ดาวน์โหลดไฟล์ฝึก

ไฟล์ชุดนี้ใช้กับห้า Exercise ปัจจุบัน ข้อมูลทั้งหมดเป็นข้อมูลสมมติสำหรับฝึก ไม่ใช่นโยบายหรือข้อมูลจริงของ SCB ดาวน์โหลดทั้งหมดเป็น ZIP หรือเลือกเป็นรายไฟล์ แล้วเก็บในโฟลเดอร์ฝึกของตนเองครับ

## ดาวน์โหลดทั้งหมด

<DownloadFile file="power-up-2-sample-files.zip">ดาวน์โหลดไฟล์ฝึกทั้งหมด (ZIP)</DownloadFile>

ZIP รวมไฟล์ฝึก แบบบันทึก และสไลด์ PDF เดิมทั้ง 15 ไฟล์ พร้อมคู่มือแบบฝึกหัดออฟไลน์ และโฟลเดอร์ `copy-text/` สำหรับคัดลอกข้อความทุก code block แตกไฟล์ก่อนเริ่มใช้งาน และคงชื่อไฟล์เดิมไว้

## คู่มือแบบฝึกหัดออฟไลน์ (A4)

<DownloadFile file="SCB-Power-Up-2-Offline-Exercise-Guide.pdf">ดาวน์โหลดคู่มือแบบฝึกหัดออฟไลน์ (PDF)</DownloadFile>

รวมก่อนเริ่ม Exercises 1–5 ทุก Practice, Readiness และ Demo run sheet พร้อมสารบัญกดได้ Bookmarks และลิงก์กลับสารบัญทุกหน้า ใช้อ่านคำสั่งเมื่อเข้าเว็บไซต์ไม่ได้ ส่วนการใช้งาน Copilot Studio ยังต้องเชื่อมต่ออินเทอร์เน็ต

ข้อความในกรอบเลือกคัดลอกได้ หากข้อความยาว ให้ใช้ไฟล์ UTF-8 ในโฟลเดอร์ `copy-text/` ของ ZIP ตามชื่อที่ระบุเหนือกรอบข้อความ

## สไลด์ประกอบการเรียน

<DownloadFile file="SCB-Power-Up-2-by-teerasej-v2.pdf">ดาวน์โหลดสไลด์ (PDF)</DownloadFile>

## Case และ Knowledge

| ไฟล์ | ใช้เมื่อใด |
|---|---|
| <DownloadFile file="case-notes-03.txt">Case notes 03 — CASE-201</DownloadFile> | case หลักของ Exercises 1–5 |
| <DownloadFile file="service-request-guide.txt">Service request guide</DownloadFile> | เพิ่มเป็น Knowledge ใน Exercise 2 |
| <DownloadFile file="document-preparation-guide.txt">Document preparation guide</DownloadFile> | เพิ่มเป็น Knowledge ใน Exercise 2 |
| <DownloadFile file="escalation-roles.txt">Escalation roles</DownloadFile> | เพิ่มเป็น Knowledge ใน Exercise 2 |
| <DownloadFile file="conflict-notice.txt">Conflict notice</DownloadFile> | ทดสอบ conflict แล้วนำออกก่อน Exercise 3 |

## Prompt และ Instructions checkpoints

| ไฟล์ | ใช้เมื่อใด |
|---|---|
| <DownloadFile file="format-service-brief-prompt.txt">Prompt template</DownloadFile> | Exercise 3: วางคำสั่งแล้วแทรก input chips CaseNotes และ BriefStyle |
| <DownloadFile file="agent-1-final-instructions.txt">Instructions หลัง Exercise 1</DownloadFile> | Instructions อย่างเดียว |
| <DownloadFile file="agent-2-instructions.txt">Instructions หลัง Exercise 2</DownloadFile> | รวมกติกา Knowledge |
| <DownloadFile file="agent-3-instructions.txt">Instructions หลัง Exercise 3–4</DownloadFile> | รวมการเรียก Prompt tool |
| <DownloadFile file="agent-5-instructions.txt">Instructions หลัง Exercise 5</DownloadFile> | รวมการใช้ Review Readiness Topic เพื่อให้คำแนะนำ |

ชื่อไฟล์ agent-1/2/3/5 หมายถึง checkpoint ของ **Agent ตัวเดียว** ไม่ใช่ Agent คนละตัว ใช้เทียบหรือกู้ส่วนที่ขาดหลังทดลองแล้ว ไม่อัปโหลด Instructions เป็น Knowledge และไฟล์เหล่านี้ไม่ได้สร้าง components ให้โดยอัตโนมัติ

## แบบบันทึกและเตรียม demo

| ไฟล์ | การใช้งาน |
|---|---|
| <DownloadFile file="test-log.xlsx">Use case test log XLSX</DownloadFile> | ตัวอย่างเสริมสำหรับบันทึก Scenario, Starter Prompts และผลของ use case ของทีม ไม่ต้องกรอกระหว่าง Exercise |
| <DownloadFile file="gap-list.csv">Gap list CSV</DownloadFile> | บันทึกสิ่งที่ต้องแก้ ผู้รับผิดชอบ และวิธี retest |
| <DownloadFile file="readiness-worksheet.md">Readiness worksheet Markdown</DownloadFile> | [อ่านบนเว็บไซต์](/resources/readiness-worksheet) |
| <DownloadFile file="demo-run-sheet.md">Demo run sheet Markdown</DownloadFile> | [อ่านบนเว็บไซต์](/resources/demo-run-sheet) |

หาก browser แสดงเนื้อหา TXT/CSV/Markdown ให้ใช้คำสั่ง Save หรือ Download ของ browser เพื่อเก็บไฟล์ โดยคงนามสกุลเดิม ไฟล์ XLSX ให้เปิดด้วย Excel หรือแอปที่รองรับรูปแบบนี้
