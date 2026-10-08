import zlib
import re

with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
print('Total streams:', len(streams))

full_pages = []
for idx, s in enumerate(streams):
    try:
        decomp = zlib.decompress(s).decode('latin1', errors='replace')
    except Exception:
        continue
    if 'BT' not in decomp:
        continue
    tj_blocks = re.findall(r'(\[(?:[^\]\\]|\\.)*\]\s*TJ|\((?:[^\)\\]|\\.)*\)\s*Tj)', decomp)
    text_pieces = []
    for blk in tj_blocks:
        if blk.endswith('TJ'):
            parts = re.findall(r'\(((?:[^\)\\]|\\.)*)\)', blk)
            cleaned = [p.replace(r'\(', '(').replace(r'\)', ')').replace(r'\\', '\\') for p in parts]
            text_pieces.append(''.join(cleaned))
        else:
            m = re.match(r'\(((?:[^\)\\]|\\.)*)\)\s*Tj', blk)
            if m:
                p = m.group(1).replace(r'\(', '(').replace(r'\)', ')').replace(r'\\', '\\')
                text_pieces.append(p)
    full_text = ' '.join(text_pieces).strip()
    full_pages.append((idx, full_text))

print('Pages with text:', len(full_pages))
for idx, pt in full_pages:
    m = re.search(r'(CHAPTER\s+(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|[0-9]+))', pt, re.I)
    if m:
        print(f'Stream {idx}: {m.group(0)} -> {pt[:140]}...')
