import glob
import re
import sys
sys.path.append('normal_christian_life')
import pdf_parser, zlib

# Read Chinese chapters and extract headings
zh_files = sorted(glob.glob('normal_christian_life/chinese_raw/*.htm'))
zh_headings = []
for f in zh_files:
    with open(f, 'r', encoding='gb18030', errors='ignore') as fp:
        raw = fp.read()
    cells = re.findall(r'<td[^>]*>(.*?)</td>', raw, re.DOTALL | re.I)
    main = cells[4]
    b_tags = re.findall(r'<b>(.*?)</b>', main, re.DOTALL | re.I)
    cleaned_b = [re.sub(r'<[^>]+>', '', b).strip() for b in b_tags if re.sub(r'<[^>]+>', '', b).strip()]
    zh_headings.append(cleaned_b)

# Read PDF streams
with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
all_pages = []
for idx, s in enumerate(streams):
    try:
        decomp = zlib.decompress(s).decode('latin1', errors='replace')
    except Exception:
        continue
    if 'BT' not in decomp:
        continue
    lines = pdf_parser.parse_pdf_stream(decomp)
    all_pages.append((idx, lines))

for ch_idx in range(14):
    print(f"=== Chapter {ch_idx+1} ===")
    print("ZH Headings:", zh_headings[ch_idx])
