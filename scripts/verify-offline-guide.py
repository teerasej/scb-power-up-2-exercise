"""Verify the generated guide against exporter evidence, without changing it."""
from pathlib import Path
import argparse, hashlib, json, re, unicodedata
import pymupdf
from pypdf import PdfReader
parser = argparse.ArgumentParser()
parser.add_argument('--work-dir', type=Path, default=Path('/private/tmp/scb-offline-guide'))
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
downloads = root / 'docs/public/downloads'
evidence = json.loads((args.work_dir / 'validation-source.json').read_text())
pdf = downloads / 'SCB-Power-Up-2-Offline-Exercise-Guide.pdf'
doc = pymupdf.open(pdf)
reader = PdfReader(pdf)
def norm(text): return re.sub(r'\s+', '', unicodedata.normalize('NFKC', text))
fulltext = norm(''.join(p.get_text() for p in doc))
pypdf_text = norm(''.join(p.extract_text() for p in reader.pages))
for block in evidence['blocks']:
    content = (downloads / 'copy-text' / block['file']).read_bytes()
    assert hashlib.sha256(content).hexdigest() == block['sha256'], block['file']
    assert content.decode() == block['text']
    assert norm(block['text']) in fulltext, ('MuPDF extraction', block['file'])
    assert norm(block['text']) in pypdf_text, ('pypdf extraction', block['file'])
for _,title,_ in evidence['toc']:
    assert norm(title) in fulltext, title
bookmarks = {norm(entry[1]) for entry in doc.get_toc()}
for _,title,_ in evidence['toc']: assert norm(title) in bookmarks, title
contents_page = reader.get_destination_page_number(reader.named_destinations['contents'])
contacts = {'mailto:teerasej@nextflow.in.th','https://www.facebook.com/teerasej','https://www.youtube.com/teerasej'}
for i,page in enumerate(doc):
    assert abs(page.rect.width - 595.276) < 1 and abs(page.rect.height - 841.89) < 1
    links = page.get_links()
    assert contacts <= {l.get('uri') for l in links}, ('contacts',i+1)
    assert any(l.get('kind') in (1,4) and l.get('page')==contents_page for l in links), ('return link',i+1)
    for l in links:
        if l.get('kind') in (1,4): assert 0 <= l.get('page',-1) < len(doc)
    assert 'All rights reserved.' in page.get_text(), i+1
    for b in page.get_text('blocks'):
        assert b[0] >= 25 and b[2] <= page.rect.width-20 and b[1] >= 20 and b[3] < page.rect.height-10, ('overflow',i+1,b[:4])
for page in reader.pages:
    for ref in page['/Resources']['/Font'].values():
        font=ref.get_object()
        if '/DescendantFonts' in font:
            descriptor=font['/DescendantFonts'][0].get_object()['/FontDescriptor'].get_object()
            assert '/FontFile2' in descriptor or '/FontFile3' in descriptor
print(json.dumps({'pages':len(doc),'bookmarks':len(doc.get_toc()),'practices':sum(title.startswith('Practice ') for _,title,_ in evidence['toc']),'code_blocks':len(evidence['blocks']),'result':'passed'},indent=2))
