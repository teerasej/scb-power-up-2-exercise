import { defineConfig } from 'vitepress'

const exercises = [
  ['01-instructions', '1 · Instructions'],
  ['02-knowledge', '2 · Knowledge'],
  ['03-prompt-tool', '3 · Prompt tool'],
  ['04-agent-flow', '4 · Agent flow'],
  ['05-topics', '5 · Topics introduction'],
]

export default defineConfig({
  title: 'Power Up #2',
  titleTemplate: ':title · Copilot Studio',
  description: 'สร้าง Service Request Assistant ด้วย Copilot Studio ผ่านห้า Exercise ที่เชื่อมต่อกัน',
  lang: 'th-TH',
  base: process.env.SITE_BASE || '/',
  cleanUrls: false,
  lastUpdated: false,
  srcExclude: ['public/**'],
  themeConfig: {
    siteTitle: 'Power Up #2',
    nav: [
      { text: 'ภาพรวม', link: '/' },
      { text: 'ก่อนเริ่ม', link: '/prerequisites' },
      { text: 'ไฟล์ฝึก', link: '/resources/downloads' },
    ],
    sidebar: [
      { text: 'เริ่มต้น', items: [{ text: 'ภาพรวม', link: '/' }, { text: 'ก่อนเริ่ม', link: '/prerequisites' }] },
      { text: 'สร้าง Agent ทีละขั้น', items: exercises.map(([slug, text]) => ({ text, link: `/exercises/${slug}` })) },
      { text: 'ไฟล์และหลักฐาน', items: [
        { text: 'ดาวน์โหลดไฟล์ฝึก', link: '/resources/downloads' },
        { text: 'Readiness worksheet', link: '/resources/readiness-worksheet' },
        { text: 'Demo run sheet', link: '/resources/demo-run-sheet' },
      ] },
    ],
    outline: { level: [2, 3], label: 'ในหน้านี้' },
    docFooter: { prev: 'ก่อนหน้า', next: 'ถัดไป' },
    sidebarMenuLabel: 'สารบัญ',
    returnToTopLabel: 'กลับด้านบน',
    darkModeSwitchLabel: 'รูปแบบสี',
    search: { provider: 'local', options: { locales: { root: { translations: {
      button: { buttonText: 'ค้นหา', buttonAriaLabel: 'ค้นหาในคู่มือ' },
      modal: { noResultsText: 'ไม่พบผลลัพธ์', resetButtonTitle: 'ล้างคำค้น', footer: { selectText: 'เลือก', navigateText: 'เลื่อน', closeText: 'ปิด' } },
    } } } } },
    footer: { message: 'ข้อมูลสมมติสำหรับการฝึก · ใช้ผลทดสอบจริงเป็นหลักฐาน', copyright: 'Power Up #2 · Build, Test and Strengthen' },
  },
  markdown: {
    config(md) {
      const original = md.renderer.rules.fence!
      md.renderer.rules.fence = (tokens, idx, options, env, self) => {
        if (tokens[idx].info.trim() === 'mermaid') {
          return `<MermaidDiagram source="${encodeURIComponent(tokens[idx].content)}" />\n`
        }
        return original(tokens, idx, options, env, self)
      }
    },
  },
})
