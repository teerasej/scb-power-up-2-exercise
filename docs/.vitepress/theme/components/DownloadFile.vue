<script setup lang="ts">
import { withBase } from 'vitepress'
defineProps<{ file: string }>()
</script>

<template>
  <a :href="withBase(`/downloads/${file}`)" download><slot /></a>
</template>
