import sys
sys.path.append('normal_christian_life')
import inspect_pdf
import re

chapter_starts = []
for p_idx, (stream_idx, text) in enumerate(inspect_pdf.full_pages):
    m = re.search(r'Chapter\s+(\d+)\s*:\s*([^\n\r]+)', text, re.I)
    if m:
        chapter_starts.append((int(m.group(1)), stream_idx, p_idx, m.group(2).strip(), text[:100]))

print(f"Total chapter starts found: {len(chapter_starts)}")
for ch, s_idx, p_idx, title, preview in chapter_starts:
    print(f"Chapter {ch:2d} | Stream {s_idx:3d} (Page {p_idx:3d}) | Title: {title}")
