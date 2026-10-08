import sys
sys.path.append('normal_christian_life')
import inspect_pdf
import re

# Chapter 1 is in streams 5 to 13 (before stream 14 which starts Chapter 2)
ch1_text_parts = []
for idx in range(5, 14):
    p = [text for s_idx, text in inspect_pdf.full_pages if s_idx == idx]
    if p:
        ch1_text_parts.append(p[0])

ch1_full = '\n\n'.join(ch1_text_parts)
print(f'Chapter 1 total raw chars: {len(ch1_full)}')

# Let's inspect subheadings and structure
# Let's see if we see "Our Dual Problem" or similar
subheadings = re.findall(r'[A-Z][A-Za-z\s:,]{4,40}', ch1_full)
print('Sample text start:')
print(ch1_full[:1500])
