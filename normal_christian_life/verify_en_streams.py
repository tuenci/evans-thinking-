import sys
sys.path.append('normal_christian_life')
import pdf_parser
import zlib
import re

with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)

# Map stream_idx to decompressed lines
stream_lines = {}
for idx, s in enumerate(streams):
    try:
        decomp = zlib.decompress(s).decode('latin1', errors='replace')
    except Exception:
        continue
    if 'BT' not in decomp:
        continue
    lines = pdf_parser.parse_pdf_stream(decomp)
    stream_lines[idx] = lines

chap_stream_ranges = [
    (1, 5, 13, "The Blood of Christ"),
    (2, 14, 20, "The Cross of Christ"),
    (3, 21, 26, "The Path of Progress: Knowing"),
    (4, 27, 36, "The Path of Progress: Reckoning"),
    (5, 37, 42, "The Divide of the Cross"),
    (6, 43, 46, "The Path of Progress: Presenting Ourselves to God"),
    (7, 47, 52, "The Eternal Purpose"),
    (8, 53, 64, "The Holy Spirit"),
    (9, 65, 74, "The Meaning and Value of Romans Seven"),
    (10, 75, 85, "The Path of Progress: Walking in the Spirit"),
    (11, 86, 94, "One Body in Christ"),
    (12, 95, 103, "The Cross and the Soul Life"),
    (13, 104, 113, "The Path of Progress: Bearing the Cross"),
    (14, 114, 121, "The Goal of the Gospel")
]

for ch_num, s_start, s_end, title in chap_stream_ranges:
    # gather all lines
    lines = []
    for s_idx in range(s_start, s_end + 1):
        if s_idx in stream_lines:
            lines.extend(stream_lines[s_idx])
    
    # filter empty lines
    non_empty = [l.strip() for l in lines if l.strip()]
    first_line = non_empty[0] if non_empty else "EMPTY"
    last_line = non_empty[-1] if non_empty else "EMPTY"
    if ch_num == 14:
        # Check where Endnotes is
        for idx_l, l in enumerate(non_empty):
            if 'Endnotes' in l:
                print(f"Ch 14: Found 'Endnotes' at line {idx_l} of {len(non_empty)}")
                last_line = non_empty[idx_l - 1]
                break

    print(f"Ch {ch_num:2d} ({len(non_empty):4d} lines) | Start: {first_line[:50]} | End: {last_line[-50:]}")
