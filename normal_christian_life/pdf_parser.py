import zlib
import re

def parse_pdf_stream(decomp):
    # Match text operators and positioning operators
    ops = re.finditer(
        r'(\[(?:[^\]\\]|\\.)*\]\s*TJ|\((?:[^\)\\]|\\.)*\)\s*Tj|'
        r'[-0-9.]+\s+[-0-9.]+\s+TD|[-0-9.]+\s+[-0-9.]+\s+Td|'
        r'[-0-9.]+\s+[-0-9.]+\s+[-0-9.]+\s+[-0-9.]+\s+[-0-9.]+\s+[-0-9.]+\s+Tm|T\*)',
        decomp
    )

    current_line = []
    lines = []

    for m in ops:
        tok = m.group(0).strip()
        if tok.endswith('TJ'):
            parts = re.findall(r'\(((?:[^\)\\]|\\.)*)\)', tok)
            cleaned = []
            for p in parts:
                p = p.replace(r'\(', '(').replace(r'\)', ')').replace(r'\\', '\\')
                cleaned.append(p)
            current_line.append(''.join(cleaned))
        elif tok.endswith('Tj'):
            match = re.match(r'\(((?:[^\)\\]|\\.)*)\)\s*Tj', tok)
            if match:
                p = match.group(1).replace(r'\(', '(').replace(r'\)', ')').replace(r'\\', '\\')
                current_line.append(p)
        elif tok == 'T*':
            lines.append(''.join(current_line))
            current_line = []
        elif tok.endswith('TD') or tok.endswith('Td'):
            parts = tok.split()
            dx, dy = float(parts[0]), float(parts[1])
            if abs(dy) > 0.01:
                lines.append(''.join(current_line))
                current_line = []
        elif tok.endswith('Tm'):
            if current_line:
                lines.append(''.join(current_line))
                current_line = []

    if current_line:
        lines.append(''.join(current_line))

    return lines

if __name__ == '__main__':
    with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
        data = f.read()

    streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)
    decomp = zlib.decompress(streams[5]).decode('latin1', errors='replace')
    lines = parse_pdf_stream(decomp)
    for l in lines[:15]:
        if l.strip():
            print(repr(l.strip()))
