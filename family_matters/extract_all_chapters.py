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
    obj_pat = re.compile(rb'\b' + obj_id + rb'\s+0\s+obj\b', re.DOTALL)
    sm = obj_pat.search(data)
    if sm:
        start = sm.start()
        stream_idx = data.find(b'stream', start)
        len_m = re.search(rb'/Length\s+(\d+)', data[start:stream_idx])
        if len_m:
            length = int(len_m.group(1))
            st_start = stream_idx + 6
            if data[st_start:st_start+2] == b'\r\n': st_start += 2
            elif data[st_start:st_start+1] in [b'\r', b'\n']: st_start += 1
            raw_stream = data[st_start:st_start+length]
            try:
                decomp = zlib.decompress(raw_stream).decode('latin1', errors='ignore')
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
            except Exception as e:
                pass

print(f"Total CMap entries mapped: {len(cmap)}")

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

def get_stream_by_obj_num(obj_num):
    obj_pat = re.compile(rb'\b' + str(obj_num).encode() + rb'\s+0\s+obj\b', re.DOTALL)
    m = obj_pat.search(data)
    if not m: return b''
    start = m.start()
    stream_idx = data.find(b'stream', start)
    if stream_idx == -1: return b''
    len_m = re.search(rb'/Length\s+(\d+)', data[start:stream_idx])
    if not len_m: return b''
    length = int(len_m.group(1))
    st_start = stream_idx + 6
    if data[st_start:st_start+2] == b'\r\n': st_start += 2
    elif data[st_start:st_start+1] in [b'\r', b'\n']: st_start += 1
    raw_stream = data[st_start:st_start+length]
    try:
        return zlib.decompress(raw_stream)
    except Exception as e:
        return b''

page_matches = list(re.finditer(rb'<<[^\r\n]*?/Type\s*/Page\b.*?>>', data, re.DOTALL))

def get_page_lines(p_num):
    if p_num > len(page_matches): return []
    p_dict = page_matches[p_num - 1].group(0)
    contents_ref = re.search(rb'/Contents\s+(\d+)\s+(\d+)\s+R', p_dict)
    if contents_ref:
        obj_num = int(contents_ref.group(1))
        decomp = get_stream_by_obj_num(obj_num)
    else:
        contents_arr = re.search(rb'/Contents\s*\[(.*?)\]', p_dict)
        if not contents_arr: return []
        refs = re.findall(rb'(\d+)\s+0\s+R', contents_arr.group(1))
        decomp = b'\n'.join([get_stream_by_obj_num(int(r)) for r in refs])
        
    bt_et_pattern = re.compile(rb'BT\s*(.*?)\s*ET', re.DOTALL)
    blocks = []
    
    for bt in bt_et_pattern.finditer(decomp):
        block = bt.group(1)
        tm = re.findall(rb'([\d\.\-]+)\s+([\d\.\-]+)\s+Tm', block)
        font = re.findall(rb'/([A-Za-z0-9_]+)\s+([\d\.]+)\s+Tf', block)
        
        # Regex matching balanced string literals with escape sequences
        str_pattern = re.compile(rb"\(((?:[^()\\]|\\.)*)\)")
        parts = []
        for m in str_pattern.finditer(block):
            parts.append(decode_bytes(m.group(1)))
        
        # In PDF TJ operator, strings are directly concatenated without adding extra spaces!
        text = ''.join(parts).strip()
        if text:
            # Check if this is just page number
            if text == str(p_num):
                continue
            y_pos = float(tm[-1][1]) if tm else 0.0
            font_name = font[-1][0].decode() if font else ''
            font_size = float(font[-1][1]) if font else 12.0
            blocks.append((y_pos, font_name, font_size, text))
            
    blocks.sort(key=lambda x: x[0], reverse=True)
    return blocks

chapters = [
    ("00_Front_Matter", 1, 6, "Front Matter & Table of Contents"),
    ("00_Introduction", 7, 11, "Introduction: The Church as Family"),
    ("01_Chapter_01", 12, 25, "Chapter 1: The Anabaptist Reformation"),
    ("02_Chapter_02", 26, 33, "Chapter 2: The Birth of 'the Brotherhood'"),
    ("03_Chapter_03", 34, 42, "Chapter 3: The MB Church Grows"),
    ("04_Chapter_04", 43, 56, "Chapter 4: People of the Word"),
    ("05_Chapter_05", 57, 71, "Chapter 5: The New Testament Church"),
    ("06_Chapter_06", 72, 87, "Chapter 6: Peacemaking"),
    ("07_Chapter_07", 88, 101, "Chapter 7: Disciples are Missionaries"),
    ("08_Chapter_08", 102, 114, "Chapter 8: Working Together"),
    ("09_Chapter_09", 115, 132, "Chapter 9: Mennonite Brethren in the U.S."),
    ("10_Chapter_10", 133, 164, "Chapter 10: The International MB Family (ICOMB)"),
    ("11_Chapter_11", 165, 186, "Chapter 11: Inter-Mennonite Connections"),
    ("12_Chapter_12", 187, 193, "Chapter 12: The Challenge for the Future"),
    ("13_Bibliography", 194, 199, "Recommended Reading & Works Cited"),
]

out_dir = '/Users/evan/.gemini/antigravity/scratch/mb_confession_translation/family_matters/extracted_en'
os.makedirs(out_dir, exist_ok=True)

for fname, start_p, end_p, title in chapters:
    lines = []
    lines.append(f"# {title}\n")
    for p in range(start_p, end_p + 1):
        blocks = get_page_lines(p)
        if not blocks:
            continue
        lines.append(f"\n<!-- Page {p} -->\n")
        current_para = []
        for y, font_name, font_size, text in blocks:
            # Check for headings
            if font_size > 14 or (font_name in ['TT0', 'TT1', 'TT2', 'TT3'] and len(text) < 60 and not text.endswith('.')):
                if current_para:
                    p_text = ' '.join(current_para)
                    p_text = re.sub(r'\s+', ' ', p_text)
                    lines.append(p_text + '\n')
                    current_para = []
                lines.append(f"\n### {text}\n")
            else:
                current_para.append(text)
        if current_para:
            p_text = ' '.join(current_para)
            p_text = re.sub(r'\s+', ' ', p_text)
            lines.append(p_text + '\n')
            current_para = []
            
    filepath = os.path.join(out_dir, f"{fname}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Extracted {fname} (pages {start_p}-{end_p}): {os.path.getsize(filepath)} bytes")

print("ALL CHAPTERS RE-EXTRACTED WITH PERFECT CONCATENATION!")
