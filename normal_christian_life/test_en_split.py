import sys
sys.path.append('normal_christian_life')
import inspect_pdf
import re

# Get ch1
ch1_pages = [text for idx, text in inspect_pdf.full_pages if 5 <= idx < 14]
ch1_full = ' '.join(ch1_pages)

# Remove "Chapter 1: The Blood of Christ" at start
ch1_full = re.sub(r'^Chapter 1:\s*The\s+Bl\s*ood of Christ\s*', '', ch1_full, flags=re.I)

# In the PDF, paragraphs are separated by 3 or more spaces
en_paras = [p.strip() for p in re.split(r'\s{3,}', ch1_full) if p.strip()]

print(f'Total English paragraphs extracted: {len(en_paras)}')
for i in range(min(15, len(en_paras))):
    print(f'EN {i+1}: {en_paras[i][:80]}...')
