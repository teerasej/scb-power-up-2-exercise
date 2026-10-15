<script setup lang="ts">
import { ref, onMounted, watch, useId } from 'vue'
import { useData } from 'vitepress'
const props = defineProps<{ source: string }>()
const { isDark } = useData()
const diagram = ref('')
const failed = ref(false)
const id = `diagram-${useId().replace(/[^a-zA-Z0-9-]/g, '')}`
let revision = 0
async function render() {
  const current = ++revision
  try {
    const { default: mermaid } = await import('mermaid')
    await document.fonts.ready
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: isDark.value ? 'dark' : 'neutral', fontFamily: 'Noto Sans Thai, sans-serif', flowchart: { htmlLabels: false, useMaxWidth: false } })
    const { svg } = await mermaid.render(`${id}-${current}`, decodeURIComponent(props.source))
    if (current === revision) { diagram.value = svg; failed.value = false }
  } catch (error) {
    failed.value = true
    console.error('Diagram rendering failed', error)
  }
}
onMounted(render)
watch(isDark, render)
</script>

<template>
  <figure class="flow-diagram">
    <figcaption>เส้นทางการทำงาน · เลื่อนแนวนอนเพื่อดูครบทุกขั้น</figcaption>
    <div v-if="diagram && !failed" class="diagram-scroll" tabindex="0" role="img" aria-label="แผนภาพเส้นทางการทำงาน" v-html="diagram" />
    <p v-else-if="!failed" role="status">กำลังแสดงแผนภาพ…</p>
    <details :open="failed">
      <summary>{{ failed ? 'แสดงแผนภาพไม่ได้ — อ่านลำดับการทำงาน' : 'ดูลำดับการทำงานแบบข้อความ' }}</summary>
      <pre>{{ decodeURIComponent(source) }}</pre>
    </details>
  </figure>
</template>
