import os

chapters = [
    ("01", "第一章：基督的血", "Chapter 1: The Blood of Christ"),
    ("02", "第二章：基督的十字架", "Chapter 2: The Cross of Christ"),
    ("03", "第三章：长进的途径－知道", "Chapter 3: The Path of Progress: Knowing"),
    ("04", "第四章：长进的途径－计算", "Chapter 4: The Path of Progress: Reckoning"),
    ("05", "第五章：十字架的分界", "Chapter 5: The Divide of the Cross"),
    ("06", "第六章：长进的途径－将自己献给神", "Chapter 6: The Path of Progress: Presenting Ourselves to God"),
    ("07", "第七章：永远的目的", "Chapter 7: The Eternal Purpose"),
    ("08", "第八章：圣灵", "Chapter 8: The Holy Spirit"),
    ("09", "第九章：罗马第七章的意义与价值", "Chapter 9: The Meaning and Value of Romans Seven"),
    ("10", "第十章：长进的途径－随从灵而行", "Chapter 10: The Path of Progress: Walking in the Spirit"),
    ("11", "第十一章：在基督里面一个身体", "Chapter 11: One Body in Christ"),
    ("12", "第十二章：十字架与魂生命", "Chapter 12: The Cross and the Soul Life"),
    ("13", "第十三章：长进的途径－背十字架", "Chapter 13: The Path of Progress: Bearing the Cross"),
    ("14", "第十四章：福音的目的", "Chapter 14: The Goal of the Gospel"),
    ("15", "附录：全书神学详注与原版考证", "Appendix: Theological Endnotes & Textual References")
]

doc_lines = [
    "# 《正常的基督徒生活》（中英双语典藏全集）",
    "## The Normal Christian Life (Bilingual Critical Edition)",
    "",
    "**作者**：倪柝声（Watchman Nee）  ",
    "**中文出处**：《倪柝声文集》第二辑第13册  ",
    "**英文出处**：*The Normal Christian Life* (Angus I. Kinnear 编订官方英译本)  ",
    "**著作背景**：《正常的基督徒生活》（英语：The Normal Christian Life）是倪柝声于1938年至1939年旅行欧洲时完成的著名作品，首先用英语在英国（开西大会）、丹麦讲道时发表，回中国后由上海福音书房出版了中文文本。该书被许多基督徒视为经典著作，这也是西方基督教界最熟悉的一本倪柝声著作。该书已经用多种语言出版，至今至少出版了25万册。  ",
    "**典藏发布**：Evan's Thinking 基督教神学与典藏文献库 (evans-thinking.pages.dev)  ",
    "",
    "---",
    ""
]

for code, title_zh, title_en in chapters:
    doc_lines.append(f"## {title_zh}")
    doc_lines.append(f"### {title_en}")
    doc_lines.append("")
    
    if code == "15":
        zh_path = "normal_christian_life/extracted_zh/15_Endnotes.md"
        en_path = "normal_christian_life/extracted_en/15_Endnotes.md"
    else:
        zh_path = f"normal_christian_life/extracted_zh/{code}_Chapter_{code}.md"
        en_path = f"normal_christian_life/extracted_en/{code}_Chapter_{code}.md"
        
    with open(zh_path, "r", encoding="utf-8") as f:
        zh_content = f.read().strip()
    with open(en_path, "r", encoding="utf-8") as f:
        en_content = f.read().strip()
        
    doc_lines.append("### 🇨🇳 中文经典译文")
    doc_lines.append("")
    doc_lines.append(zh_content)
    doc_lines.append("")
    doc_lines.append("### 🇬🇧 English Original Text")
    doc_lines.append("")
    doc_lines.append(en_content)
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")

full_md = "\n".join(doc_lines)

out_file1 = "正常的基督徒生活_倪柝声_中英双语对照版.md"
with open(out_file1, "w", encoding="utf-8") as f:
    f.write(full_md)
print(f"Generated {out_file1} ({len(full_md)} chars)")

out_file2 = "Google云端硬盘上传发布包/正常的基督徒生活_倪柝声_中英双语对照版.md"
with open(out_file2, "w", encoding="utf-8") as f:
    f.write(full_md)
print(f"Generated {out_file2} ({len(full_md)} chars)")
