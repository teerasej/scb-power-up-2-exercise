// Vite treats # as a URL fragment. Stage only this site's files when its path contains #.
import { cp, mkdir, mkdtemp, rm, readdir, readFile, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import { tmpdir } from 'node:os'
import { dirname, join, relative } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = dirname(dirname(fileURLToPath(import.meta.url)))
const [mode, ...extra] = process.argv.slice(2)
if (!['dev', 'build'].includes(mode)) throw new Error('Use dev or build')
const staged = root.includes('#')
const work = staged ? await mkdtemp(join(tmpdir(), 'power-up-site-')) : root
let timer
let syncing = false
let previous = new Map()
async function syncDocs() {
  if (syncing) return
  syncing = true
  try {
    const current = new Map()
    async function walk(folder) {
      for (const entry of await readdir(folder, { withFileTypes: true })) {
        const path = join(folder, entry.name)
        const rel = relative(join(root, 'docs'), path)
        if (['.vitepress/dist', '.vitepress/cache'].some(p => rel === p || rel.startsWith(p + '/'))) continue
        if (entry.isDirectory()) await walk(path)
        else if (entry.isFile()) {
          const content = await readFile(path)
          current.set(rel, content)
          if (!previous.get(rel)?.equals(content)) {
            const dest = join(work, 'docs', rel)
            await mkdir(dirname(dest), { recursive: true })
            await writeFile(dest, content)
          }
        }
      }
    }
    await walk(join(root, 'docs'))
    for (const rel of previous.keys()) if (!current.has(rel)) await rm(join(work, 'docs', rel), { force: true })
    previous = current
  } finally { syncing = false }
}
try {
  if (staged) {
    console.log('Preparing a temporary build path for this workspace…')
    await cp(join(root, 'node_modules'), join(work, 'node_modules'), { recursive: true })
    await cp(join(root, 'package.json'), join(work, 'package.json'))
    await syncDocs()
    if (mode === 'dev') timer = setInterval(() => { syncDocs().catch(console.error) }, 800)
  }
  const args = [join(work, 'node_modules/vitepress/bin/vitepress.js'), mode, 'docs']
  if (mode !== 'build') args.push('--host', '127.0.0.1')
  args.push(...extra)
  const child = spawn(process.execPath, args, { cwd: work, stdio: 'inherit', env: process.env })
  const stop = signal => child.kill(signal)
  process.on('SIGINT', stop)
  process.on('SIGTERM', stop)
  const code = await new Promise((resolve, reject) => { child.on('error', reject); child.on('exit', code => resolve(code ?? 1)) })
  process.off('SIGINT', stop)
  process.off('SIGTERM', stop)
  if (staged && mode === 'build' && code === 0) {
    await rm(join(root, 'docs/.vitepress/dist'), { recursive: true, force: true })
    await cp(join(work, 'docs/.vitepress/dist'), join(root, 'docs/.vitepress/dist'), { recursive: true })
  }
  process.exitCode = Number(code)
} finally {
  clearInterval(timer)
  if (staged) await rm(work, { recursive: true, force: true })
}
