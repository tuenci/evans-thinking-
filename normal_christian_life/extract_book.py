import zlib
import re
import os
import urllib.request
from urllib.parse import quote

def extract_pdf_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        data = f.read()

    streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
    pages_text = []

    for idx, s in enumerate(streams):
        try:
            decomp = zlib.decompress(s).decode('latin1', errors='replace')
        except Exception:
            continue

        # Check if stream has BT ... ET
        if 'BT' not in decomp:
            continue

        tj_blocks = re.findall(r'(\[(?:[^\]\\]|\\.)*\]\s*TJ|\((?:[^\)\\]|\\.)*\)\s*Tj)', decomp)
        text_pieces = []
        for blk in tj_blocks:
            if blk.endswith('TJ'):
                parts = re.findall(r'\(((?:[^\)\\]|\\.)*)\)', blk)
                cleaned = []
                for p in parts:
                    p = p.replace('\\(', '(').replace('\\)', ')').replace('\\\\', '\\')
                    cleaned.append(p)
                text_pieces.append(''.join(cleaned))
            else:
                m = re.match(r'\(((?:[^\)\\]|\\.)*)\)\s*Tj', blk)
                if m:
                    p = m.group(1).replace('\\(', '(').replace('\\)', ')').replace('\\\\', '\\')
                    text_pieces.append(p)
        
        full_text = ' '.join(text_pieces).strip()
        if full_text:
            pages_text.append((idx, full_text))

    return pages_text

if __name__ == '__main__':
    pdf_path = 'normal_christian_life/The_Normal_Christian_Life.pdf'
    pages = extract_pdf_pages(pdf_path)
    print(f'Extracted {len(pages)} text streams from PDF.')
    for idx, p in pages[:5]:
        print(f'--- Stream {idx} ({len(p)} chars) ---')
        print(p[:300])
        print()
