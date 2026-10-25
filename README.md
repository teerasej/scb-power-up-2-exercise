# Power Up #2 learner website

Thai-first learner instructions for one Service Request Assistant across five connected exercises. This directory contains the learner website source and its GitHub Pages deployment workflow.

## Maintain the site

`docs/` is the canonical website content. Edit exercise pages in `docs/exercises/`, resources in `docs/resources/`, and actual downloadable files in `docs/public/downloads/`. When changing a rendered worksheet, update its downloadable Markdown copy too. Keep the explicit core previous/next links in order. The optional Test log guide at `/resources/test-log` teaches one example from the unchanged XLSX template.

Use Node.js 22.12 or newer (prefer a supported LTS release), npm, and Python 3 (standard-library ZIP packaging):

```sh
npm ci
npm run docs:dev
npm run docs:build
npm run docs:preview
```

The local base is `/`. GitHub Pages builds use `SITE_BASE=/scb-power-up-2-exercise/` for the project URL. The workflow publishes pushes to `main` and also supports manual dispatch. Keep build output and dependencies ignored.

Website: https://teerasej.github.io/scb-power-up-2-exercise/

Repository: https://github.com/teerasej/scb-power-up-2-exercise

## Content boundaries

The site carries the approved five-exercise learner guide and 13 downloads, including synthetic practice files, optional planning templates and the approved presentation PDF. The original teaching pack remains a separate source snapshot. Future website edits belong here; there is no automatic two-way synchronization.

Do not place instructor notes, credentials, tenant addresses, private source references, participant records, old archives or editable presentations anywhere in this directory. Only the approved presentation PDF is included. Repository contents outside navigation can become public too. No organization logo or repository/edit buttons are used.

Learner access, capacity, Outlook connections for Exercise 4, and live exercise rehearsal still require instructor preparation. Exercise 5 creates Review Readiness from blank without a starter, flow call or email. The website does not contain an importable solution. Site verification is not tenant or classroom readiness.

## Toolchain notes

VitePress 1.6.4 is the stable release. The Vite override to 6.4.4 addresses current Vite/esbuild advisories in its default dependency tree; the Vue plugin supports Vite 6. Keep this override under review when upgrading VitePress.

The command wrapper uses a temporary copy if the workspace path contains `#`, which Vite treats as a URL fragment. Successful builds copy generated output back to `docs/.vitepress/dist/`; development mode mirrors source edits into the temporary copy. Preview uses Vite to serve the production build on 127.0.0.1 only. The wrapper removes its temporary directory when it exits normally.

## Local verification

The site contains 10 content pages plus a generated 404 page and 13 downloadable learner files. Release checks include the production build, page/asset links, desktop/mobile layouts, Thai text, search, code copying, downloads and the Exercise 4 flow diagram. The publication workflow and current deployment status are available in GitHub Actions.

## SCB visual theme

The interface uses minimal purple and gold accents with neutral reading surfaces. Six related 2D illustrations have distinct palettes: home, lilac Instructions, mauve Knowledge, indigo Prompt tool, gold Agent flow and plum Topics. Current headings and exercise content are preserved.

Optimized responsive artwork is in `docs/public/images/`. The custom home hero reads the `courseHero` frontmatter text; exercise banners use `ExerciseCover`. Keep the image dimensions, Thai alternative text and responsive source sets when replacing an image. Original generation assets and prompts are kept separately from the public website source.

## Combined sample download

The hero’s second button directly downloads `docs/public/downloads/power-up-2-sample-files.zip`; its third button downloads `SCB-Power-Up-2-by-teerasej-v2.pdf`. The ZIP contains all 13 current files, including the presentation PDF, with the same bytes as the individual downloads. `npm run docs:build` regenerates and verifies this ZIP before building; use `npm run samples:zip` to refresh it independently. The explicit file list in `scripts/package-samples.py` excludes old archives, standalone illustrations, editable presentations and instructor material.

## Practice illustrations

All 19 Practice headings across the five exercises have distinct generated illustrations. `PracticeIllustration` uses a public asset mapping for Thai alternative text, actual dimensions and base-aware responsive WebP URLs. Images preserve the complete scene proportionally. Keep original generation files and provenance outside this repository. The sample ZIP excludes standalone artwork; the approved presentation PDF retains its embedded slide artwork.
