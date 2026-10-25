# Offline learner guide

`export-offline-guide.py` reads committed learner Markdown at the requested Git revision, resolves local illustrations, exports A4 with internal contents/bookmarks/return links, and produces exact UTF-8 copies of fenced code blocks. It deliberately does not include uncommitted exercise edits. Export only a reviewed learner revision.

Local dependencies: Python 3.12+, WeasyPrint 70.0 (with Pango), markdown-it-py 4.2.0, fonttools 4.67.0, pypdf 6.21.2. For verification use PyMuPDF and Pillow. Use a virtual environment; do not modify system Python. Required fonts: Noto Sans Thai variable font and Avenir Next Regular / Demi Bold. Font paths are configurable with `--thai-font` and `--english-font`; missing styles fail explicitly. Font binaries are not distributed in this repository.

```sh
python scripts/export-offline-guide.py --source-revision <reviewed-commit> --work-dir /tmp/scb-offline-guide
python scripts/verify-offline-guide.py --work-dir /tmp/scb-offline-guide
python scripts/package-samples.py
npm run docs:build
```

On macOS with Homebrew Pango, set `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` if required. `XDG_CACHE_HOME` can point to a writable temporary cache. The exporter writes the PDF and `copy-text/` under `docs/public/downloads/`; temporary HTML/fonts and validation evidence stay in `--work-dir`. The code includes a narrow Thai nikhahit ToUnicode repair because Pango's sara-am decomposition can otherwise lose this mark during PDF copying. It does not change rendered text.

Review all rendered pages before release, especially Thai diacritics, code blocks and page breaks. The verifier checks the Unicode-normalized extracted code text, exact TXT hashes, headings, A4, bookmarks and page links. It does not replace visual review or tenant rehearsal. PDF viewers may add wrapping/newlines or decompose Thai characters when copying; the TXT files preserve exact source bytes.

The committed PDF is the release artifact. CI packages it without requiring licensed local fonts or the PDF export dependencies. When learner content changes, regenerate/review the PDF before releasing a refreshed offline edition. Preserve all existing learner ZIP entries and compare them byte-for-byte before publication.
