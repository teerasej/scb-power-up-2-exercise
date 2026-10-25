"""Export the learner website to A4. See offline-guide.md for local dependencies."""
from pathlib import Path
import argparse, datetime, hashlib, html, json, os, posixpath, re, subprocess
from zoneinfo import ZoneInfo
from markdown_it import MarkdownIt
from fontTools.ttLib import TTFont, TTCollection
from fontTools.varLib.instancer import instantiateVariableFont
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
PUBLIC = DOCS / 'public'
DOWNLOADS = PUBLIC / 'downloads'
parser = argparse.ArgumentParser()
parser.add_argument('--source-revision', default='HEAD')
parser.add_argument('--work-dir', type=Path, default=Path('/private/tmp/scb-offline-guide'))
parser.add_argument('--thai-font', type=Path, default=Path.home() / 'Library/Fonts/NotoSansThai[wdth,wght].ttf')
parser.add_argument('--english-font', type=Path, default=Path('/System/Library/Fonts/Avenir Next.ttc'))
args = parser.parse_args()
work = args.work_dir
work.mkdir(parents=True, exist_ok=True)
revision = subprocess.check_output(['git', 'rev-parse', args.source_revision], cwd=ROOT, text=True).strip()
date = datetime.datetime.now(ZoneInfo('Asia/Bangkok')).strftime('%d %B %Y')
for p in (args.thai_font, args.english_font):
    if not p.is_file(): raise SystemExit(f'Required font unavailable: {p}')
for weight, name in [(400, 'ThaiRegular'), (600, 'ThaiHeading')]:
    font = instantiateVariableFont(TTFont(args.thai_font), {'wght': weight, 'wdth': 100})
    font.save(work / f'{name}.ttf')
found = set()
for font in TTCollection(args.english_font).fonts:
    names = {n.toUnicode() for n in font['name'].names if n.nameID == 6}
    for postscript, name in [('AvenirNext-Regular', 'EnglishRegular'), ('AvenirNext-DemiBold', 'EnglishHeading')]:
        if postscript in names:
            font.save(work / f'{name}.ttf'); found.add(name)
assert found == {'EnglishRegular', 'EnglishHeading'}, 'Avenir Next required styles unavailable'

routes = ['prerequisites'] + [f'exercises/{p.stem}' for p in sorted((DOCS / 'exercises').glob('*.md'))] + ['resources/readiness-worksheet', 'resources/demo-run-sheet', 'resources/downloads']
art = json.loads((DOCS / '.vitepress/theme/components/practice-illustrations.json').read_text())
md = MarkdownIt('commonmark', {'html': True, 'breaks': False}).enable('table')
copy_dir = DOWNLOADS / 'copy-text'
copy_dir.mkdir(exist_ok=True)
# Only generated files listed in the prior manifest belong to this exporter.
manifest_path = copy_dir / 'index.json'
if manifest_path.exists():
    for entry in json.loads(manifest_path.read_text())['blocks']:
        (copy_dir / entry['file']).unlink(missing_ok=True)
blocks, toc, rendered, headings = [], [], [], {}
source_hashes = {}

def picture(src, alt):
    p = PUBLIC / src.lstrip('/')
    assert p.is_file(), p
    return f'<figure><img src="{p.as_uri()}" alt="{html.escape(alt)}"></figure>'

def source(route):
    raw = subprocess.check_output(['git', 'show', f'{revision}:docs/{route}.md'], cwd=ROOT, text=True)
    source_hashes[route] = hashlib.sha256(raw.encode()).hexdigest()
    return re.sub(r'^---\n.*?\n---\n', '', raw, count=1, flags=re.S)

for route_index, route in enumerate(routes):
    raw = source(route)
    if route == 'resources/downloads':
        raw = raw.replace('ZIP รวมไฟล์ฝึก แบบบันทึก และสไลด์ PDF ทั้ง 15 ไฟล์ที่แสดงด้านล่าง', 'ZIP รวมไฟล์ฝึก แบบบันทึก และสไลด์ PDF เดิมทั้ง 15 ไฟล์ พร้อมคู่มือ Offline Exercise Guide และโฟลเดอร์ copy-text/')
    raw = re.sub(r'<ExerciseCover\s+image="([^"]+)"\s+alt="([^"]+)"[^>]*/>', lambda m: picture('/images/' + m[1] + '-1440.webp', m[2]), raw)
    raw = re.sub(r'<PracticeIllustration\s+id="([^"]+)"\s*/>', lambda m: picture(art[m[1]]['variants'][-1]['src'], art[m[1]]['alt']), raw)
    raw = re.sub(r'<DownloadFile file="([^"]+)">(.*?)</DownloadFile>', lambda m: f'{m[2]} <span class="filename">(ไฟล์ใน ZIP: {html.escape(m[1])})</span>', raw)
    tokens = md.parse(raw)
    page_id = f'section-{route_index}'
    practice, number = 'intro', 0
    current_heading = ''
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            title = tokens[i+1].content
            current_heading = title
            anchor = f'{page_id}-h{i}'
            if token.tag == 'h1': anchor = page_id
            token.attrSet('id', anchor)
            headings[(route, title)] = anchor
            if token.tag == 'h1' or title.startswith('Practice '):
                toc.append((int(token.tag[1]), title, anchor))
                if title.startswith('Practice '):
                    practice = 'practice-' + re.search(r'Practice (\d+)', title)[1]
                    number = 0
        if token.type == 'fence':
            number += 1
            filename = f'{route.split("/")[-1]}-{practice}-{number:02d}.txt'
            (copy_dir / filename).write_text(token.content, encoding='utf-8')
            blocks.append({'file': filename, 'route': route, 'practice': practice, 'heading': current_heading, 'sha256': hashlib.sha256(token.content.encode()).hexdigest(), 'text': token.content})
            token.type = 'html_block'
            token.content = f'<div class="codeblock"><div class="copy-label">ข้อความสำหรับคัดลอก · copy-text/{filename}</div><pre>{html.escape(token.content)}</pre></div>\n'
        if token.children:
            for child in token.children:
                if child.type == 'link_open':
                    href = child.attrGet('href') or ''
                    if not re.match(r'^(https?:|mailto:|#)', href):
                        target, _, fragment = href.partition('#')
                        target = posixpath.normpath(target.lstrip('/') if target.startswith('/') else posixpath.join(posixpath.dirname(route), target))
                        target = re.sub(r'\.(md|html)$', '', target)
                        if target in ('', '.', '/'): child.attrSet('href', '#contents')
                        elif target in routes: child.attrSet('href', '#section-' + str(routes.index(target)))
                        else: child.attrSet('href', 'https://teerasej.github.io/scb-power-up-2-exercise/' + target)
    rendered.append('<section>' + md.renderer.render(tokens, md.options, {}) + '</section>')

assert len([x for x in toc if x[1].startswith('Practice ')]) == 25
assert len([r for r in routes if r.startswith('exercises/')]) == 5
assert len({b['file'] for b in blocks}) == len(blocks)
public_manifest = {'source_revision': revision, 'blocks': [{k:v for k,v in b.items() if k != 'text'} for b in blocks]}
manifest_path.write_text(json.dumps(public_manifest, ensure_ascii=False, indent=2) + '\n')
(copy_dir / 'README.txt').write_text('ข้อความสำหรับคัดลอกจากคู่มือ Offline Exercise Guide\nเปิดไฟล์ .txt ที่ระบุข้าง code block แล้วคัดลอกข้อความทั้งหมด\nชื่อไฟล์เรียงตาม Exercise, Practice และลำดับ code block\nไฟล์เป็น UTF-8 และเก็บข้อความจากเว็บไซต์โดยไม่เปลี่ยนเนื้อหา\n', encoding='utf-8')
css = (ROOT / 'scripts/offline-guide.css').read_text().replace('FONT_ROOT', work.as_uri())
footer = '''<footer><div><a href="#contents">กลับสารบัญ</a> · SCB Power Up #2</div><div>© 2026 Teerasej Jiraphatchandej. All rights reserved.</div><div><a href="mailto:teerasej@nextflow.in.th">Email me</a> · <a href="https://www.facebook.com/teerasej">Facebook</a> · <a href="https://www.youtube.com/teerasej">YouTube</a></div></footer>'''
cover = f'''<section class="cover"><p class="eyebrow">POWER UP #2 · OFFLINE LEARNER GUIDE</p><h1>Build, Test<br>and Strengthen</h1><h2>คู่มือฝึกปฏิบัติฉบับออฟไลน์</h2><p>Service Request Assistant</p><p>5 Exercises · 21 Practices<br>พร้อม Readiness 4 Practices และ Demo run sheet</p><div class="cover-note">เปิดอ่านและคัดลอกข้อความได้ แม้เข้าเว็บไซต์แบบฝึกหัดไม่ได้</div><p class="edition">Website source: {revision[:12]}<br>Export: {date} · Asia/Bangkok</p></section>'''
intro = '''<section><h1 id="how-to">วิธีใช้คู่มือ</h1><ol><li>แตกไฟล์ power-up-2-sample-files.zip ก่อนเริ่ม และเก็บไฟล์ทั้งหมดไว้ในโฟลเดอร์เดียวกัน</li><li>เลือก Exercise หรือ Practice จากสารบัญ หรือใช้ Bookmarks ของโปรแกรมอ่าน PDF</li><li>กด “กลับสารบัญ” ที่ด้านล่างของหน้าเพื่อกลับมาเลือกหัวข้อ</li><li>เลือกข้อความในกรอบเพื่อคัดลอก หากข้อความยาวหรือการคัดลอกขึ้นบรรทัดไม่ตรง ให้เปิดไฟล์ UTF-8 ใน copy-text/ ตามชื่อที่ระบุเหนือกรอบ แล้วคัดลอกจากไฟล์นั้น</li><li>ไฟล์ประกอบอ้างอิงด้วยชื่อไฟล์ใน ZIP จึงเปิดใช้งานได้โดยไม่ต้องดาวน์โหลดซ้ำ</li></ol><p>คู่มือนี้ช่วยอ่านคำสั่งแบบออฟไลน์ ส่วนการสร้างและทดสอบ Agent ยังต้องเชื่อมต่อ Copilot Studio และบริการที่เกี่ยวข้อง</p><p>ใช้ข้อมูลสมมติและ approved test inbox เท่านั้น ผลการทดสอบจริงขึ้นอยู่กับ Environment และสิทธิ์ที่ได้รับ</p></section>'''
contents = '<section class="contents"><h1 id="contents">สารบัญ</h1><p>คลิกชื่อหัวข้อเพื่อเปิดหน้าที่ต้องการ</p><a class="toc-item" href="#how-to">วิธีใช้คู่มือ</a>' + ''.join(f'<a class="toc-item {"sub" if level > 1 else "major"}" href="#{anchor}">{html.escape(title)}</a>' for level,title,anchor in toc) + '</section>'
html_doc = '<!doctype html><html lang="th"><meta charset="utf-8"><title>SCB Power Up #2 - Offline Exercise Guide</title><style>' + css + '</style><body>' + footer + cover + contents + intro + ''.join(rendered) + '</body></html>'
(work / 'guide.html').write_text(html_doc)
output = DOWNLOADS / 'SCB-Power-Up-2-Offline-Exercise-Guide.pdf'
HTML(string=html_doc, base_url=ROOT.as_uri()).write_pdf(output)
# Pango can leave the decomposed Thai sara-am's nikhahit glyph without a
# ToUnicode value. Restore that glyph's Unicode mapping without changing pixels.
reader = PdfReader(output)
seen = set()
for page in reader.pages:
    for font_ref in page['/Resources']['/Font'].values():
        font = font_ref.get_object()
        if 'Thai' not in str(font.get('/BaseFont')) or id(font) in seen: continue
        seen.add(id(font))
        cmap = font['/ToUnicode'].get_object().get_data().decode('ascii')
        font_name = 'ThaiHeading' if 'Semi-Bold' in str(font['/BaseFont']) else 'ThaiRegular'
        tt = TTFont(work / f'{font_name}.ttf')
        glyph_id = tt.getGlyphID(tt.getBestCmap()[0x0e4d])
        cmap = cmap.replace(f'<{glyph_id:04x}> <>', f'<{glyph_id:04x}> <0e4d>')
        font['/ToUnicode'].get_object().set_data(cmap.encode('ascii'))
writer = PdfWriter()
writer.clone_document_from_reader(reader)
writer.write(output)

(work / 'validation-source.json').write_text(json.dumps({'revision': revision, 'source_hashes': source_hashes, 'toc': toc, 'blocks': blocks}, ensure_ascii=False, indent=2))
print(json.dumps({'pdf': str(output), 'practices': 25, 'code_blocks': len(blocks), 'source': revision}))
