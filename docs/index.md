---
layout: home
title: Build, Test and Strengthen
courseHero:
  name: "Power Up #2"
  text: สร้างผู้ช่วยงานอัตโนมัติ ด้วยพลัง Generative AI
  tagline: ใช้ Copilot Studio สร้าง Service Request Assistant ตัวเดียว ตั้งแต่จัดโน้ต ค้นคู่มือ จนถึงส่งสรุปหลังตรวจทาน
  actions:
    - theme: brand
      text: เตรียมตัวก่อนเริ่ม
      link: /prerequisites
    - theme: alt
      text: ดาวน์โหลดไฟล์ฝึก (ZIP)
      link: /downloads/power-up-2-sample-files.zip
      download: power-up-2-sample-files.zip
features:
  - title: เริ่มจากงานที่ชัดเจน
    details: ใช้ CASE-201 ซึ่งเป็นคำขอเอกสารสมมติ แล้วกำหนดขอบเขตและคู่มือให้ผู้ช่วย
  - title: ต่อเครื่องมือเข้าด้วยกัน
    details: ฝึก Prompt และ entity ทดสอบ flow แล้วรู้จัก Topic แบบหนึ่งคำถามสองตัวเลือก
  - title: ตรวจผลก่อนนำเสนอ
    details: เก็บหลักฐานจากการทดสอบ แยกสิ่งที่ทำได้จากสิ่งที่ยังต้องแก้
---

## เส้นทางการเรียนรู้

การทำงานกับ Agent ก็เหมือนทำงานกับคู่หูที่โต๊ะเดียวกัน: **Instructions** คือแนวทางทำงาน, **Knowledge** คือแฟ้มคู่มือ, **Prompt** คือแบบจัดสรุป, **flow** คือขั้นตอนการทำงาน และ **Topic** คือรูปแบบการถามและเก็บข้อมูล แล้วให้คำแนะนำตามคำตอบครับ

| Exercise | สิ่งที่จะสร้าง | สิ่งที่นำไปใช้ต่อ |
|---|---|---|
| [1 · Instructions](/exercises/01-instructions) | Service Request Assistant | Agent และ Instructions |
| [2 · Knowledge](/exercises/02-knowledge) | เพิ่มคู่มือให้ Agent ตัวเดิม | คำตอบที่ตรวจสอบได้ |
| [3 · Prompt tool](/exercises/03-prompt-tool) | Format Service Brief และ BriefStyle entity | body ที่ review แล้ว |
| [4 · Agent flow](/exercises/04-agent-flow) | Send Reviewed Training Brief | flow ที่รับ input สองตัว |
| [5 · Topics](/exercises/05-topics) | Review Readiness | คำแนะนำสองเส้นทางตามคำตอบ โดยไม่มีการส่ง email |

ใช้ Agent ตัวเดิมตลอดทั้ง 5 Exercise และเก็บชื่อ components ไว้สำหรับขั้นถัดไป

## ตรวจเช็คว่าพร้อมหรือไม่

ใช้ <DownloadFile file="test-log.csv">Test log</DownloadFile>, [Readiness worksheet](/resources/readiness-worksheet), <DownloadFile file="gap-list.csv">Gap list</DownloadFile> และ [Demo run sheet](/resources/demo-run-sheet) บันทึกผลจริง ข้อมูลฝึกทั้งหมดเป็นข้อมูลสมมติ ไม่ใช่นโยบายหรือข้อมูลลูกค้าจริง

การเปิดเว็บไซต์ได้ยังไม่ยืนยันว่า Environment พร้อมฝึก ตรวจ [สิ่งที่ต้องเตรียม](/prerequisites) กับผู้สอนก่อนเริ่ม
