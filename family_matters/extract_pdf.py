import zlib
import re
import os

pdf_path = '/Users/evan/.gemini/antigravity/brain/efaef208-de04-415c-b332-8944ee4b4674/.user_uploaded/media_1790717608521.pdf'

with open(pdf_path, 'rb') as f:
    data = f.read()

def decode_pdf_bytes(b):
    # b is raw bytes from inside (...)
    # PDF literal strings can contain \ddd octal escapes, \n, \r, \t, \b, \f, \(, \), \\
    out = bytearray()
    i = 0
    n = len(b)
    while i < n:
        if b[i] == ord('\\') and i + 1 < n:
            i += 1
            c = b[i]
            if ord('0') <= c <= ord('7'):
                # octal digits up to 3
                oct_digits = bytes([c])
                for _ in range(2):
                    if i + 1 < n and ord('0') <= b[i+1] <= ord('7'):
                        i += 1
                        oct_digits += bytes([b[i]])
                    else:
                        break
                val = int(oct_digits, 8)
                out.append(val)
            elif c == ord('n'):
                out.append(ord('\n'))
            elif c == ord('r'):
                out.append(ord('\r'))
            elif c == ord('t'):
                out.append(ord('\t'))
            elif c == ord('b'):
                out.append(ord('\b'))
            elif c == ord('f'):
                out.append(ord('\f'))
            elif c == ord('('):
                out.append(ord('('))
            elif c == ord(')'):
                out.append(ord(')'))
            elif c == ord('\\'):
                out.append(ord('\\'))
            elif c in [ord('\r'), ord('\n')]:
                # line continuation
                if c == ord('\r') and i + 1 < n and b[i+1] == ord('\n'):
                    i += 1
            else:
                out.append(c)
        else:
            out.append(b[i])
        i += 1
    # Decode using cp1252 / latin1
    return out.decode('cp1252', errors='replace')

def extract_page_paragraphs(stream_data):
    # Extract text from stream
    # Each text block is BT ... ET
    # We want to extract lines and separate them cleanly
    bt_et_pattern = re.compile(rb'BT\s*(.*?)\s*ET', re.DOTALL)
    paragraphs = []
    
    for bt in bt_et_pattern.finditer(stream_data):
        block = bt.group(1)
        # Find all TJ and Tj commands
        cmd_pattern = re.compile(rb'(\[(?:[^\[\]]|\\[\[\]])*\])\s*TJ|(\((?:[^\(\)]|\\\(|\\\))*\))\s*T[j\']|(?:\-?[\d\.]+)\s+(?:\-?[\d\.]+)\s+T\*', re.DOTALL)
        
        block_text = []
        for m in cmd_pattern.finditer(block):
            tj_arr, tj_single = m.groups()
            if tj_arr:
                # extract all strings
                str_literals = re.findall(rb'\(((?:[^\(\)]|\\\(|\\\))*)\)', tj_arr)
                decoded_parts = [decode_pdf_bytes(s) for s in str_literals]
                block_text.append(''.join(decoded_parts))
            elif tj_single:
                body = tj_single[1:-1]
                block_text.append(decode_pdf_bytes(body))
        
        combined = ' '.join(block_text).strip()
        # Clean up multiple whitespaces
        combined = re.sub(r'[ \t]+', ' ', combined)
        if combined:
            paragraphs.append(combined)
            
    return paragraphs

# Extract all pages
page_matches = list(re.finditer(rb'<<[^\r\n]*?/Type\s*/Page\b.*?>>', data, re.DOTALL))
pages_text = {}

for p_idx, p_match in enumerate(page_matches):
    p_num = p_idx + 1
    p_dict = p_match.group(0)
    contents_ref = re.search(rb'/Contents\s+(\d+)\s+(\d+)\s+R', p_dict)
    decomp = b''
    if contents_ref:
        obj_num = int(contents_ref.group(1))
        obj_pat = re.compile(rb'\b' + str(obj_num).encode() + rb'\s+0\s+obj\b.*?stream[\r\n]+(.*?)[\r\n]+endstream', re.DOTALL)
        stream_m = obj_pat.search(data)
        if stream_m:
            try:
                decomp = zlib.decompress(stream_m.group(1))
            except Exception:
                pass
    else:
        contents_arr = re.search(rb'/Contents\s*\[(.*?)\]', p_dict)
        if contents_arr:
            arr_text = contents_arr.group(1)
            refs = re.findall(rb'(\d+)\s+0\s+R', arr_text)
            decomp_all = []
            for r in refs:
                obj_pat = re.compile(rb'\b' + r + rb'\s+0\s+obj\b.*?stream[\r\n]+(.*?)[\r\n]+endstream', re.DOTALL)
                stream_m = obj_pat.search(data)
                if stream_m:
                    try:
                        decomp_all.append(zlib.decompress(stream_m.group(1)))
                    except Exception:
                        pass
            decomp = b'\n'.join(decomp_all)
            
    paras = extract_page_paragraphs(decomp)
    pages_text[p_num] = paras

print(f"Total extracted pages: {len(pages_text)}")

# Let's inspect pages 1 to 6 (Front matter & Table of Contents)
for p in range(1, 7):
    print(f"================ PAGE {p} ================")
    for para in pages_text.get(p, []):
        print(para)
