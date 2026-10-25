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
    - theme: alt
      text: ดาวน์โหลดสไลด์ (PDF)
      link: /downloads/SCB-Power-Up-2-by-teerasej-v2.pdf
      download: SCB-Power-Up-2-by-teerasej-v2.pdf
features:
  - title: เริ่มจากงานที่ชัดเจน
    details: ใช้ CASE-201 ซึ่งเป็นคำขอเอกสารสมมติ แล้วกำหนดขอบเขตและคู่มือให้ผู้ช่วย
  - title: ต่อเครื่องมือเข้าด้วยกัน
    details: ฝึก Prompt และ entity ทดสอบ flow แล้วรู้จัก Topic แบบหนึ่งคำถามสองตัวเลือก
  - title: ตรวจผลก่อนนำเสนอ
    details: สังเกตผลจากการทดสอบ แยกสิ่งที่ทำได้จากสิ่งที่ยังต้องแก้
---

## เส้นทางการเรียนรู้

การทำงานกับ Agent ก็เหมือนทำงานกับคู่หูที่โต๊ะเดียวกัน: **Instructions** คือแนวทางทำงาน, **Knowledge** คือแฟ้มคู่มือ, **Prompt** คือคำสั่งหรือแบบจัดสรุป, **flow** คือขั้นตอนการทำงานแบบเจาะจงชัดเจน และ **Topic** คือการควบคุมรูปแบบการถามตอบและเก็บข้อมูลครับ

| Exercise | สิ่งที่จะสร้าง | สิ่งที่นำไปใช้ต่อ |
|---|---|---|
| [1 · Instructions](/exercises/01-instructions) | Service Request Assistant | Agent และ Instructions |
| [2 · Knowledge](/exercises/02-knowledge) | เพิ่มคู่มือให้ Agent ตัวเดิม | คำตอบของที่ตรวจสอบความถูกต้องได้ |
| [3 · Prompt tool](/exercises/03-prompt-tool) | Format Service Brief และ BriefStyle entity | โครงสร้างของ Service Brief ที่ตรวจสอบความถูกต้องได้ |
| [4 · Agent flow](/exercises/04-agent-flow) | Send Reviewed Training Brief | flow ที่รับ input สองตัวและใช้งานได้ |
| [5 · Topics](/exercises/05-topics) | Review Readiness | คำแนะนำสองเส้นทางตามคำตอบ |

ในที่นี้พลจะให้เราใช้ Agent ตัวเดิมตลอดทั้ง 5 Exercise ครับ

## ตรวจเช็คว่าพร้อมหรือไม่

ใช้ [Readiness worksheet](/resources/readiness-worksheet), <DownloadFile file="gap-list.csv">Gap list</DownloadFile> และ [Demo run sheet](/resources/demo-run-sheet) ทบทวนผลจริงและเตรียมนำเสนอ ข้อมูลฝึกทั้งหมดเป็นข้อมูลสมมติ ไม่ใช่นโยบายหรือข้อมูลลูกค้าจริง

การเปิดเว็บไซต์ได้ยังไม่ยืนยันว่า Environment พร้อมฝึก ตรวจ [สิ่งที่ต้องเตรียม](/prerequisites) กับผู้สอนก่อนเริ่ม
