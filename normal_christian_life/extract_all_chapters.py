import zlib
import re
import sys
sys.path.append('normal_christian_life')
import pdf_parser

with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', data, re.DOTALL)

# Extract lines from all streams
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

print(f"Total pages extracted: {len(all_pages)}")

# Let's find chapter boundaries
# Each chapter starts with Chapter X: Title
# Stream ranges identified earlier:
# Ch 1: 5..13
# Ch 2: 14..20
# Ch 3: 21..26
# Ch 4: 27..36
# Ch 5: 37..42
# Ch 6: 43..46
# Ch 7: 47..52
# Ch 8: 53..64
# Ch 9: 65..74
# Ch 10: 75..85
# Ch 11: 86..94
# Ch 12: 95..103
# Ch 13: 104..113
# Ch 14: 114..121 (up to 'Endnotes')
# Endnotes: 121..123
