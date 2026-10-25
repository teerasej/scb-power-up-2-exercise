"""Package only the approved learner files; keep the website ZIP reproducible."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

DOWNLOADS = Path(__file__).resolve().parents[1] / 'docs/public/downloads'
FILES = (
    'case-notes-03.txt',
    'service-request-guide.txt',
    'document-preparation-guide.txt',
    'escalation-roles.txt',
    'conflict-notice.txt',
    'format-service-brief-prompt.txt',
    'agent-1-final-instructions.txt',
    'agent-2-instructions.txt',
    'agent-3-instructions.txt',
    'agent-5-instructions.txt',
    'test-log.xlsx',
    'demo-run-sheet.md',
    'SCB-Power-Up-2-by-teerasej-v2.pdf',
    'SCB-Power-Up-2-Offline-Exercise-Guide.pdf',
)
copy_files = tuple('copy-text/' + p.name for p in sorted((DOWNLOADS / 'copy-text').glob('*')) if p.is_file())
if not copy_files or 'copy-text/index.json' not in copy_files:
    raise SystemExit('Generate offline guide and copy-text files before packaging')
FILES += copy_files
archive = DOWNLOADS / 'power-up-2-sample-files.zip'
for name in FILES:
    path = DOWNLOADS / name
    if not path.is_file() or path.is_symlink():
        raise SystemExit(f'Missing or unsafe learner file: {name}')
with ZipFile(archive, 'w', compression=ZIP_DEFLATED, compresslevel=9) as output:
    for name in FILES:
        info = ZipInfo(name, date_time=(2026, 10, 15, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        output.writestr(info, (DOWNLOADS / name).read_bytes(), compresslevel=9)
with ZipFile(archive) as packaged:
    assert packaged.namelist() == list(FILES)
    assert packaged.testzip() is None
    for name in FILES:
        assert packaged.read(name) == (DOWNLOADS / name).read_bytes(), name
print(f'Packaged and verified {len(FILES)} learner files: {archive.name}')
