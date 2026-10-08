import re

with open('normal_christian_life/chinese_raw/01_001第一章　基督的血.htm', 'r', encoding='gb18030', errors='ignore') as f:
    raw = f.read()

cells = re.findall(r'<td[^>]*>(.*?)</td>', raw, re.DOTALL | re.I)
main_cell = cells[4]

# Let's inspect the tags in main_cell
# usually <br><br> or <p>
paras = re.split(r'(?:<br\s*/?>\s*){1,2}', main_cell, flags=re.I)
cleaned = []
for p in paras:
    p = re.sub(r'<[^>]+>', '', p).strip()
    p = re.sub(r'\s+', ' ', p)
    if p:
        cleaned.append(p)

print(f'Total paragraphs in Cell 4: {len(cleaned)}')
for i in range(min(10, len(cleaned))):
    print(f'{i+1}: {cleaned[i][:80]}...')
