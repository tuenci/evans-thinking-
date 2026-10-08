import os
import re
import html

CHAPTER_DEFS = [
    {
        "id": "chap-front",
        "art_code": "front",
        "num_label": "序言",
        "part": "导言与序章",
        "part_en": "Front Matter",
        "title_zh": "扉页、版权与目录",
        "title_en": "Title, Copyright & Table of Contents",
        "desc": "本书出版版权信息、美加门诺弟兄会总会出版声明与全书目录总览。",
        "en_file": "family_matters/extracted_en/00_Front_Matter.md",
        "zh_file": "family_matters/translations_zh/00_Front_Matter.md",
    },
    {
        "id": "chap-intro",
        "art_code": "intro",
        "num_label": "引言",
        "part": "导言与序章",
        "part_en": "Introduction",
        "title_zh": "教会作为神的家",
        "title_en": "The Church as Family",
        "desc": "以属灵家庭的视角探索教会：爱与接纳、属灵成长、规劝挽回与接纳新成员。",
        "en_file": "family_matters/extracted_en/00_Introduction.md",
        "zh_file": "family_matters/translations_zh/00_Introduction.md",
    },
    {
        "id": "chap-01",
        "art_code": "01",
        "num_label": "01",
        "part": "第一部分：家族的根基",
        "part_en": "Part One: Roots of the Family",
        "title_zh": "第一章：重洗派宗教改革",
        "title_en": "Chapter 1: The Anabaptist Reformation",
        "desc": "早期教会、君士坦丁转变、1525年苏黎世信徒再洗礼、施莱特海姆信仰宣言与门诺·西蒙斯。",
        "en_file": "family_matters/extracted_en/01_Chapter_01.md",
        "zh_file": "family_matters/translations_zh/01_Chapter_01.md",
    },
    {
        "id": "chap-02",
        "art_code": "02",
        "num_label": "02",
        "part": "第一部分：家族的根基",
        "part_en": "Part One: Roots of the Family",
        "title_zh": "第二章：“弟兄会”的诞生",
        "title_en": "Chapter 2: Birth of \"the Brotherhood\"",
        "desc": "普鲁士迁徙至沙俄、小聚会派、爱德华·维斯特（Eduard Wuest）与敬虔派复兴、1860年分裂文书与弟兄会破土而出。",
        "en_file": "family_matters/extracted_en/02_Chapter_02.md",
        "zh_file": "family_matters/translations_zh/02_Chapter_02.md",
    },
    {
        "id": "chap-03",
        "art_code": "03",
        "num_label": "03",
        "part": "第一部分：家族的根基",
        "part_en": "Part One: Roots of the Family",
        "title_zh": "第三章：门诺弟兄会的成长",
        "title_en": "Chapter 3: The MB Church Grows",
        "desc": "1865年六月改革、1874-80年代北美移民大潮、俄国黄金时代、十月革命浩劫与MCC创立援助。",
        "en_file": "family_matters/extracted_en/03_Chapter_03.md",
        "zh_file": "family_matters/translations_zh/03_Chapter_03.md",
    },
    {
        "id": "chap-04",
        "art_code": "04",
        "num_label": "04",
        "part": "第二部分：家族的特质",
        "part_en": "Part Two: Characteristics of the Family",
        "title_zh": "第四章：圣道之民",
        "title_en": "Chapter 4: People of the Word",
        "desc": "圣经是上帝无误的启示；基督中心正典观；共同体释经学与山上宝训的核心指引。",
        "en_file": "family_matters/extracted_en/04_Chapter_04.md",
        "zh_file": "family_matters/translations_zh/04_Chapter_04.md",
    },
    {
        "id": "chap-05",
        "art_code": "05",
        "num_label": "05",
        "part": "第二部分：家族的特质",
        "part_en": "Part Two: Characteristics of the Family",
        "title_zh": "第五章：新约教会",
        "title_en": "Chapter 5: The New Testament Church",
        "desc": "家庭式的相通交接、救赎性教会纪律、信徒浸礼、主餐圣餐与洗脚礼仪、平信徒恩赐配搭。",
        "en_file": "family_matters/extracted_en/05_Chapter_05.md",
        "zh_file": "family_matters/translations_zh/05_Chapter_05.md",
    },
    {
        "id": "chap-06",
        "art_code": "06",
        "num_label": "06",
        "part": "第二部分：家族的特质",
        "part_en": "Part Two: Characteristics of the Family",
        "title_zh": "第六章：缔造和平",
        "title_en": "Chapter 6: Peacemaking",
        "desc": "迪克·威廉斯（Dirk Willems）舍己救追捕者；华特·温克的第三条路；信仰宣言第13条修订；良心拒服兵役与和平见证。",
        "en_file": "family_matters/extracted_en/06_Chapter_06.md",
        "zh_file": "family_matters/translations_zh/06_Chapter_06.md",
    },
    {
        "id": "chap-07",
        "art_code": "07",
        "num_label": "07",
        "part": "第二部分：家族的特质",
        "part_en": "Part Two: Characteristics of the Family",
        "title_zh": "第七章：门徒即宣教士",
        "title_en": "Chapter 7: Disciples are Missionaries",
        "desc": "救恩与悔改归正；喀麦隆与印度宣教先驱；本土化自立宣教；Multiply（全球宣教差会）全人福音。",
        "en_file": "family_matters/extracted_en/07_Chapter_07.md",
        "zh_file": "family_matters/translations_zh/07_Chapter_07.md",
    },
    {
        "id": "chap-08",
        "art_code": "08",
        "num_label": "08",
        "part": "第三部分：茁壮成长的家庭",
        "part_en": "Part Three: A Growing Family",
        "title_zh": "第八章：齐心同工",
        "title_en": "Chapter 8: Working Together",
        "desc": "北美总会123年历程与2002年体面移交；历史委员会；泰博学院与弗雷斯诺大学；门诺弟兄会基金会。",
        "en_file": "family_matters/extracted_en/08_Chapter_08.md",
        "zh_file": "family_matters/translations_zh/08_Chapter_08.md",
    },
    {
        "id": "chap-09",
        "art_code": "09",
        "num_label": "09",
        "part": "第三部分：茁壮成长的家庭",
        "part_en": "Part Three: A Growing Family",
        "title_zh": "第九章：美国的门诺弟兄会",
        "title_en": "Chapter 9: Mennonite Brethren in the U.S.",
        "desc": "USMB 治理架构变革；三大核心委身（植堂布道、刻意门徒、领袖培育）；五大区会版图；基督徒领袖会刊。",
        "en_file": "family_matters/extracted_en/09_Chapter_09.md",
        "zh_file": "family_matters/translations_zh/09_Chapter_09.md",
    },
    {
        "id": "chap-10",
        "art_code": "10",
        "num_label": "10",
        "part": "第三部分：茁壮成长的家庭",
        "part_en": "Part Three: A Growing Family",
        "title_zh": "第十章：门诺弟兄会国际大家庭",
        "title_en": "Chapter 10: The International MB Family (ICOMB)",
        "desc": "ICOMB 国际信仰宣言五大支柱；巡礼非、亚、欧、拉美与北美全球22个国家总会及新兴宣教前线。",
        "en_file": "family_matters/extracted_en/10_Chapter_10.md",
        "zh_file": "family_matters/translations_zh/10_Chapter_10.md",
    },
    {
        "id": "chap-11",
        "art_code": "11",
        "num_label": "11",
        "part": "第三部分：茁壮成长的家庭",
        "part_en": "Part Three: A Growing Family",
        "title_zh": "第十一章：门诺会各支派间的合作纽带",
        "title_en": "Chapter 11: Inter-Mennonite Connections",
        "desc": "“奉基督的名”——MCC百年人道救济；MDS灾难急先锋；MWC门诺会世界大会全球两百余万信徒同心合一。",
        "en_file": "family_matters/extracted_en/11_Chapter_11.md",
        "zh_file": "family_matters/translations_zh/11_Chapter_11.md",
    },
    {
        "id": "chap-12",
        "art_code": "12",
        "num_label": "12",
        "part": "第四部分：面向未来的家庭纽带",
        "part_en": "Part Four: Family Ties for the Future",
        "title_zh": "第十二章：未来的挑战",
        "title_en": "Chapter 12: The Challenge for the Future",
        "desc": "后现代语境下的终极叙事；颠倒天国仆人领导力；窄路门徒生命；门诺·西蒙斯基督唯一根基祝祷。",
        "en_file": "family_matters/extracted_en/12_Chapter_12.md",
        "zh_file": "family_matters/translations_zh/12_Chapter_12.md",
    },
    {
        "id": "chap-biblio",
        "art_code": "biblio",
        "num_label": "附录",
        "part": "文献索引与书目",
        "part_en": "Bibliography",
        "title_zh": "附录：推荐阅读与引用书目",
        "title_en": "Appendix: Recommended Reading & Works Cited",
        "desc": "经典重洗派神学专著、门诺弟兄会历史通史文献及各章引述一手资料详注。",
        "en_file": "family_matters/extracted_en/13_Bibliography.md",
        "zh_file": "family_matters/translations_zh/13_Bibliography.md",
    }
]

def clean_en(text, ch_name):
    # Remove junk headers in Front Matter
    text = re.sub(r'###\s+FamilyMattersDISCOVERING THE MENN\s*', '', text)
    text = re.sub(r'###\s+DISCOVERING THE MENN\s*', '', text)
    
    # Restore glued headings across various chapters
    if ch_name == '00_Front_Matter':
        text = re.sub(r'\bChapter 9: Mennonite Brethren in the U.S\.\s*', r'\n\n### Chapter 9: Mennonite Brethren in the U.S.\n\n', text)
        text = re.sub(r'(\d+)\s+PART ONE', r'\1\n\n### PART ONE', text)
    elif ch_name == '01_Chapter_01':
        text = re.sub(r'\bRadical Reformation Through his visionary', '### Radical Reformation\n\nThrough his visionary', text)
    elif ch_name == '02_Chapter_02':
        text = re.sub(r'\bBirth of the Mennonite Brethren Many people had been', '### Birth of the Mennonite Brethren\n\nMany people had been', text)
        text = re.sub(r'\bReaction of the Mennonite Colony Administration The Mennonite church', '### Reaction of the Mennonite Colony Administration\n\nThe Mennonite church', text)
    elif ch_name == '04_Chapter_04':
        text = re.sub(r'(Commitment to studying and obeying the Word of God is at the core)', r'### Evangelical Pietist Influences\n\n\1', text)
        text = re.sub(r'\bThe Anabaptist Interpretation of Scripture Mennonite Brethren recognize', '### The Anabaptist Interpretation of Scripture\n\nMennonite Brethren recognize', text)
        text = re.sub(r'\bMB Principles of Interpretation The MB Confession of Faith recognizes', '### MB Principles of Interpretation\n\nThe MB Confession of Faith recognizes', text)
        text = re.sub(r'\b1\.\s+(“We believe that the entire Bible was inspired)', r'### Principle 1: Infallible Word of God\n\n\1', text)
        text = re.sub(r'\b2\.\s+We believe that “(the same Spirit guides the community of faith)', r'### Principle 2: Community Discernment\n\n“\1', text)
        text = re.sub(r'(Jesus’ person, life and teaching reveal God, and thus Jesus is the lens)', r'### Principle 3: Christ-Centered Lens\n\n\1', text)
    elif ch_name == '05_Chapter_05':
        text = re.sub(r'\bGrowing the Family The New Testament teaches', '### Growing the Family\n\nThe New Testament teaches', text)
        text = re.sub(r'\bLiving as a Family Every family develops routines', '### Living as a Family\n\nEvery family develops routines', text)
        text = re.sub(r'\bCongregational Polity Mennonite Brethren do not have', '### Congregational Polity\n\nMennonite Brethren do not have', text)
    elif ch_name == '06_Chapter_06':
        text = re.sub(r'(Peacemaking begins with restoring our relationship with God.*?)\s*(This leads us to consider how Mennonite Brethren respond to war\.)', r'\1\n\n### Responding to War & Military Service\n\n\2', text, flags=re.DOTALL)
        text = re.sub(r'Objection 1:\s*Old Testament War and Peace', '### Objection 1: Old Testament War and Peace\n\n', text)
        text = re.sub(r'Objection 2:\s*Can Christians Live in the Way of Peace\?', '### Objection 2: Can Christians Live in the Way of Peace?\n\n', text)
        text = re.sub(r'Objection 3:\s*Does love for the unprotected neighbor permit the use of violent force\?', '### Objection 3: Does love for the unprotected neighbor permit the use of violent force?\n\n', text)
    elif ch_name == '07_Chapter_07':
        text = re.sub(r'(By the 1950s, North American missionaries totaled 279\.)\s*(?:<!-- Page \d+ -->\s*)?(The middle decades of the 20th century)', r'\1\n\n### Transformation & Indigenization\n\n\2', text)
    elif ch_name == '09_Chapter_09':
        text = re.sub(r'\bGovernance and Vision Most families go through', '### Governance and Vision\n\nMost families go through', text)
    elif ch_name == '10_Chapter_10':
        text = re.sub(r'Asia: India, Japan, Khmu Mission and beyond\s+(The Conference of the)', '### Asia: India, Japan, Khmu Mission and beyond\n\n\\1', text)
        text = re.sub(r'### Europe: Austria, Germany, Lithuania, Portugal\s*\n+(?:<!-- Page \d+ -->\s*\n+)?and beyond\s+(After four centuries,)', '### Europe: Austria, Germany, Lithuania, Portugal and beyond\n\n\\1', text)
        text = re.sub(r'### Latin America: Brazil, Colombia, Mexico, Panama,\s*\n+(?:<!-- Page \d+ -->\s*\n+)?Paraguay, Peru, Uruguay and beyond\s+(The Mennonite Brethren)', '### Latin America: Brazil, Colombia, Mexico, Panama, Paraguay, Peru, Uruguay and beyond\n\n\\1', text)
        text = re.sub(r'North America: Canada and the United States\s+(Mennonite Brethren in North America)', '### North America: Canada and the United States\n\n\\1', text)

    # Stitch broken lines across <!-- Page \d+ -->
    def stitch_pages(match):
        p1 = match.group(1).rstrip()
        p2 = match.group(2).lstrip()
        ends_punct = bool(re.search(r'[.!?][\"\'”’]?$', p1))
        starts_lower = bool(re.match(r'^[a-z]', p2))
        starts_heading = p2.startswith('#')
        
        if (not ends_punct or starts_lower) and not starts_heading:
            if p1.endswith('-'):
                return p1[:-1] + p2
            return p1 + ' ' + p2
        else:
            return p1 + '\n\n' + p2

    prev_len = 0
    while len(text) != prev_len:
        prev_len = len(text)
        text = re.sub(r'([^\n]+)\s*\n+\s*<!-- Page \d+ -->\s*\n+([^\n]+)', stitch_pages, text)
        
    text = re.sub(r'\s*<!-- Page \d+ -->\s*', '\n\n', text)
    return text

def clean_zh(text):
    text = text.replace('爱德华·乌斯特', '爱德华·维斯特（Eduard Wuest）')
    text = text.replace('德克·威廉斯', '迪克·威廉斯（Dirk Willems）')
    text = text.replace('加倍宣教部（Multiply）', 'Multiply（全球宣教差会）')
    text = text.replace('加倍宣教部', 'Multiply（全球宣教差会）')
    return text

def split_by_headings(zh, en, zh_regex_list, en_regex_list):
    assert len(zh_regex_list) == len(en_regex_list)
    zh_chunks = []
    en_chunks = []
    
    zh_indices = [0]
    for r in zh_regex_list:
        m = re.search(r, zh)
        if not m: raise ValueError(f"ZH heading not found: {r}")
        zh_indices.append(m.start())
    zh_indices.append(len(zh))
    for i in range(len(zh_indices) - 1):
        zh_chunks.append(zh[zh_indices[i]:zh_indices[i+1]].strip())
        
    en_indices = [0]
    for r in en_regex_list:
        m = re.search(r, en)
        if not m: raise ValueError(f"EN heading not found: {r}")
        en_indices.append(m.start())
    en_indices.append(len(en))
    for i in range(len(en_indices) - 1):
        en_chunks.append(en[en_indices[i]:en_indices[i+1]].strip())
        
    pairs = []
    for zc, ec in zip(zh_chunks, en_chunks):
        if zc or ec:
            pairs.append((zc, ec))
    return pairs

def get_chapter_pairs(item):
    art_id = item["id"]
    with open(item["zh_file"], "r", encoding="utf-8") as f: zh_raw = clean_zh(f.read())
    with open(item["en_file"], "r", encoding="utf-8") as f: en_raw = clean_en(f.read(), os.path.basename(item["en_file"])[:-3])
    
    if art_id == 'chap-front':
        zh0_p1 = zh_raw[:zh_raw.find('#### 版权与出版说明')].strip()
        zh0_p2 = zh_raw[zh_raw.find('#### 版权与出版说明'):zh_raw.find('### 全书总目录')].strip()
        zh0_p3 = zh_raw[zh_raw.find('### 全书总目录'):].strip()
        en0_p1 = en_raw[:en_raw.find('All Scripture quotations unless otherwise indicated')].strip()
        en0_p2 = en_raw[en_raw.find('All Scripture quotations unless otherwise indicated'):en_raw.find('### Introduction\n\n................................................................................... 7')].strip()
        en0_p3 = en_raw[en_raw.find('### Introduction\n\n................................................................................... 7'):].strip()
        return [(zh0_p1, en0_p1), (zh0_p2, en0_p2), (zh0_p3, en0_p3)]

    elif art_id == 'chap-intro':
        zh_split = '然而，在门诺弟兄会的历史叙事中，也许没有任何一种对家庭隐喻的实践，比“寄居者与外人”'
        en_split = 'Perhaps no application of the metaphor is more central to the Mennonite Brethren story'
        zh_in_parts = zh_raw.split(zh_split)
        en_in_parts = en_raw.split(en_split)
        return [
            (zh_in_parts[0].strip(), en_in_parts[0].strip()),
            (('### 寄居者、朝圣者与全书导览 (Strangers, Pilgrims & Book Guide)\n\n' + zh_split + zh_in_parts[1]).strip(),
             ('### Strangers, Pilgrims & Book Guide\n\n' + en_split + en_in_parts[1]).strip())
        ]

    elif art_id == 'chap-01':
        zh_h = [
            r'#### 早期教会 \(Early Church\)',
            r'#### 君士坦丁与大公教会 \(Constantine and Catholicism\)',
            r'#### 宗教改革运动 \(Protestant Reformation\)',
            r'#### 激进宗教改革 \(Radical Reformation\)',
            r'#### 门诺·西蒙斯 \(Menno Simons\)'
        ]
        en_h = [
            r'### Early Church',
            r'### Constantine and Catholicism',
            r'### Protestant Reformation',
            r'### Radical Reformation',
            r'### Menno Simons'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-02':
        zh_h = [
            r'#### 迁徙至波兰与普鲁士 \(Migration to Poland\)',
            r'#### 俄国门诺殖民地 \(Mennonite Colonies in Russia\)',
            r'#### 敬虔复兴运动 \(Revival Movements\)',
            r'#### 门诺弟兄会的诞生 \(Birth of the Mennonite Brethren\)',
            r'#### 殖民地管理阶层的反应 \(Reaction of the Mennonite Colony Administration\)'
        ]
        en_h = [
            r'### Migration to Poland',
            r'### Mennonite Colonies in Russia',
            r'### Revival Movements',
            r'### Birth of the Mennonite Brethren',
            r'### Reaction of the Mennonite Colony Administration'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-03':
        zh_h = [
            r'#### 初期的挑战（1860–1865） \(Early Challenges\)',
            r'#### 首次向北美的移民潮 \(The First Migration to North America\)',
            r'#### 俄国革命与后续的移民 \(The Russian Revolution and Later Migrations\)',
            r'#### 动荡年代、世界大战与全球大迁徙 \(Revolution, World Wars and Migrations\)'
        ]
        en_h = [
            r'### Early Challenges \(1860-65\)',
            r'### The First Migration to North America',
            r'### The Russian Revolution and Later Migrations',
            r'### Revolution, World Wars and Migrations'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-04':
        zh_h = [
            r'#### 福音派与敬虔主义的影响 \(Evangelical Pietist Influences\)',
            r'#### 重洗派对圣经的诠释 \(The Anabaptist Interpretation of Scripture\)',
            r'#### 门诺弟兄会的圣经诠释原则 \(MB Principles of Interpretation\)',
            r'##### 原则一：圣经是上帝完全可靠的话语，是信仰与生活的权威指南',
            r'##### 原则二：圣灵亲自引导信仰共同体共同辨识并诠释圣经',
            r'##### 原则三：耶稣基督是诠释整本圣经的核心透镜与最高峰'
        ]
        en_h = [
            r'### Evangelical Pietist Influences',
            r'### The Anabaptist Interpretation of Scripture',
            r'### MB Principles of Interpretation',
            r'### Principle 1: Infallible Word of God',
            r'### Principle 2: Community Discernment',
            r'### Principle 3: Christ-Centered Lens'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-05':
        zh_h = [
            r'#### 家庭的扩增：全人宣教与生命重生 \(Growing the Family\)',
            r'#### 救赎性的教会纪律 \(Redemptive Discipline\)',
            r'#### 洗礼与主的晚餐：两项神圣记号',
            r'#### 主的晚餐 \(The Lord’s Supper\)',
            r'#### 过肢体相爱的家庭生活：恩赐与作门徒 \(Living as a Family\)',
            r'#### 会众治理体制与跨堂会联会架构 \(Congregational Polity\)'
        ]
        en_h = [
            r'### Growing the Family',
            r'### Redemptive Discipline',
            r'### Baptism',
            r'### The Lord’s Supper',
            r'### Living as a Family',
            r'### Congregational Polity'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-06':
        zh_h = [
            r'#### 第三千禧年的和平缔造者 \(Third Millennium Peacemakers\)',
            r'#### 面对战争与国家军役的神圣抉择 \(Responding to War & Military Service\)',
            r'#### 面对“积极缔造和平”的三大严峻质疑与神圣回应',
            r'##### 质疑二的神圣回应：和平之道在现实中能行得通吗？',
            r'##### 质疑三的神圣回应：以暴力保护无辜邻舍是爱的体现吗？',
            r'#### 教会与国家政权 \(Church and State\)'
        ]
        en_h = [
            r'### Third Millennium Peacemakers',
            r'### Responding to War & Military Service',
            r'### Objection 1: Old Testament War and Peace',
            r'### Objection 2: Can Christians Live in the Way of Peace\?',
            r'### Objection 3: Does love for the unprotected neighbor permit the use of violent force\?',
            r'### Church and State'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-07':
        zh_h = [
            r'#### 成为门徒：归信、悔改与终生救恩 \(Becoming a Disciple\)',
            r'#### 全球宣教的悲壮与荣耀历程 \(Global Mission\)',
            r'#### 本土化浪潮、伙伴关系与 Multiply 的诞生 \(Transformation & Indigenization\)',
            r'#### 当代宣教的前沿实践与战略反思 \(Contemporary Mission Work\)'
        ]
        en_h = [
            r'### Becoming a Disciple',
            r'### Global Mission',
            r'### Transformation & Indigenization',
            r'### Contemporary Mission Work'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-08':
        zh_h = [
            r'### 与加拿大的协同事工',
            r'### Multiply（全球宣教差会）'
        ]
        en_h = [
            r'### Ministry with Canada',
            r'### Multiply'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-09':
        zh_h = [
            r'### 治理架构与异象重塑',
            r'### 三大核心委身',
            r'### USMB 的事工运作模式',
            r'### 装备下一代',
            r'### 《基督徒领袖》杂志（Christian Leader）',
            r'### 五大区会（District Conferences）'
        ]
        en_h = [
            r'### Governance and Vision',
            r'### Core Commitments',
            r'### USMB Ministry Model',
            r'### Equipping the Next Generation',
            r'### Christian Leader',
            r'### District Conferences'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-10':
        zh_h = [
            r'### 非洲：安哥拉、刚果民主共和国、马拉维及其他地区',
            r'### 亚洲：印度、日本、克木人差传及其他工场',
            r'### 欧洲：奥地利、德国、立陶宛、葡萄牙及前线见证',
            r'### 拉丁美洲：巴西、哥伦比亚、墨西哥、巴拿马、巴拉圭、秘鲁、乌拉圭及其他地区',
            r'### 北美洲：加拿大与美国'
        ]
        en_h = [
            r'### Africa: Angola, DR Congo, Malawi and beyond',
            r'### Asia: India, Japan, Khmu Mission and beyond',
            r'### Europe: Austria, Germany, Lithuania, Portugal and beyond',
            r'### Latin America: Brazil, Colombia, Mexico, Panama, Paraguay, Peru, Uruguay and beyond',
            r'### North America: Canada and the United States'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-11':
        zh_h = [
            r'### 携手服事众人',
            r'### 门诺会中央委员会（MCC）步入百年华诞',
            r'### 门诺灾难服侍处（MDS）：北美救灾急先锋',
            r'### 门诺会世界大会（MWC）：同一个信仰大家庭',
            r'### 全球重洗派信徒版图与会友统计',
            r'### 跨门诺派联合机构权威指南'
        ]
        en_h = [
            r'### Working Together to Serve Others',
            r'### MCC Turns 100',
            r'### MDS: North American Disaster Response',
            r'### MWC: A Family of Faith',
            r'### Worldwide Membership',
            r'### Guide to Inter-Mennonite Agencies'
        ]
        return split_by_headings(zh_raw, en_raw, zh_h, en_h)

    elif art_id == 'chap-12':
        zh12_split = '三十多年前，'
        en12_split = 'More than 30 years ago theologian Howard Loewen outlined'
        zh12_p = zh_raw.split(zh12_split)
        en12_p = en_raw.split(en12_split)
        return [
            (zh12_p[0].strip(), en12_p[0].strip()),
            (('### 信仰纽带前瞻与基督根基祝祷 (Loewen’s Vision & Benediction)\n\n三十多年前，' + zh12_p[1]).strip(),
             ('### Loewen’s Vision & Benediction\n\n' + en12_split + en12_p[1]).strip())
        ]

    elif art_id == 'chap-biblio':
        zh13_h = [
            r'#### 引言',
            r'#### 第一章',
            r'#### 第三章',
            r'#### 第四章',
            r'#### 第六章',
            r'#### 第七章',
            r'#### 第八章与第九章',
            r'#### 第十章',
            r'#### 第十一章',
            r'#### 第十二章'
        ]
        en13_h = [
            r'### Introduction',
            r'### Chapter 1',
            r'### Chapter 3',
            r'### Chapter 4',
            r'### Chapter 6',
            r'### Chapter 7',
            r'### Chapters 8 & 9',
            r'### Chapter 10',
            r'### Chapter 11',
            r'### Chapter 12'
        ]
        return split_by_headings(zh_raw, en_raw, zh13_h, en13_h)

    raise ValueError(f"Unknown article id: {art_id}")

def markdown_to_html(md_text, lang='zh'):
    subheading_cls = f"{lang}-subheading"
    minorheading_cls = f"{lang}-minor-heading"
    
    lines = md_text.split('\n')
    output = []
    
    in_ul = False
    in_ol = False
    in_bq = False
    in_table = False
    table_rows = []
    
    def close_blocks():
        nonlocal in_ul, in_ol, in_bq, in_table, table_rows
        res = []
        if in_ul:
            res.append('</ul>')
            in_ul = False
        if in_ol:
            res.append('</ol>')
            in_ol = False
        if in_bq:
            res.append('</blockquote>')
            in_bq = False
        if in_table:
            res.append(render_table(table_rows))
            in_table = False
            table_rows = []
        return res

    def render_table(rows):
        if not rows:
            return ""
        html_out = ['<div class="table-responsive"><table class="styled-table">']
        headers = [c.strip() for c in rows[0].split('|')[1:-1]]
        html_out.append('<thead><tr>' + ''.join(f'<th>{inline_format(h)}</th>' for h in headers) + '</tr></thead>')
        html_out.append('<tbody>')
        for r in rows[2:]:
            cols = [c.strip() for c in r.split('|')[1:-1]]
            html_out.append('<tr>' + ''.join(f'<td>{inline_format(c)}</td>' for c in cols) + '</tr>')
        html_out.append('</tbody></table></div>')
        return '\n'.join(html_out)

    def inline_format(text):
        text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text

    for line in lines:
        raw = line.strip()
        
        if raw.startswith('<!-- Page'):
            continue
        if raw in ['---', '***', '___']:
            output.extend(close_blocks())
            output.append('<hr class="content-divider">')
            continue
            
        if not raw:
            output.extend(close_blocks())
            continue
            
        if raw.startswith('|') and raw.endswith('|'):
            if not in_table:
                output.extend(close_blocks())
                in_table = True
                table_rows = []
            table_rows.append(raw)
            continue
        elif in_table:
            output.extend(close_blocks())
            
        if raw.startswith('>'):
            if not in_bq:
                output.extend(close_blocks())
                output.append('<blockquote>')
                in_bq = True
            bq_text = raw[1:].strip()
            output.append(f'<p>{inline_format(bq_text)}</p>')
            continue
        elif in_bq:
            output.extend(close_blocks())

        if raw.startswith('#'):
            output.extend(close_blocks())
            m = re.match(r'^(#{1,6})\s+(.*)$', raw)
            if m:
                level = len(m.group(1))
                h_text = inline_format(m.group(2))
                if level == 1:
                    continue
                elif level == 2 or level == 3:
                    output.append(f'<h3 class="{subheading_cls}">{h_text}</h3>')
                else:
                    output.append(f'<h4 class="{minorheading_cls}">{h_text}</h4>')
                continue
                
        if raw.startswith(('- ', '* ')):
            if not in_ul:
                output.extend(close_blocks())
                output.append('<ul>')
                in_ul = True
            item_text = inline_format(raw[2:].strip())
            output.append(f'<li>{item_text}</li>')
            continue
        elif in_ul:
            output.extend(close_blocks())

        m_ol = re.match(r'^(\d+)\.\s+(.*)$', raw)
        if m_ol:
            if not in_ol:
                output.extend(close_blocks())
                output.append('<ol>')
                in_ol = True
            item_text = inline_format(m_ol.group(2).strip())
            output.append(f'<li>{item_text}</li>')
            continue
        elif in_ol:
            output.extend(close_blocks())
            
        output.append(f'<p>{inline_format(raw)}</p>')
        
    output.extend(close_blocks())
    return '\n'.join(output)


def build_full_html():
    # 1. Generate Sidebar Nav items
    sidebar_items_html = []
    current_part = None
    for item in CHAPTER_DEFS:
        if item["part"] != current_part:
            current_part = item["part"]
            sidebar_items_html.append(f'<li class="nav-part-header">{current_part}</li>')
        
        sidebar_items_html.append(f'''
    <li class="nav-item" data-art="{item["art_code"]}">
      <a href="#{item["id"]}" class="nav-link">
        <span class="nav-num">{item["num_label"]}</span>
        <div class="nav-link-content">
          <div class="nav-title">{html.escape(item["title_zh"])}</div>
          <div class="nav-en">{html.escape(item["title_en"])}</div>
        </div>
      </a>
    </li>''')

    # 2. Generate Grid Directory cards
    grid_cards_html = []
    for item in CHAPTER_DEFS:
        grid_cards_html.append(f'''
        <a href="#{item["id"]}" class="grid-card">
          <div class="grid-card-num">{item["part_en"]} · {item["num_label"]}</div>
          <div class="grid-card-title">{html.escape(item["title_zh"])}</div>
          <div class="grid-card-en">{html.escape(item["title_en"])}</div>
          <div class="grid-card-desc">{html.escape(item["desc"])}</div>
        </a>''')

    # 3. Generate Chapter Articles
    articles_html = []
    total_chaps = len(CHAPTER_DEFS)
    for idx, item in enumerate(CHAPTER_DEFS):
        prev_item = CHAPTER_DEFS[idx - 1] if idx > 0 else None
        next_item = CHAPTER_DEFS[idx + 1] if idx < total_chaps - 1 else None

        pairs = get_chapter_pairs(item)
        rows_parts = []
        rows_parts.append('''
        <div class="bilingual-row row-tags">
          <div class="row-cell cell-zh"><span class="col-lang-tag tag-zh">🇨🇳 中文译文 · 信仰与生活委员会核定</span></div>
          <div class="row-cell cell-en"><span class="col-lang-tag tag-en">🇬🇧 English Original Text</span></div>
        </div>''')

        for zh_chunk, en_chunk in pairs:
            zh_rendered = markdown_to_html(zh_chunk, lang='zh')
            en_rendered = markdown_to_html(en_chunk, lang='en')
            rows_parts.append(f'''
        <div class="bilingual-row">
          <div class="row-cell cell-zh">
            {zh_rendered}
          </div>
          <div class="row-cell cell-en">
            {en_rendered}
          </div>
        </div>''')

        prev_btn = f'<a href="#{prev_item["id"]}" class="art-nav-btn">← 上一章：{html.escape(prev_item["title_zh"])}</a>' if prev_item else '<span class="art-nav-disabled">已是第一章</span>'
        next_btn = f'<a href="#{next_item["id"]}" class="art-nav-btn">下一章：{html.escape(next_item["title_zh"])} →</a>' if next_item else '<a href="#cover" class="art-nav-btn">返回全书顶部 ⇡</a>'

        article_block = f'''
    <!-- ARTICLE: {item["title_zh"]} -->
    <article id="{item["id"]}" class="article-section" data-art="{item["art_code"]}">
      <nav class="article-top-nav">
        <a href="index.html" class="article-back-home">🏠 首页</a>
        <span class="article-nav-sep">/</span>
        <a href="#cover" class="article-nav-crumb">属灵家事</a>
        <span class="article-nav-sep">/</span>
        <span class="article-nav-crumb">{html.escape(item["part"])}</span>
        <span class="article-nav-sep">/</span>
        <span class="article-nav-crumb" style="font-weight: 600; color: var(--apple-blue);">{html.escape(item["title_zh"])}</span>
      </nav>

      <div class="article-header-wrapper">
        <div class="article-badge-row">
          <span class="article-badge">{item["num_label"]} · {html.escape(item["part"])}</span>
          <span class="article-badge-sub">{html.escape(item["part_en"])}</span>
        </div>
        <div class="bilingual-header-grid">
          <div class="header-zh">
            <h2 class="article-title">{html.escape(item["title_zh"])}</h2>
          </div>
          <div class="header-en">
            <h2 class="article-title-en">{html.escape(item["title_en"])}</h2>
          </div>
        </div>
      </div>

      <div class="bilingual-rows-wrapper">
        {''.join(rows_parts)}
      </div>

      <div class="article-footer-nav">
        <div class="article-footer-left">
          <a href="index.html" class="art-nav-btn art-home-action">🏠 返回 Evan's Thinking 首页</a>
        </div>
        <div class="article-footer-right">
          {prev_btn}
          <a href="#cover" class="art-nav-btn">⇡ 回顶部</a>
          {next_btn}
        </div>
      </div>
    </article>
'''
        articles_html.append(article_block)

    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>《属灵家事：走近门诺弟兄会》（中英双语典藏全集）- Family Matters: Discovering the Mennonite Brethren</title>
<meta name="description" content="《属灵家事：走近门诺弟兄会》（美国修订版，Family Matters: Discovering the Mennonite Brethren）中英双语对照权威典藏全集。收录全书12章历史、神学、教会治理与差传全貌。">
<style>
  :root {{
    /* Apple SF System Colors */
    --apple-blue: #0071E3;
    --apple-blue-hover: #0077ED;
    --apple-blue-subtle: rgba(0, 113, 227, 0.08);
    --apple-purple: #AF52DE;
    --apple-purple-subtle: rgba(175, 82, 222, 0.08);
    --apple-teal: #00C7BE;
    --apple-teal-subtle: rgba(0, 199, 190, 0.08);
    --apple-gray: #86868B;
    --apple-gray-light: #F5F5F7;
    
    /* Semantic Theme Tokens - Light Mode */
    --bg-canvas: #F5F5F7;
    --bg-card: #FFFFFF;
    --bg-card-subtle: #F0F2F2;
    --text-primary: #313938;
    --text-secondary: #555E5D;
    --border-color: #E5E7E6;
    --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    
    --accent-gold: #F4BA19;
    --accent-gold-subtle: rgba(244, 186, 25, 0.15);
    --accent-gold-border: rgba(244, 186, 25, 0.35);
    
    /* macOS Frosted Sidebar */
    --bg-sidebar: rgba(250, 249, 246, 0.94);
    --sidebar-text: #18181B;
    --sidebar-text-muted: #71717A;
    --sidebar-border: rgba(0, 0, 0, 0.07);
    --sidebar-width: 320px;
    
    /* Typography */
    --font-apple: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    --font-apple-display: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", "Hiragino Sans GB", sans-serif;
    --font-serif: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", "Hiragino Sans GB", sans-serif;
    --font-en: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
    --reader-fs-zh: 16.5px;
    --reader-lh-zh: 1.9;
    --reader-fs-en: 15.5px;
    --reader-lh-en: 1.8;
  }}

  /* Dark Mode (Apple Pro OLED & Titanium) */
  body.theme-dark {{
    --bg-canvas: #000000;
    --bg-card: #1C1C1E;
    --bg-card-subtle: #2C2C2E;
    --text-primary: #F5F5F7;
    --text-secondary: #98989D;
    --border-color: rgba(255, 255, 255, 0.12);
    --card-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    
    --bg-sidebar: rgba(28, 28, 30, 0.9);
    --sidebar-text: #F5F5F7;
    --sidebar-text-muted: #98989D;
    --sidebar-border: rgba(255, 255, 255, 0.1);
    
    --apple-blue: #2997FF;
    --apple-blue-subtle: rgba(41, 151, 255, 0.15);
  }}

  /* Sepia Mode (Apple Books Paper Reading Theme) */
  body.theme-sepia {{
    --bg-canvas: #FAF4E8;
    --bg-card: #F4ECDF;
    --bg-card-subtle: #EDE3D4;
    --text-primary: #383127;
    --text-secondary: #7E7060;
    --border-color: rgba(126, 112, 96, 0.15);
    --card-shadow: 0 4px 20px rgba(126, 112, 96, 0.08);
    
    --bg-sidebar: rgba(244, 236, 223, 0.94);
    --sidebar-text: #383127;
    --sidebar-text-muted: #7E7060;
    --sidebar-border: rgba(126, 112, 96, 0.15);
    
    --apple-blue: #8E5A2D;
    --apple-blue-subtle: rgba(142, 90, 45, 0.12);
  }}

  * {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
  html {{ scroll-behavior: smooth; font-size: 16px; }}

  body {{
    font-family: var(--font-apple);
    background-color: var(--bg-canvas);
    color: var(--text-primary);
    line-height: 1.8;
    margin: 0;
    padding: 0;
    display: flex;
    transition: background-color 0.3s ease, color 0.3s ease;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }}

  /* Apple iOS/macOS Smooth Scrollbars */
  ::-webkit-scrollbar {{
    width: 8px;
    height: 8px;
  }}
  ::-webkit-scrollbar-track {{
    background: transparent;
  }}
  ::-webkit-scrollbar-thumb {{
    background: rgba(0, 0, 0, 0.18);
    border-radius: 9999px;
    border: 2px solid transparent;
    background-clip: content-box;
  }}
  ::-webkit-scrollbar-thumb:hover {{
    background: rgba(0, 0, 0, 0.35);
  }}
  body.theme-dark ::-webkit-scrollbar-thumb {{
    background: rgba(255, 255, 255, 0.2);
  }}

  /* Top Progress Bar */
  #progress-bar {{
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, #0071E3, #AF52DE, #00C7BE);
    width: 0%;
    z-index: 1001;
    transition: width 0.1s ease-out;
  }}

  /* macOS Frosted Sidebar */
  #sidebar {{
    width: var(--sidebar-width);
    height: 100vh;
    background: var(--bg-sidebar);
    backdrop-filter: blur(25px) saturate(180%);
    -webkit-backdrop-filter: blur(25px) saturate(180%);
    color: var(--sidebar-text);
    position: fixed;
    top: 0;
    left: 0;
    overflow-y: auto;
    padding: 20px 14px 80px 14px;
    z-index: 100;
    border-right: 1px solid var(--sidebar-border);
    box-shadow: 2px 0 20px rgba(0,0,0,0.03);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  #sidebar.collapsed {{
    transform: translateX(-100%);
  }}

  /* macOS Traffic Light Window Controls */
  .mac-window-controls {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 18px;
    padding-left: 2px;
  }}
  .mac-dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
    cursor: pointer;
    transition: transform 0.15s ease, opacity 0.15s ease;
  }}
  .mac-dot:hover {{
    transform: scale(1.15);
  }}
  .mac-close {{ background: #FF5F56; border: 0.5px solid rgba(0,0,0,0.15); }}
  .mac-minimize {{ background: #FFBD2E; border: 0.5px solid rgba(0,0,0,0.15); }}
  .mac-maximize {{ background: #27C93F; border: 0.5px solid rgba(0,0,0,0.15); }}
  .mac-window-title {{
    font-size: 11.5px;
    font-weight: 600;
    color: var(--sidebar-text-muted);
    margin-left: 6px;
    letter-spacing: -0.01em;
  }}

  .sidebar-header {{
    padding-bottom: 14px;
    border-bottom: 1px solid var(--sidebar-border);
    margin-bottom: 14px;
  }}
  .sidebar-badge {{
    font-size: 11px;
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    padding: 2px 8px;
    border-radius: 9999px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 6px;
    letter-spacing: 0.02em;
  }}
  .sidebar-title {{
    font-size: 16px;
    font-weight: 700;
    color: var(--sidebar-text);
    margin: 0 0 4px 0;
    letter-spacing: -0.015em;
    line-height: 1.35;
  }}
  .sidebar-subtitle {{
    font-size: 11.5px;
    color: var(--sidebar-text-muted);
    margin: 0;
  }}

  .search-box {{
    margin-bottom: 14px;
  }}
  .search-input {{
    width: 100%;
    padding: 8px 12px;
    background: rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(0, 0, 0, 0.04);
    border-radius: 10px;
    color: var(--sidebar-text);
    font-size: 13px;
    font-family: var(--font-apple);
    outline: none;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .search-input:focus {{
    background: var(--bg-card);
    border-color: var(--apple-blue);
    box-shadow: 0 0 0 3px var(--apple-blue-subtle);
  }}
  body.theme-dark .search-input {{
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.1);
  }}

  /* Sidebar Portal Links */
  .sidebar-portal-nav {{
    margin-bottom: 14px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--sidebar-border);
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .sidebar-portal-btn {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 12px;
    border-radius: 10px;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--apple-blue);
    background: var(--apple-blue-subtle);
    border: 1px solid rgba(0, 113, 227, 0.15);
    text-decoration: none;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .sidebar-portal-btn:hover {{
    background: var(--apple-blue);
    color: #FFFFFF;
    box-shadow: 0 4px 12px rgba(0, 113, 227, 0.25);
    transform: translateY(-1px);
  }}
  .portal-btn-arrow {{
    font-size: 13px;
    transition: transform 0.2s ease;
  }}
  .sidebar-portal-btn:hover .portal-btn-arrow {{
    transform: translateX(3px);
  }}

  /* Sidebar Mobile Header Bar */
  .sidebar-top-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .sidebar-mobile-close {{
    display: none;
    background: rgba(0, 0, 0, 0.08);
    border: none;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    color: var(--text-primary);
    font-size: 13px;
    cursor: pointer;
    align-items: center;
    justify-content: center;
  }}
  body.theme-dark .sidebar-mobile-close {{
    background: rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
  }}

  /* Mobile Sidebar Backdrop */
  .sidebar-backdrop {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.38);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 99;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
  }}
  .sidebar-backdrop.active {{
    display: block;
    opacity: 1;
    pointer-events: auto;
  }}

  /* Navigation List */
  .nav-list {{
    list-style: none;
    padding: 0;
    margin: 0;
  }}
  .nav-part-header {{
    font-size: 11px;
    font-weight: 700;
    color: var(--sidebar-text-muted);
    padding: 12px 10px 4px 10px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .nav-item {{
    margin-bottom: 4px;
    border-radius: 10px;
    padding: 7px 10px;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .nav-item:hover {{
    background: rgba(0, 0, 0, 0.04);
  }}
  body.theme-dark .nav-item:hover {{
    background: rgba(255, 255, 255, 0.06);
  }}
  .nav-item.active {{
    background: var(--apple-blue);
    box-shadow: 0 2px 10px rgba(0, 113, 227, 0.25);
  }}
  .nav-item.active .nav-title,
  .nav-item.active .nav-en,
  .nav-item.active .nav-num {{
    color: #FFFFFF !important;
  }}
  .nav-link {{
    display: flex;
    align-items: center;
    color: var(--sidebar-text);
    text-decoration: none;
    gap: 10px;
  }}
  .nav-num {{
    background: rgba(0, 0, 0, 0.05);
    color: var(--sidebar-text-muted);
    font-size: 11px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 9999px;
    min-width: 26px;
    text-align: center;
  }}
  body.theme-dark .nav-num {{
    background: rgba(255, 255, 255, 0.08);
  }}
  .nav-item.active .nav-num {{
    background: rgba(255, 255, 255, 0.25);
    color: #FFFFFF;
  }}
  .nav-link-content {{
    flex: 1;
    min-width: 0;
  }}
  .nav-title {{
    font-size: 13.5px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    letter-spacing: -0.01em;
  }}
  .nav-en {{
    font-size: 11px;
    color: var(--sidebar-text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  /* Main Content Canvas */
  #main-content {{
    margin-left: var(--sidebar-width);
    flex: 1;
    max-width: 1540px;
    padding: 40px 48px 120px 48px;
    min-height: 100vh;
    transition: margin-left 0.35s cubic-bezier(0.16, 1, 0.3, 1), max-width 0.35s ease;
  }}
  #main-content.expanded {{
    margin-left: 0;
    max-width: 1600px;
    margin-right: auto;
    margin-left: auto;
  }}
  body.view-zh-only #main-content,
  body.view-en-only #main-content {{
    max-width: 980px;
  }}

  /* Top Floating Capsule Toolbar */
  .top-toolbar {{
    position: fixed;
    top: 14px;
    right: 24px;
    display: flex;
    align-items: center;
    gap: 4px;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    padding: 5px 8px;
    border-radius: 9999px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(0, 0, 0, 0.08);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
    transform: translateY(0);
    opacity: 1;
  }}
  body.theme-dark .top-toolbar {{
    background: rgba(30, 30, 32, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);
  }}
  body.theme-sepia .top-toolbar {{
    background: rgba(244, 236, 223, 0.9);
    border: 1px solid rgba(126, 112, 96, 0.2);
  }}
  .top-toolbar.toolbar-hidden {{
    transform: translateY(-160%);
    opacity: 0;
    pointer-events: none;
  }}
  .toolbar-divider {{
    width: 1px;
    height: 16px;
    background: rgba(0, 0, 0, 0.1);
    margin: 0 3px;
  }}
  body.theme-dark .toolbar-divider {{
    background: rgba(255, 255, 255, 0.15);
  }}
  .tool-btn {{
    background: transparent;
    border: none;
    color: var(--text-primary);
    font-size: 12.5px;
    font-weight: 500;
    font-family: var(--font-apple);
    cursor: pointer;
    padding: 6px 11px;
    border-radius: 9999px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    white-space: nowrap !important;
    text-decoration: none;
  }}
  .tool-btn:hover {{
    background: rgba(0, 0, 0, 0.06);
  }}
  body.theme-dark .tool-btn:hover {{
    background: rgba(255, 255, 255, 0.1);
  }}
  .tool-btn.active {{
    background: var(--apple-blue);
    color: #FFFFFF;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(0, 113, 227, 0.3);
  }}

  /* Floating Trigger */
  .toolbar-trigger-btn {{
    position: fixed;
    top: 14px;
    right: 20px;
    z-index: 999;
    background: rgba(0, 0, 0, 0.82);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    color: #FFFFFF;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 9999px;
    padding: 7px 16px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
    display: none;
    align-items: center;
    gap: 6px;
  }}
  .toolbar-trigger-btn.trigger-visible {{
    display: flex;
  }}
  .toolbar-trigger-btn:hover {{
    background: var(--apple-blue);
  }}
  .trigger-dot {{
    width: 6px;
    height: 6px;
    background: #34C759;
    border-radius: 50%;
    display: inline-block;
  }}

  /* Cover Banner Card */
  .cover-card {{
    background: transparent;
    color: var(--text-primary);
    padding: 30px 0 44px 0;
    margin-bottom: 40px;
    border-bottom: 1px solid var(--border-color);
  }}
  .cover-layout {{
    display: flex;
    align-items: flex-start;
    gap: 40px;
  }}
  .cover-img-col {{
    flex-shrink: 0;
    width: 220px;
  }}
  .cover-img {{
    width: 100%;
    border-radius: 14px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.16);
    border: 1px solid rgba(0, 0, 0, 0.08);
  }}
  .cover-info-col {{
    flex: 1;
    min-width: 0;
  }}
  .cover-badge {{
    display: inline-block;
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    border: 1px solid rgba(0, 113, 227, 0.2);
    font-size: 11.5px;
    font-weight: 600;
    padding: 4px 14px;
    border-radius: 9999px;
    margin-bottom: 14px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}
  .cover-title {{
    font-family: var(--font-apple-display);
    font-size: 34px;
    font-weight: 700;
    letter-spacing: -0.028em;
    line-height: 1.25;
    margin: 0 0 10px 0;
    color: var(--text-primary);
  }}
  .cover-subtitle {{
    font-size: 17px;
    color: var(--text-secondary);
    margin: 0 0 18px 0;
    font-weight: 400;
    letter-spacing: -0.01em;
  }}
  .cover-meta {{
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.75;
    margin: 0 0 20px 0;
    border-top: 1px solid var(--border-color);
    padding-top: 16px;
  }}
  .tag-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 22px;
  }}
  .theology-tag {{
    background: rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(0, 0, 0, 0.08);
    color: var(--text-primary);
    font-size: 12px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 9999px;
  }}
  body.theme-dark .theology-tag {{
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.15);
  }}
  .cover-action-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    padding-top: 18px;
    border-top: 1px solid var(--border-color);
  }}
  .cover-action-btn {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 20px;
    border-radius: 9999px;
    font-size: 13.5px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .cover-start-btn {{
    background: var(--apple-blue);
    color: #FFFFFF;
    box-shadow: 0 2px 10px rgba(0, 113, 227, 0.3);
  }}
  .cover-start-btn:hover {{
    background: #0077ED;
    transform: translateY(-2px);
  }}
  .cover-portal-btn {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    border: 1px solid rgba(0, 113, 227, 0.2);
  }}
  .cover-portal-btn:hover {{
    background: var(--apple-blue);
    color: #FFFFFF;
    transform: translateY(-2px);
  }}

  /* Directory Card Grid */
  .grid-section {{
    margin-bottom: 60px;
  }}
  .grid-header {{
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--text-primary);
    letter-spacing: -0.02em;
  }}
  .articles-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
  }}
  .grid-card {{
    background: transparent;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 20px 22px;
    text-decoration: none;
    color: inherit;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
  }}
  .grid-card:hover {{
    transform: translateY(-2px);
    border-color: rgba(0, 113, 227, 0.5);
    background: rgba(0, 113, 227, 0.02);
  }}
  .grid-card-num {{
    font-size: 11px;
    font-weight: 700;
    color: var(--apple-blue);
    background: var(--apple-blue-subtle);
    display: inline-block;
    padding: 2px 8px;
    border-radius: 9999px;
    width: fit-content;
    margin-bottom: 8px;
  }}
  .grid-card-title {{
    font-size: 15.5px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
  }}
  .grid-card-en {{
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 10px;
  }}
  .grid-card-desc {{
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.55;
    margin-top: auto;
  }}

  /* Article Containers */
  .article-section {{
    padding: 36px 0 48px 0;
    margin-bottom: 48px;
    border-bottom: 1px solid var(--border-color);
  }}
  .article-top-nav {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    margin-bottom: 16px;
    color: var(--text-secondary);
  }}
  .article-back-home {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    color: var(--apple-blue);
    text-decoration: none;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 6px;
    background: var(--apple-blue-subtle);
  }}
  .article-nav-sep {{
    opacity: 0.4;
  }}
  .article-nav-crumb {{
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .article-header-wrapper {{
    margin-bottom: 34px;
    padding-bottom: 22px;
    border-bottom: 1px solid var(--border-color);
  }}
  .article-badge-row {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }}
  .article-badge {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    font-size: 11.5px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 9999px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}
  .article-badge-sub {{
    font-size: 12.5px;
    color: var(--text-secondary);
    font-weight: 500;
  }}

  /* Bilingual Headers Grid */
  .bilingual-header-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
  }}
  .article-title {{
    font-family: var(--font-apple-display);
    font-size: 28px;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    letter-spacing: -0.025em;
    line-height: 1.25;
  }}
  .article-title-en {{
    font-size: 23px;
    font-weight: 600;
    color: var(--text-secondary);
    margin: 0;
    letter-spacing: -0.02em;
    line-height: 1.3;
  }}

  /* Dual Column Grid */
  .bilingual-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    margin-bottom: 24px;
  }}

  /* Bilingual Rows Architecture (Locked-Row Alignment) */
  .bilingual-rows-wrapper {{
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-bottom: 24px;
  }}

  .bilingual-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    align-items: start;
    padding-top: 20px;
    padding-bottom: 24px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    transition: background-color 0.18s ease;
  }}
  .bilingual-row:first-child {{
    padding-top: 4px;
  }}
  .bilingual-row:last-child {{
    border-bottom: none;
    padding-bottom: 0;
  }}
  .bilingual-row.row-tags {{
    border-bottom: none;
    padding-top: 0;
    padding-bottom: 6px;
  }}

  body.theme-dark .bilingual-row {{
    border-bottom-color: rgba(255, 255, 255, 0.08);
  }}
  body.theme-sepia .bilingual-row {{
    border-bottom-color: rgba(126, 112, 96, 0.1);
  }}

  .col-zh, .cell-zh {{
    font-family: var(--font-apple);
    text-align: justify;
    text-justify: inter-ideograph;
    font-size: var(--reader-fs-zh, 16.5px);
    line-height: var(--reader-lh-zh, 1.9);
  }}

  .col-en, .cell-en {{
    font-family: var(--font-en);
    text-align: left;
    font-size: var(--reader-fs-en, 15.5px);
    line-height: var(--reader-lh-en, 1.8);
  }}

  .bilingual-row .zh-subheading:first-child,
  .bilingual-row .en-subheading:first-child,
  .bilingual-row .zh-minor-heading:first-child,
  .bilingual-row .en-minor-heading:first-child {{
    margin-top: 0;
  }}

  .bilingual-row p:first-child {{
    margin-top: 0;
  }}
  .col-lang-tag {{
    font-size: 11px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 9999px;
    display: inline-block;
    margin-bottom: 14px;
    letter-spacing: 0.02em;
  }}
  .tag-zh {{ background: var(--apple-blue-subtle); color: var(--apple-blue); border: 1px solid rgba(0, 113, 227, 0.2); }}
  .tag-en {{ background: rgba(134, 134, 139, 0.08); color: var(--apple-gray); border: 1px solid rgba(134, 134, 139, 0.2); }}

  /* Subheadings & Typography inside columns */
  .zh-subheading {{
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 26px;
    margin-bottom: 12px;
    border-left: 3px solid var(--apple-blue);
    padding-left: 10px;
    letter-spacing: -0.015em;
  }}
  .en-subheading {{
    font-size: 17px;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 26px;
    margin-bottom: 12px;
    border-left: 3px solid var(--apple-gray);
    padding-left: 10px;
    font-family: var(--font-en);
    letter-spacing: -0.015em;
  }}
  .zh-minor-heading, .en-minor-heading {{
    font-size: 15.5px;
    font-weight: 600;
    color: var(--text-primary);
    margin-top: 18px;
    margin-bottom: 8px;
  }}

  p {{
    margin: 14px 0;
    color: var(--text-primary);
  }}
  blockquote {{
    border-left: 4px solid var(--apple-gray);
    background: rgba(134, 134, 139, 0.06);
    padding: 14px 20px;
    margin: 18px 0;
    color: var(--text-secondary);
    border-radius: 0 12px 12px 0;
  }}
  blockquote p {{
    margin: 6px 0;
    color: inherit;
  }}
  ul, ol {{
    padding-left: 24px;
    margin: 14px 0;
  }}
  li {{
    margin-bottom: 8px;
    font-size: 15px;
  }}
  .content-divider {{
    border: none;
    border-top: 1px solid var(--border-color);
    margin: 28px 0;
  }}

  /* Table styling */
  .table-responsive {{
    width: 100%;
    overflow-x: auto;
    margin: 20px 0;
  }}
  .styled-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border-color);
  }}
  .styled-table th {{
    background: var(--bg-card-subtle);
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
  }}
  .styled-table td {{
    padding: 10px 14px;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
  }}
  .styled-table tr:last-child td {{
    border-bottom: none;
  }}

  /* Article Footer Bar */
  .article-footer-nav {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 36px;
    padding-top: 22px;
    border-top: 1px solid var(--border-color);
    flex-wrap: wrap;
    gap: 12px;
  }}
  .article-footer-left, .article-footer-right {{
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}
  .art-nav-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border-radius: 9999px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    border: 1px solid var(--border-color);
    background: var(--bg-card-subtle);
    color: var(--text-primary);
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .art-nav-btn:hover {{
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }}
  .art-nav-disabled {{
    padding: 7px 14px;
    font-size: 12.5px;
    color: var(--text-secondary);
    opacity: 0.5;
  }}
  .art-home-action {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    border-color: rgba(0, 113, 227, 0.2);
  }}
  .art-home-action:hover {{
    background: var(--apple-blue);
    color: #FFFFFF;
  }}

  /* View Mode Toggles */
  body.view-zh-only .col-en,
  body.view-zh-only .cell-en,
  body.view-zh-only .header-en {{
    display: none !important;
  }}
  body.view-zh-only .bilingual-grid,
  body.view-zh-only .bilingual-row,
  body.view-zh-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

  body.view-en-only .col-zh,
  body.view-en-only .cell-zh,
  body.view-en-only .header-zh {{
    display: none !important;
  }}
  body.view-en-only .bilingual-grid,
  body.view-en-only .bilingual-row,
  body.view-en-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

  /* Floating Back to Top */
  #back-to-top {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.82);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.15);
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    z-index: 999;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  #back-to-top:hover {{
    transform: scale(1.1);
    background: var(--apple-blue);
  }}

  /* Mobile Bottom Reading Dock */
  .mobile-reading-dock {{
    display: none;
  }}

  /* Responsive Breakpoints (iPhone & iPad Optimization - Strictly matching reader.html) */
  @media (max-width: 1024px) {{
    #sidebar {{
      transform: translateX(-100%);
      width: 82vw;
      max-width: 340px;
      z-index: 10000;
      box-shadow: 10px 0 30px rgba(0, 0, 0, 0.2);
    }}
    #sidebar.show-mobile {{
      transform: translateX(0);
    }}
    .sidebar-mobile-close {{
      display: flex;
    }}
    #main-content {{
      margin-left: 0;
      padding: 68px 18px 100px 18px;
    }}
    .bilingual-grid,
    .bilingual-row,
    .bilingual-header-grid {{
      grid-template-columns: 1fr !important;
      gap: 20px !important;
    }}
    .cover-layout {{
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 24px;
    }}
    .cover-img-col {{
      width: 180px;
    }}
    .cover-action-row {{
      justify-content: center;
    }}
    .tag-row {{
      justify-content: center;
    }}
  }}

  @media (max-width: 768px) {{
    /* Hide top toolbar on mobile to maximize reading space */
    .top-toolbar {{
      display: none !important;
    }}
    .toolbar-trigger-btn {{
      display: none !important;
    }}

    /* Mobile Bottom Reading Dock */
    .mobile-reading-dock {{
      position: fixed;
      bottom: calc(14px + env(safe-area-inset-bottom, 0px));
      left: 50%;
      transform: translateX(-50%);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: space-around;
      gap: 4px;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(25px) saturate(180%);
      -webkit-backdrop-filter: blur(25px) saturate(180%);
      border: 1px solid rgba(0, 0, 0, 0.08);
      box-shadow: 0 10px 32px rgba(0, 0, 0, 0.14), 0 2px 6px rgba(0, 0, 0, 0.04);
      border-radius: 9999px;
      padding: 5px 10px;
      width: calc(100% - 28px);
      max-width: 420px;
      transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
    }}
    body.theme-dark .mobile-reading-dock {{
      background: rgba(28, 28, 30, 0.92);
      border-color: rgba(255, 255, 255, 0.15);
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6);
    }}
    body.theme-sepia .mobile-reading-dock {{
      background: rgba(244, 236, 223, 0.94);
      border-color: rgba(126, 112, 96, 0.2);
    }}
    .mobile-reading-dock.dock-hidden {{
      transform: translate(-50%, 150%);
      opacity: 0;
      pointer-events: none;
    }}

    .dock-btn {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2px;
      padding: 6px 2px;
      background: transparent;
      border: none;
      color: var(--text-primary);
      text-decoration: none;
      font-size: 10.5px;
      font-weight: 500;
      border-radius: 12px;
      cursor: pointer;
      touch-action: manipulation;
      min-width: 0;
    }}
    .dock-btn:active {{
      transform: scale(0.92);
      background: rgba(0, 0, 0, 0.06);
    }}
    body.theme-dark .dock-btn:active {{
      background: rgba(255, 255, 255, 0.1);
    }}
    .dock-icon {{
      font-size: 16px;
      line-height: 1.1;
    }}
    .dock-label {{
      font-size: 10.5px;
      letter-spacing: -0.01em;
      white-space: nowrap;
    }}
    .dock-home {{
      color: var(--apple-blue);
      font-weight: 600;
    }}

    /* Mobile Typography & Reading Canvas (matching reader.html exactly) */
    #main-content {{
      padding: 16px 14px calc(100px + env(safe-area-inset-bottom, 20px)) 14px;
    }}
    .article-section {{
      padding: 20px 0 28px 0;
      border-radius: 0;
      border: none;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 24px;
      box-shadow: none;
      background: transparent;
    }}
    .article-title {{
      font-size: 22px;
      line-height: 1.3;
    }}
    .article-title-en {{
      font-size: 17px;
      line-height: 1.35;
    }}
    .col-zh {{
      font-size: 18px;
      line-height: 1.95;
      letter-spacing: 0.02em;
    }}
    .col-en {{
      font-size: 16.5px;
      line-height: 1.82;
      letter-spacing: 0.01em;
    }}
    .col-zh p, p {{
      margin: 16px 0;
    }}
    .zh-subheading {{
      font-size: 20px;
      line-height: 1.4;
      margin-top: 28px;
      margin-bottom: 12px;
      border-left-width: 3px;
      padding-left: 10px;
    }}
    .en-subheading {{
      font-size: 18px;
      line-height: 1.4;
      margin-top: 26px;
      margin-bottom: 10px;
      border-left-width: 3px;
      padding-left: 10px;
    }}
    .zh-minor-heading {{
      font-size: 17px;
      font-weight: 600;
      margin-top: 20px;
      margin-bottom: 8px;
    }}
    .en-minor-heading {{
      font-size: 16px;
      font-weight: 600;
      margin-top: 18px;
      margin-bottom: 8px;
    }}
    blockquote {{
      padding: 14px 16px;
      font-size: 16.5px;
      line-height: 1.85;
      border-left-width: 4px;
      margin: 18px 0;
      border-radius: 0 12px 12px 0;
    }}
    li {{
      font-size: 17px;
      line-height: 1.85;
      margin-bottom: 10px;
    }}
    .cover-card {{
      padding: 20px 0 24px 0;
      border-radius: 0;
      margin-bottom: 24px;
      border: none;
      border-bottom: 1px solid var(--border-color);
    }}
    .cover-title {{
      font-size: 22px;
      line-height: 1.3;
    }}
    .cover-subtitle {{
      font-size: 13.5px;
      margin-bottom: 12px;
    }}
    .cover-meta {{
      font-size: 13px;
      line-height: 1.65;
      padding-top: 14px;
    }}
    .grid-section {{
      margin-bottom: 36px;
    }}
    .articles-grid {{
      grid-template-columns: 1fr;
      gap: 12px;
    }}
    .grid-card {{
      padding: 16px 18px;
      border-radius: 14px;
    }}
    .article-footer-nav {{
      flex-direction: column;
      align-items: stretch;
      gap: 10px;
    }}
    .article-footer-left, .article-footer-right {{
      display: flex;
      width: 100%;
      justify-content: stretch;
      gap: 8px;
    }}
    .article-footer-left .art-nav-btn, .article-footer-right .art-nav-btn {{
      width: 100%;
      justify-content: center;
    }}
  }}

  @media print {{
    body {{
      background: #ffffff !important;
      color: #000000 !important;
      display: block !important;
    }}
    #sidebar, .top-toolbar, #progress-bar, #back-to-top, .grid-section, .toolbar-trigger-btn, .mobile-reading-dock {{
      display: none !important;
    }}
    #main-content {{
      margin-left: 0 !important;
      padding: 0 !important;
      max-width: 100% !important;
    }}
    .cover-card {{
      page-break-after: always;
    }}
    .article-section {{
      page-break-before: always;
      padding: 20px 0 !important;
    }}
    .bilingual-grid,
    .bilingual-row {{
      grid-template-columns: 1fr 1fr !important;
      gap: 24px !important;
    }}
  }}
</style>
</head>
<body class="view-bilingual">

<div id="progress-bar"></div>

<div id="sidebar-backdrop" class="sidebar-backdrop" onclick="toggleSidebar()"></div>

<aside id="sidebar">
  <div class="sidebar-header">
    <div class="sidebar-top-bar">
      <div class="mac-window-controls">
        <span class="mac-dot mac-close" title="收起侧栏" onclick="toggleSidebar()"></span>
        <span class="mac-dot mac-minimize" title="切换外观主题" onclick="toggleTheme()"></span>
        <span class="mac-dot mac-maximize" title="双栏视图" onclick="setViewMode('bilingual')"></span>
        <span class="mac-window-title">Family Matters Reader</span>
      </div>
      <button class="sidebar-mobile-close" onclick="toggleSidebar()" title="收起目录">✕</button>
    </div>
    <span class="sidebar-badge">USMB · 北美门诺弟兄会</span>
    <h2 class="sidebar-title">属灵家事：走近门诺弟兄会</h2>
    <p class="sidebar-subtitle">中英双语对照典藏全集 · 目录导航</p>
  </div>

  <div class="sidebar-portal-nav">
    <a href="index.html" class="sidebar-portal-btn" title="返回 Evan's Thinking 首页">
      <span>🏠 返回主站首页</span>
      <span class="portal-btn-arrow">→</span>
    </a>
  </div>

  <div class="search-box">
    <input type="text" id="nav-search" class="search-input" placeholder="🔍 检索篇章、主题与关键词..." oninput="filterNav(this.value)">
  </div>

  <ul class="nav-list" id="nav-list">
    {''.join(sidebar_items_html)}
  </ul>
</aside>

<div class="top-toolbar" id="top-toolbar">
  <button class="tool-btn active" id="btn-view-bilingual" onclick="setViewMode('bilingual')" title="中英双栏对照阅读">双栏对照</button>
  <button class="tool-btn" id="btn-view-zh" onclick="setViewMode('zh-only')" title="仅显示中文译文">仅看中文</button>
  <button class="tool-btn" id="btn-view-en" onclick="setViewMode('en-only')" title="仅显示英文原文">English</button>
  <div class="toolbar-divider"></div>
  <button class="tool-btn" onclick="toggleTheme()" title="切换浅色/羊皮纸/深色模式">🌗 外观</button>
  <button class="tool-btn" onclick="adjustFontSize(-1)" title="减小字号">A-</button>
  <button class="tool-btn" onclick="adjustFontSize(1)" title="放大字号">A+</button>
  <div class="toolbar-divider"></div>
  <button class="tool-btn" onclick="window.print()" title="打印当前页面或导出为 PDF">🖨️ 打印</button>
  <a href="index.html" class="tool-btn" style="color: var(--apple-blue);" title="返回主页">🏠 首页</a>
</div>

<button class="toolbar-trigger-btn" id="toolbar-trigger" onclick="toggleToolbar()" title="展开阅读控制栏">
  <span class="trigger-dot"></span> 阅读选项
</button>

<button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="返回顶部">↑</button>

<!-- Mobile Floating Reading Dock (Apple Books Style - Strictly matching reader.html) -->
<nav class="mobile-reading-dock" id="mobile-reading-dock" aria-label="移动端底部快速操作栏">
  <a href="index.html" class="dock-btn dock-home" title="返回 Evan's Thinking 首页">
    <span class="dock-icon">🏠</span>
    <span class="dock-label">首页</span>
  </a>
  <button class="dock-btn" onclick="toggleSidebar()" title="打开全书章节目录">
    <span class="dock-icon">☰</span>
    <span class="dock-label">目录</span>
  </button>
  <button class="dock-btn" id="dock-view-btn" onclick="cycleMobileView()" title="切换 中文 / 双栏 / 英文">
    <span class="dock-icon">🌐</span>
    <span class="dock-label" id="dock-view-label">双栏</span>
  </button>
  <button class="dock-btn" onclick="toggleTheme()" title="切换 纸质米黄 / 柔白 / 深黑">
    <span class="dock-icon">☀️</span>
    <span class="dock-label">外观</span>
  </button>
  <button class="dock-btn" onclick="cycleMobileFontSize()" title="循环调节字号">
    <span class="dock-icon">Aa</span>
    <span class="dock-label" id="dock-size-label">字号</span>
  </button>
  <button class="dock-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" title="回到顶部">
    <span class="dock-icon">↑</span>
    <span class="dock-label">顶部</span>
  </button>
</nav>

<main id="main-content">
  <!-- Book Cover Presentation Card -->
  <section class="cover-card" id="cover">
    <div class="cover-layout">
      <div class="cover-img-col">
        <img src="family_matters_cover.jpg" alt="Family Matters Cover" class="cover-img">
      </div>
      <div class="cover-info-col">
        <span class="cover-badge">USMB &amp; CCMBC 权威典藏 · 中英双语对照版</span>
        <h1 class="cover-title">属灵家事：走近门诺弟兄会</h1>
        <div class="cover-subtitle"><em>Family Matters: Discovering the Mennonite Brethren (Revised United States Edition)</em></div>
        <div class="cover-meta">
          <strong>编著</strong>：美国门诺弟兄会信仰与生活委员会（Board of Faith and Life, USMB）· 康妮·费伯（Connie Faber）主编<br>
          <strong>中文译校</strong>：北美及海外门诺弟兄会教牧文献翻译组 · 和合本圣经经文引注 · 全本无删减中英双语版
        </div>
        <div class="tag-row">
          <span class="theology-tag">🏛️ 重洗派历史与宗教改革</span>
          <span class="theology-tag">📖 圣道之民与释经共同体</span>
          <span class="theology-tag">🕊️ 和平神学与和好使命</span>
          <span class="theology-tag">🌍 全球差传与ICOMB大家庭</span>
          <span class="theology-tag">📚 12大核心篇章全景典藏</span>
        </div>
<!-- Cover actions omitted for clean aesthetic -->
      </div>
    </div>
  </section>

  <!-- Quick Jump Directory Grid -->
  <section class="grid-section" id="grid-toc">
    <div class="grid-header">
      <span>📑 全书章节快速索引 · Quick Jump Directory</span>
    </div>
    <div class="articles-grid">
      {''.join(grid_cards_html)}
    </div>
  </section>

  <!-- All Book Articles -->
  {''.join(articles_html)}
</main>

<script>
  let lastScrollY = window.pageYOffset || document.documentElement.scrollTop;
  const toolbarEl = document.getElementById('top-toolbar');
  const triggerEl = document.getElementById('toolbar-trigger');
  const dockEl = document.getElementById('mobile-reading-dock');
  let ticking = false;

  function updateToolbarState() {{
    const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
    const diff = currentScrollY - lastScrollY;

    // Desktop Toolbar
    if (toolbarEl) {{
      if (currentScrollY <= 45) {{
        toolbarEl.classList.remove('toolbar-hidden');
        if (triggerEl) triggerEl.classList.remove('trigger-visible');
      }} else if (diff > 10) {{
        // Scrolling down: auto-hide toolbar so reading view is unobstructed
        toolbarEl.classList.add('toolbar-hidden');
        if (triggerEl) triggerEl.classList.add('trigger-visible');
      }} else if (diff < -8) {{
        // Scrolling up: immediately re-appear
        toolbarEl.classList.remove('toolbar-hidden');
        if (triggerEl) triggerEl.classList.remove('trigger-visible');
      }}
    }}

    // Mobile Dock Auto-Hide & Reveal
    if (dockEl) {{
      if (currentScrollY <= 45 || diff < -8) {{
        dockEl.classList.remove('dock-hidden');
      }} else if (diff > 12) {{
        dockEl.classList.add('dock-hidden');
      }}
    }}

    lastScrollY = currentScrollY;
    ticking = false;
  }}

  window.addEventListener('scroll', () => {{
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.getElementById('progress-bar').style.width = scrolled + '%';

    const btt = document.getElementById('back-to-top');
    if (winScroll > 400) {{
      btt.style.display = 'flex';
    }} else {{
      btt.style.display = 'none';
    }}

    if (!ticking) {{
      window.requestAnimationFrame(updateToolbarState);
      ticking = true;
    }}
  }}, {{ passive: true }});

  function toggleToolbar() {{
    if (toolbarEl.classList.contains('toolbar-hidden')) {{
      toolbarEl.classList.remove('toolbar-hidden');
      if (triggerEl) triggerEl.classList.remove('trigger-visible');
    }} else {{
      toolbarEl.classList.add('toolbar-hidden');
      if (triggerEl) triggerEl.classList.add('trigger-visible');
    }}
  }}

  document.querySelectorAll('.nav-link').forEach(link => {{
    link.addEventListener('click', () => {{
      if (window.innerWidth <= 1024) {{
        document.getElementById('sidebar').classList.remove('show-mobile');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (backdrop) backdrop.classList.remove('active');
        document.body.style.overflow = '';
      }}
    }});
  }});

  function toggleSidebar() {{
    const sb = document.getElementById('sidebar');
    const mc = document.getElementById('main-content');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (window.innerWidth <= 1024) {{
      const willShow = !sb.classList.contains('show-mobile');
      sb.classList.toggle('show-mobile', willShow);
      if (backdrop) backdrop.classList.toggle('active', willShow);
      document.body.style.overflow = willShow ? 'hidden' : '';
    }} else {{
      sb.classList.toggle('collapsed');
      mc.classList.toggle('expanded');
    }}
  }}

  function setViewMode(mode) {{
    document.body.classList.remove('view-bilingual', 'view-zh-only', 'view-en-only');
    const btnBi = document.getElementById('btn-view-bilingual');
    const btnZh = document.getElementById('btn-view-zh');
    const btnEn = document.getElementById('btn-view-en');
    if (btnBi) btnBi.classList.remove('active');
    if (btnZh) btnZh.classList.remove('active');
    if (btnEn) btnEn.classList.remove('active');

    if (mode === 'zh-only') {{
      document.body.classList.add('view-zh-only');
      if (btnZh) btnZh.classList.add('active');
    }} else if (mode === 'en-only') {{
      document.body.classList.add('view-en-only');
      if (btnEn) btnEn.classList.add('active');
    }} else {{
      document.body.classList.add('view-bilingual');
      if (btnBi) btnBi.classList.add('active');
    }}

    const dockLabel = document.getElementById('dock-view-label');
    if (dockLabel) {{
      if (mode === 'zh-only') dockLabel.textContent = '仅中文';
      else if (mode === 'en-only') dockLabel.textContent = '仅英文';
      else dockLabel.textContent = '双栏';
    }}
  }}

  const mobileModes = ['bilingual', 'zh-only', 'en-only'];
  let mobileModeIdx = 0;
  function cycleMobileView() {{
    mobileModeIdx = (mobileModeIdx + 1) % mobileModes.length;
    setViewMode(mobileModes[mobileModeIdx]);
  }}

  const themes = ['light', 'theme-sepia', 'theme-dark'];
  let currentThemeIdx = 0;
  function toggleTheme() {{
    document.body.classList.remove('theme-sepia', 'theme-dark');
    currentThemeIdx = (currentThemeIdx + 1) % themes.length;
    if (currentThemeIdx > 0) {{
      document.body.classList.add(themes[currentThemeIdx]);
    }}
  }}

  let currentDesktopBase = 16.5;
  function adjustFontSize(delta) {{
    currentDesktopBase = Math.max(14, Math.min(24, currentDesktopBase + delta));
    document.documentElement.style.setProperty('--reader-fs-zh', currentDesktopBase + 'px');
    document.documentElement.style.setProperty('--reader-fs-en', (currentDesktopBase - 1) + 'px');
  }}

  const mobileSizes = [15, 16.5, 18, 20];
  let mobileSizeIdx = 2; // Default 18px matching reader.html mobile size
  function cycleMobileFontSize() {{
    mobileSizeIdx = (mobileSizeIdx + 1) % mobileSizes.length;
    const sz = mobileSizes[mobileSizeIdx];
    document.documentElement.style.fontSize = sz + 'px';
    document.documentElement.style.setProperty('--reader-fs-zh', sz + 'px');
    document.documentElement.style.setProperty('--reader-fs-en', (sz - 1.5) + 'px');
    const lbl = document.getElementById('dock-size-label');
    if (lbl) lbl.textContent = sz + 'px';
  }}

  function filterNav(keyword) {{
    const kw = keyword.trim().toLowerCase();
    const items = document.querySelectorAll('.nav-item');
    items.forEach(item => {{
      const text = item.textContent.toLowerCase();
      if (!kw || text.includes(kw)) {{
        item.style.display = '';
      }} else {{
        item.style.display = 'none';
      }}
    }});
  }}

  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        const artCode = entry.target.getAttribute('data-art');
        if (artCode) {{
          document.querySelectorAll('.nav-item').forEach(el => {{
            if (el.getAttribute('data-art') === artCode) {{
              el.classList.add('active');
            }} else {{
              el.classList.remove('active');
            }}
          }});
        }}
      }}
    }});
  }}, {{ rootMargin: '-20% 0px -70% 0px' }});

  document.querySelectorAll('.article-section').forEach(sec => observer.observe(sec));

  // Keyboard navigation shortcuts
  window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 't' || e.key === 'T') toggleTheme();
    if (e.key === 'v' || e.key === 'V') cycleMobileView();
  }});
</script>

</body>
</html>
'''
    return full_html

if __name__ == '__main__':
    print("Building family_matters_reader.html with Bilingual Rows...")
    html_content = build_full_html()
    targets = [
        "family_matters_reader.html",
        "pages_dist/family_matters_reader.html",
        "Google云端硬盘上传发布包/family_matters_reader.html",
        "Google云端硬盘上传发布包/属灵家事_走近门诺弟兄会_中英双语对照版.html"
    ]
    for target in targets:
        os.makedirs(os.path.dirname(os.path.abspath(target)), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {target} ({len(html_content.encode('utf-8')):,} bytes)")
