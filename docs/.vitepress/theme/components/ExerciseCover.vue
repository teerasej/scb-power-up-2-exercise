<script setup lang="ts">
import { withBase } from 'vitepress'
const props = defineProps<{ image: string; alt: string; position?: string }>()
</script>

<template>
  <div class="exercise-cover">
    <img :src="withBase(`/images/${image}.webp`)"
      :srcset="`${withBase(`/images/${image}-768.webp`)} 768w, ${withBase(`/images/${image}-1440.webp`)} 1440w, ${withBase(`/images/${image}.webp`)} 2172w`"
      sizes="(max-width: 767px) calc(100vw - 48px), 688px"
      width="2172" height="724" :alt="alt"
      :style="{ objectPosition: props.position || 'center' }"
      loading="lazy" decoding="async">
  </div>
</template>
