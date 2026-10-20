<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import illustrations from './practice-illustrations.json'

type Artwork = {
  alt: string
  width: number
  height: number
  variants: { src: string; width: number }[]
}

const props = defineProps<{ id: string }>()
const artwork = computed(() => (illustrations as Record<string, Artwork>)[props.id])
</script>

<template>
  <figure v-if="artwork" class="practice-illustration" :data-practice="id">
    <img
      :src="withBase(artwork.variants[artwork.variants.length - 1].src)"
      :srcset="artwork.variants.map(image => `${withBase(image.src)} ${image.width}w`).join(', ')"
      sizes="(max-width: 767px) calc(100vw - 48px), 688px"
      :width="artwork.width"
      :height="artwork.height"
      :alt="artwork.alt"
      loading="lazy"
      decoding="async"
    >
  </figure>
</template>

<style scoped>
.practice-illustration {
  margin: 1.25rem 0;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
}

.practice-illustration img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: contain;
}
</style>
