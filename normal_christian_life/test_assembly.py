import sys
sys.path.append('normal_christian_life')
import pdf_parser, zlib, re

with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)

def get_chapter_lines(s_start, s_end):
    lines = []
    for s_idx in range(s_start, s_end + 1):
        if s_idx >= len(streams):
            break
        try:
            decomp = zlib.decompress(streams[s_idx]).decode('latin1', errors='replace')
        except Exception:
            continue
        if 'BT' not in decomp:
            continue
        l = pdf_parser.parse_pdf_stream(decomp)
        lines.extend(l)
    return lines

lines_ch1 = get_chapter_lines(5, 13)

blocks = []
curr_block = []

for l in lines_ch1:
    if not l.strip():
        if curr_block:
            blocks.append(' '.join(curr_block))
            curr_block = []
        continue
    
    is_indent = bool(re.match(r'^\s{3,}', l))
    stripped = l.strip()
    
    if is_indent:
        if curr_block:
            blocks.append(' '.join(curr_block))
            curr_block = []
        curr_block.append(stripped)
    else:
        # Check if heading: short, capitalized, no punctuation at end
        if len(stripped) < 60 and not stripped.endswith(('.', ';', ',', ':')) and (not curr_block or curr_block[-1].endswith(('.', '!"', '?"', '."'))):
            if curr_block:
                blocks.append(' '.join(curr_block))
                curr_block = []
            blocks.append(f"### {stripped}")
            continue
        curr_block.append(stripped)

if curr_block:
    blocks.append(' '.join(curr_block))

print(f"Total blocks in Ch 1: {len(blocks)}")
for i, b in enumerate(blocks[:15]):
    print(f"Block {i+1}: {b[:90]}...")
