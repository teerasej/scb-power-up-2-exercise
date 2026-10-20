import { h } from 'vue'
import CourseHero from './components/CourseHero.vue'
import PracticeIllustration from './components/PracticeIllustration.vue'
import ExerciseCover from './components/ExerciseCover.vue'
import DownloadFile from './components/DownloadFile.vue'
import DefaultTheme from 'vitepress/theme'
import MermaidDiagram from './components/MermaidDiagram.vue'
import '@fontsource/noto-sans-thai/400.css'
import '@fontsource/noto-sans-thai/600.css'
import '@fontsource/noto-sans-thai/700.css'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'home-hero-before': () => h(CourseHero) }),
  enhanceApp({ app }) {
    app.component('MermaidDiagram', MermaidDiagram)
    app.component('DownloadFile', DownloadFile)
    app.component('ExerciseCover', ExerciseCover)
    app.component('PracticeIllustration', PracticeIllustration)
  },
}
