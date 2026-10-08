import zlib
import re
import os

pdf_path = '/Users/evan/.gemini/antigravity/brain/efaef208-de04-415c-b332-8944ee4b4674/.user_uploaded/media_1790717608521.pdf'

with open(pdf_path, 'rb') as f:
    data = f.read()

# Build comprehensive CMap lookup
cmap = {}
for m in re.finditer(rb'<<[^>]*?/ToUnicode\s+(\d+)\s+0\s+R.*?>>', data):
    obj_id = m.group(1)
    stream_m = re.search(rb'\b' + obj_id + rb'\s+0\s+obj\b.*?stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
    if stream_m:
        decomp = zlib.decompress(stream_m.group(1)).decode('latin1', errors='ignore')
        for line in decomp.splitlines():
            line = line.strip()
            bfm = re.findall(r'<([0-9A-Fa-f]+)>\s+<([0-9A-Fa-f]+)>', line)
            for src_hex, dst_hex in bfm:
                if len(src_hex) == 2:
                    src_byte = int(src_hex, 16)
                    dst_chars = ''
                    for i in range(0, len(dst_hex), 4):
                        dst_chars += chr(int(dst_hex[i:i+4], 16))
                    cmap[src_byte] = dst_chars

def decode_bytes(b):
    out = []
    i = 0
    n = len(b)
    while i < n:
        if b[i] == ord('\\') and i + 1 < n:
            i += 1
            c = b[i]
            if ord('0') <= c <= ord('7'):
                oct_digits = bytes([c])
                for _ in range(2):
                    if i + 1 < n and ord('0') <= b[i+1] <= ord('7'):
                        i += 1
                        oct_digits += bytes([b[i]])
                    else:
                        break
                val = int(oct_digits, 8)
                out.append(cmap.get(val, bytes([val]).decode('cp1252', errors='replace')))
            elif c == ord('n'): out.append('\n')
            elif c == ord('r'): out.append('\r')
            elif c == ord('t'): out.append('\t')
            elif c == ord('b'): out.append('\b')
            elif c == ord('f'): out.append('\f')
            elif c == ord('('): out.append('(')
            elif c == ord(')'): out.append(')')
            elif c == ord('\\'): out.append('\\')
            elif c in [ord('\r'), ord('\n')]:
                if c == ord('\r') and i + 1 < n and b[i+1] == ord('\n'):
                    i += 1
            else:
                out.append(chr(c))
        else:
            val = b[i]
            out.append(cmap.get(val, chr(val)))
        i += 1
    return ''.join(out)

def get_page_text_blocks(p_num):
    page_matches = list(re.finditer(rb'<<[^\r\n]*?/Type\s*/Page\b.*?>>', data, re.DOTALL))
    if p_num > len(page_matches): return []
    p_dict = page_matches[p_num - 1].group(0)
    contents_ref = re.search(rb'/Contents\s+(\d+)\s+(\d+)\s+R', p_dict)
    if not contents_ref: return []
    obj_num = int(contents_ref.group(1))
    obj_pat = re.compile(rb'\b' + str(obj_num).encode() + rb'\s+0\s+obj\b.*?stream[\r\n]+(.*?)[\r\n]+endstream', re.DOTALL)
    stream_m = obj_pat.search(data)
    if not stream_m: return []
    decomp = zlib.decompress(stream_m.group(1))
    
    # Extract blocks with position
    bt_et_pattern = re.compile(rb'BT\s*(.*?)\s*ET', re.DOTALL)
    blocks = []
    for bt in bt_et_pattern.finditer(decomp):
        block = bt.group(1)
        tm = re.findall(rb'([\d\.\-]+)\s+([\d\.\-]+)\s+Tm', block)
        font = re.findall(rb'/([A-Za-z0-9_]+)\s+([\d\.]+)\s+Tf', block)
        
        # Extract TJ and Tj
        cmd_pattern = re.compile(rb'(\[(?:[^\[\]]|\\[\[\]])*\])\s*TJ|(\((?:[^\(\)]|\\\(|\\\))*\))\s*T[j\']', re.DOTALL)
        parts = []
        for m in cmd_pattern.finditer(block):
            tj_arr, tj_single = m.groups()
            if tj_arr:
                strs = re.findall(rb'\(((?:[^\(\)]|\\\(|\\\))*)\)', tj_arr)
                parts.append(''.join(decode_bytes(s) for s in strs))
            elif tj_single:
                parts.append(decode_bytes(tj_single[1:-1]))
        text = ' '.join(parts).strip()
        text = re.sub(r'\s+', ' ', text)
        if text:
            blocks.append((tm[-1] if tm else None, font[-1] if font else None, text))
    return blocks

# Let's inspect page 13, 14, 15
for p in [13, 14, 15]:
    print(f"=== PAGE {p} ===")
    for tm, font, txt in get_page_text_blocks(p):
        print(f"  [font={font}, y={tm[1] if tm else '?'}] {txt}")
