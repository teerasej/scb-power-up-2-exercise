---
title: ก่อนเริ่ม
prev: { text: ภาพรวม, link: / }
next: { text: "Exercise 1: Instructions", link: /exercises/01-instructions }
---

# ก่อนเริ่ม

เราจะสร้าง **Service Request Assistant ตัวเดียว** ด้วย Copilot Studio standard harness และใช้ **CASE-201** ต่อเนื่องทั้งห้า Exercise

## บัญชีและ Environment

- ใช้บัญชีและ Environment ฝึกที่ผู้สอนกำหนด มีสิทธิ์สร้างและแก้ไข Agent
- ให้ผู้สอนยืนยันสิทธิ์และ availability ของ Copilot Studio, Generative AI, file Knowledge, Prompt tool, Agent flow และ Topics รวมถึง capacity ที่ใช้ฝึก
- ก่อน Exercise 4 ต้องมี Office 365 Outlook connection, Exchange mailbox และ approved test inbox ที่ผู้สอนอนุญาต การทดสอบ flow อาจส่ง email จริง
- Native Agent flow ไม่ได้ต้องมี Power Automate license แยกเพียงเพราะใช้ flow แต่สิทธิ์และ capacity ที่เกี่ยวข้องยังต้องพร้อม

## ไฟล์และสิ่งที่ต้องรับจากผู้สอน

1. ดาวน์โหลด <DownloadFile file="case-notes-03.txt">Case notes 03 — CASE-201</DownloadFile> และเปิด [หน้าไฟล์ฝึก](/resources/downloads)
2. เก็บ <DownloadFile file="test-log.csv">Test log</DownloadFile> และ <DownloadFile file="gap-list.csv">Gap list</DownloadFile> ไว้กรอกผลของตนเอง
3. ก่อน Exercise 5 ตรวจว่าเปิด `Topics` และสร้าง Topic ใหม่ใน Agent ตัวเดิมได้
4. เก็บ approved test inbox ใน Environment ฝึกและโน้ตส่วนตัว ไม่เติมลงในไฟล์ที่จะแชร์

::: info Topic introduction
Exercise 5 สร้าง Topic เล็ก ๆ จากหน้าเปล่า ไม่ต้อง import starter หรือเชื่อม flow ใช้ standard harness; GitHub Copilot harness มีวิธี authoring ต่างออกไปซึ่งผู้สอนจะเปรียบเทียบให้ดู
:::

## วิธีทำกิจกรรม

- ทำตามลำดับ Instructions → Knowledge → Prompt tool → Agent flow → Topics
- ใช้ข้อมูลสมมติเท่านั้น ไม่ใส่ข้อมูลลูกค้า เลขบัญชี หรือ credentials จริง
- Hands-on ใช้ standard harness; GitHub Copilot harness เป็น instructor demo
- ถ้า component ไม่พร้อม ให้บันทึก `Blocked` หรือ `Not run` แล้วใช้ checkpoint ที่ผู้สอนเตรียม การดูตัวอย่างไม่ใช่หลักฐานว่า Agent ของตนผ่านแล้ว

[เริ่ม Exercise 1](/exercises/01-instructions)

## เอกสารผลิตภัณฑ์

- [เพิ่ม tools ให้ Agent — Microsoft Learn](https://learn.microsoft.com/microsoft-copilot-studio/add-tools-custom-agent)
- [Agent flows — Microsoft Learn](https://learn.microsoft.com/microsoft-copilot-studio/flows-faqs)
- [เรียก flow จาก Agent — Microsoft Learn](https://learn.microsoft.com/microsoft-copilot-studio/flow-agent)
