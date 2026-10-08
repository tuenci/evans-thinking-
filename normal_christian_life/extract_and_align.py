import os
import sys
import glob
import re
import zlib

sys.path.append('normal_christian_life')
import pdf_parser

# Output directories
os.makedirs('normal_christian_life/extracted_zh', exist_ok=True)
os.makedirs('normal_christian_life/extracted_en', exist_ok=True)

# 1. Process Chinese raw HTML files
zh_files = sorted(glob.glob('normal_christian_life/chinese_raw/*.htm'))
print(f"Processing {len(zh_files)} Chinese HTML files...")

chap_titles_zh = [
    "第一章：基督的血",
    "第二章：基督的十字架",
    "第三章：长进的途径－知道",
    "第四章：长进的途径－计算",
    "第五章：十字架的分界",
    "第六章：长进的途径－将自己献给神",
    "第七章：永远的目的",
    "第八章：圣灵",
    "第九章：罗马第七章的意义与价值",
    "第十章：长进的途径－随从灵而行",
    "第十一章：在基督里面一个身体",
    "第十二章：十字架与魂生命",
    "第十三章：长进的途径－背十字架",
    "第十四章：福音的目的"
]

chap_titles_en = [
    "Chapter 1: The Blood of Christ",
    "Chapter 2: The Cross of Christ",
    "Chapter 3: The Path of Progress: Knowing",
    "Chapter 4: The Path of Progress: Reckoning",
    "Chapter 5: The Divide of the Cross",
    "Chapter 6: The Path of Progress: Presenting Ourselves to God",
    "Chapter 7: The Eternal Purpose",
    "Chapter 8: The Holy Spirit",
    "Chapter 9: The Meaning and Value of Romans Seven",
    "Chapter 10: The Path of Progress: Walking in the Spirit",
    "Chapter 11: One Body in Christ",
    "Chapter 12: The Cross and the Soul Life",
    "Chapter 13: The Path of Progress: Bearing the Cross",
    "Chapter 14: The Goal of the Gospel"
]

for idx, fpath in enumerate(zh_files):
    with open(fpath, 'r', encoding='gb18030', errors='ignore') as f:
        raw = f.read()
    
    cells = re.findall(r'<td[^>]*>(.*?)</td>', raw, re.DOTALL | re.I)
    main = cells[4]
    
    # Format b tags as headings
    # If it's the chapter title at the top, format as # Title
    main_clean = main
    # Replace the top chapter title
    main_clean = re.sub(r'<b>\s*(?:<font[^>]*>)?\s*(第[一二三四五六七八九十]+章[^\n<]+)\s*(?:</font>)?\s*</b>', r'\n\n# \1\n\n', main_clean, flags=re.I)
    # Replace other <b> as ### Headings
    main_clean = re.sub(r'<b>\s*(?:<font[^>]*>)?\s*(.*?)\s*(?:</font>)?\s*</b>', r'\n\n### \1\n\n', main_clean, flags=re.DOTALL | re.I)
    
    main_clean = re.sub(r'<br\s*/?>', '\n', main_clean, flags=re.I)
    main_clean = re.sub(r'<p[^>]*>', '\n\n', main_clean, flags=re.I)
    main_clean = re.sub(r'</p>', '\n', main_clean, flags=re.I)
    main_clean = re.sub(r'<[^>]+>', '', main_clean)
    
    # Split paragraphs
    paras = [p.strip() for p in main_clean.split('\n') if p.strip()]
    
    md_lines = []
    for p in paras:
        p = re.sub(r'\s+', ' ', p)
        if p.startswith('# '):
            md_lines.append(f"# {chap_titles_zh[idx]}\n")
        elif p.startswith('### '):
            heading = p[4:].strip()
            # Clean any title duplication
            if '章' in heading and idx < 9 and f'第{idx+1}' in heading:
                continue
            md_lines.append(f"### {heading}\n")
        else:
            md_lines.append(f"{p}\n")
            
    out_zh_file = f'normal_christian_life/extracted_zh/{idx+1:02d}_Chapter_{idx+1:02d}.md'
    with open(out_zh_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(md_lines))
    print(f"Saved ZH: {out_zh_file} ({len(md_lines)} lines)")

# 2. Process English PDF
with open('normal_christian_life/The_Normal_Christian_Life.pdf', 'rb') as f:
    pdf_data = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', pdf_data, re.DOTALL)

chap_stream_ranges = [
    (1, 5, 13),
    (2, 14, 20),
    (3, 21, 26),
    (4, 27, 36),
    (5, 37, 42),
    (6, 43, 46),
    (7, 47, 52),
    (8, 53, 64),
    (9, 65, 74),
    (10, 75, 85),
    (11, 86, 94),
    (12, 95, 103),
    (13, 104, 113),
    (14, 114, 121)
]

def get_stream_lines(s_start, s_end):
    lines = []
    for s_idx in range(s_start, s_end + 1):
        if s_idx >= len(streams):
            break
        try:
            decomp = zlib.decompress(streams[s_idx]).decode('latin1', errors='replace')
        except Exception:
            continue
        if 'BT' not in decomp:
            continue
        l = pdf_parser.parse_pdf_stream(decomp)
        lines.extend(l)
    return lines

for ch_num, s_start, s_end in chap_stream_ranges:
    raw_lines = get_stream_lines(s_start, s_end)
    
    # If chapter 14, cut off at 'Endnotes'
    if ch_num == 14:
        cut_idx = None
        for i_l, l_txt in enumerate(raw_lines):
            if 'Endnotes' in l_txt:
                cut_idx = i_l
                break
        if cut_idx is not None:
            raw_lines = raw_lines[:cut_idx]
            
    blocks = []
    curr_block = []
    
    for l in raw_lines:
        if not l.strip():
            if curr_block:
                blocks.append(' '.join(curr_block))
                curr_block = []
            continue
        
        is_indent = bool(re.match(r'^\s{3,}', l))
        stripped = l.strip()
        
        if is_indent:
            if curr_block:
                blocks.append(' '.join(curr_block))
                curr_block = []
            curr_block.append(stripped)
        else:
            # Check if heading
            if len(stripped) < 65 and not stripped.endswith(('.', ';', ',', ':')) and (not curr_block or curr_block[-1].endswith(('.', '!"', '?"', '."'))):
                if curr_block:
                    blocks.append(' '.join(curr_block))
                    curr_block = []
                blocks.append(f"### {stripped}")
                continue
            curr_block.append(stripped)
            
    if curr_block:
        blocks.append(' '.join(curr_block))
        
    # Build markdown
    md_lines = [f"# {chap_titles_en[ch_num - 1]}\n"]
    for b in blocks:
        b_clean = re.sub(r'\s+', ' ', b).strip()
        if not b_clean:
            continue
        if b_clean.startswith('### Chapter'):
            continue
        if b_clean.startswith('Chapter ') and 'The Normal Christian Life' in b_clean:
            continue
        if b_clean.startswith('### '):
            md_lines.append(f"{b_clean}\n")
        else:
            md_lines.append(f"{b_clean}\n")
            
    out_en_file = f'normal_christian_life/extracted_en/{ch_num:02d}_Chapter_{ch_num:02d}.md'
    with open(out_en_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(md_lines))
    print(f"Saved EN: {out_en_file} ({len(md_lines)} lines)")

# 3. Process Endnotes (Stream 121-123)
endnotes_raw = get_stream_lines(121, 123)
start_idx = 0
for idx, l in enumerate(endnotes_raw):
    if 'Endnotes' in l:
        start_idx = idx
        break

endnotes_filtered = endnotes_raw[start_idx:]
endnotes_blocks = []
curr_n = []
for l in endnotes_filtered:
    if not l.strip():
        if curr_n:
            endnotes_blocks.append(' '.join(curr_n))
            curr_n = []
        continue
    stripped = l.strip()
    is_indent = bool(re.match(r'^\s{3,}', l))
    if is_indent:
        if curr_n:
            endnotes_blocks.append(' '.join(curr_n))
            curr_n = []
        curr_n.append(stripped)
    else:
        # Check if editor attribution or note start
        if stripped.startswith(('katargeo', 'sumphtuos', 'long-ien', 'Note .--', 'The Holy Spirit,', 'The Life of', 'Autobiography', 'ek,', 'li-mien', 'Corinthians', 'of Pagoda', 'was the home', 'Hudson Taylor')):
            if curr_n:
                endnotes_blocks.append(' '.join(curr_n))
                curr_n = []
            curr_n.append(stripped)
        else:
            curr_n.append(stripped)

if curr_n:
    endnotes_blocks.append(' '.join(curr_n))

# Save EN Endnotes
with open('normal_christian_life/extracted_en/15_Endnotes.md', 'w', encoding='utf-8') as f:
    f.write("# Appendix: Theological Endnotes & Textual References\n\n")
    for b in endnotes_blocks:
        b_clean = re.sub(r'\s+', ' ', b).strip()
        if b_clean:
            f.write(f"{b_clean}\n\n")
print(f"Saved EN Endnotes: 15_Endnotes.md ({len(endnotes_blocks)} blocks)")

# Create corresponding ZH Endnotes
zh_endnotes = """# 附录：全书神学详注与原版考证

大部分读者对于“十字架”一词的现今用法当十分熟悉，该词首先指主耶稣自己历史上在受死、埋葬、复活与升天中所完成的全部救赎大工（腓二8～9）；其次在更广义的层面，指信徒借着恩典在其中与祂的联合（罗六4；弗二5～6）。显然，在该词的这一用法中，“宝血”在对付罪愆赦免上的功效（如本书第一章所述），从神的眼光来看，乃是包含在十字架工作之内。然而在本书随后的各章中，作者因缺乏其他合宜字眼，不得不在一个更具体而受限的教义意义上使用“十字架”一词，借以作出有益的区分——即在人的角度将“代赎”（Substitution）与“联合”（Identification）视为救赎真理的两个不同层面。因此，全称不得不被用来指代其部分。读者在阅读下文时当谨记此点。—— 原书英编者注（Ed.）

历史或时间上的意义：唯有在历史的意义上，这一陈述才是可逆的。—— 倪柝声原注（W.N.）

戴德生与中国内地会（《Hudson Taylor and the China Inland Mission》，霍华德·泰勒博士夫妇著），第十二章“交换的生命”。全段皆值得细心研读。—— 原书英编者注（Ed.）

罗马书六章六节（钦定本）中被译为“灭绝”（destroyed）的希腊字 *katargeo*，其原意并非“彻底消灭”，而是“使其失去效用”、“使其瘫痪无能”。该字源于希腊文字根 *argos*，意为“不活动”、“不工作”、“无收益”，马太福音二十章三节、六节在市集上闲立无工可作的人即用此字。—— 原书英编者注（Ed.）

希腊字 *sumphytos*：意为“同栽同长”、“一同联合”。在古典希腊文中亦有“嫁接”之意。在下文生动精彩的譬喻中，或许不必过分拘泥于植物嫁接的字面细节，因若无适度界定，暗示基督被嫁接到旧树干上是不完全严谨的。然而，又有何种地上的譬喻能彻底描摹新造的奇迹呢？—— 原书英编者注（Ed.）

龙眼（*Euphoria longana*，中国本土水果）：果实形如杏子大小，内有浑圆果核，外皮干燥淡褐如纸，果肉晶莹雪白多汁如葡萄。在中国既可鲜食亦可烘制为龙眼干（桂圆），因其美味与极高滋补价值而深受珍视。—— 原书英编者注（Ed.）

对于这一罕见异象与经历的记载，其后所作的见证是无可置疑的。—— 原书英编者注（Ed.）

神学字词考订：罗马书六章中的两个希腊动词 *paristano* 与 *paristemi*，在修订本（R.V.）中皆译为“献上”（present），而在英钦定本（A.V.）中则译为“降服/让步”（yield）。*paristemi* 经常带有此种积极奉献之义，如罗马书十二章一节、哥林多后书十一章二节、歌罗西书一章二十二、二十八节，以及路加福音二章二十二节记载在圣殿中将婴孩耶稣“献与主”。这两个字皆带有主动积极的行动意涵，因此修订本的“献上”（present）远优于钦定本。“Yield”带有一种消极被动的“投降/听任”意味，长期影响了许多福音派的思想，但这并不符合罗马书此处的上下文脉络。—— 原书英编者注（Ed.）

毕罗德（R.A. Torrey）博士著：《圣灵：祂是谁与祂的作为》（*The Holy Spirit, who He is and what He does*），第198-199页。
慕迪生平（*The Life of Dwight L. Moody*），其子 W.R. Moody 著，第149页。
芬尼自传（*Autobiography of Charles E. Finney*），第二章。

希腊文介词 *ek*：其深邃之内涵极难用任何单一英文词汇完全表达。—— 原书英编者注（Ed.）

中文俗语：“里面当家的”（*li-mien tang-chia tih*）—— 指在内心掌权主导、主持家计并定规一切的主事人。—— 原书英编者注（Ed.）

哥林多前书十一章二十八至二十九节与哥林多后书十三章五节之辨析：前者吩咐我们在领受主的圣餐时当省察自己，分辨是否认得主的身体；这与圣餐擘饼直接相联，并非指一般的自我检视。而保罗在后一处经文中严正吩咐我们省察自己“有信心没有”，这是关乎我们里面是否存在根本的救赎信心，即我们究竟是不是真实的基督徒。这与我们在圣灵里的日常行事生活，或内省式的自知并无直接关联。—— 倪柝声原注（W.N.）

福州罗星塔（Pagoda Anchorage, Foochow）：福建闽江门户，见本书相关记叙。—— 原书英编者注（Ed.）

伯大尼西门之家：乃是马利亚、马大与拉撒路之故乡，西门据考亦为两姊妹之亲属。—— 原书英编者注（Ed.）
"""

with open('normal_christian_life/extracted_zh/15_Endnotes.md', 'w', encoding='utf-8') as f:
    f.write(zh_endnotes)
print("Saved ZH Endnotes: 15_Endnotes.md")
