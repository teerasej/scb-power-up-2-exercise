<script setup lang="ts">
import { useData, withBase } from 'vitepress'
import { VPButton } from 'vitepress/theme'
const { frontmatter } = useData()
</script>

<template>
  <section class="course-hero" aria-labelledby="course-heading">
    <img
      class="course-hero-art"
      :src="withBase('/images/home.webp')"
      :srcset="`${withBase('/images/home-768.webp')} 768w, ${withBase('/images/home-1440.webp')} 1440w, ${withBase('/images/home.webp')} 1672w`"
      sizes="(max-width: 767px) 100vw, (max-width: 1279px) calc(100vw - 64px), 1216px"
      width="1672" height="941"
      alt="ทีมบริการร่วมสร้างผู้ช่วยที่โต๊ะเดียวกัน ตั้งแต่จัดโน้ตและค้นคู่มือจนถึงเตรียมสรุปส่งต่อ"
      fetchpriority="high" decoding="async"
    >
    <div class="course-hero-copy">
      <p class="course-hero-name">{{ frontmatter.courseHero.name }}</p>
      <h1 id="course-heading" v-html="frontmatter.courseHero.text" />
      <p class="course-hero-tagline">{{ frontmatter.courseHero.tagline }}</p>
      <div class="course-hero-actions">
        <VPButton v-for="action in frontmatter.courseHero.actions" :key="action.link"
          :theme="action.theme" :href="action.download ? withBase(action.link) : action.link" :text="action.text" :download="action.download || undefined" />
      </div>
    </div>
  </section>
</template>
