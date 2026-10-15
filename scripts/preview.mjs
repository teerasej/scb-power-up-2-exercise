import { preview } from 'vite'
import { dirname } from 'node:path'
import { fileURLToPath } from 'node:url'
const root = dirname(dirname(fileURLToPath(import.meta.url)))
const args = process.argv.slice(2)
const portIndex = args.indexOf('--port')
const port = portIndex < 0 ? 4173 : Number(args[portIndex + 1])
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('Invalid preview port')
const server = await preview({
  configFile: false,
  root,
  base: process.env.SITE_BASE || '/',
  appType: 'mpa',
  build: { outDir: 'docs/.vitepress/dist' },
  preview: { host: '127.0.0.1', port, strictPort: true },
})
server.printUrls()
for (const signal of ['SIGINT', 'SIGTERM']) process.on(signal, () => server.httpServer.close(() => process.exit(0)))
