import re

with open('normal_christian_life/chinese_raw/01_001第一章　基督的血.htm', 'r', encoding='gb18030', errors='ignore') as f:
    raw = f.read()

cells = re.findall(r'<td[^>]*>(.*?)</td>', raw, re.DOTALL | re.I)
main = cells[4]

# split by <br> or <p>
# replace <b>Heading</b> with ### Heading
# Let's inspect
main_clean = main
# convert <p align="center"><b>Title</b></p>
# In this cell, let's see how <b> tags are placed
# replace <b>X</b> with \n\n### X\n\n
main_clean = re.sub(r'<b>\s*(?:<font[^>]*>)?(.*?)(?:</font>)?\s*</b>', r'\n\n### \1\n\n', main_clean, flags=re.DOTALL)
main_clean = re.sub(r'<br\s*/?>', '\n', main_clean, flags=re.I)
main_clean = re.sub(r'<p[^>]*>', '\n\n', main_clean, flags=re.I)
main_clean = re.sub(r'</p>', '', main_clean, flags=re.I)
main_clean = re.sub(r'<[^>]+>', '', main_clean)

raw_blocks = [b.strip() for b in main_clean.split('\n') if b.strip()]
blocks = []
for b in raw_blocks:
    b = re.sub(r'\s+', ' ', b)
    if b:
        blocks.append(b)

print(f"Total ZH blocks in Ch 1: {len(blocks)}")
for i, b in enumerate(blocks[:15]):
    print(f"ZH {i+1}: {b[:70]}...")
