import os
import re
import html

CHAPTER_DEFS = [
    {
        "id": "chap-01",
        "art_code": "01",
        "num_label": "01",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第一章：基督的血",
        "title_en": "Chapter 1: The Blood of Christ",
        "desc": "正常的基督徒生活之定义；罪行与罪性的双重问题；宝血与十字架的双重救赎；宝血在神面前的功效；良心的平安与得胜控告。",
        "en_file": "normal_christian_life/extracted_en/01_Chapter_01.md",
        "zh_file": "normal_christian_life/extracted_zh/01_Chapter_01.md",
    },
    {
        "id": "chap-02",
        "art_code": "02",
        "num_label": "02",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第二章：基督的十字架",
        "title_en": "Chapter 2: The Cross of Christ",
        "desc": "罪行得赦与从罪中得释放；人类的天性与肉体；在亚当里与在基督里；基督之死与复活的代表性与包罗万有性。",
        "en_file": "normal_christian_life/extracted_en/02_Chapter_02.md",
        "zh_file": "normal_christian_life/extracted_zh/02_Chapter_02.md",
    },
    {
        "id": "chap-03",
        "art_code": "03",
        "num_label": "03",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第三章：长进的途径－知道",
        "title_en": "Chapter 3: The Path of Progress: Knowing",
        "desc": "我们与基督同死是客观既成的事实；长进的第一步：知道（罗马书六章六节）；启示与头脑理智的本质区别；十字架解决人罪性的根源。",
        "en_file": "normal_christian_life/extracted_en/03_Chapter_03.md",
        "zh_file": "normal_christian_life/extracted_zh/03_Chapter_03.md",
    },
    {
        "id": "chap-04",
        "art_code": "04",
        "num_label": "04",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第四章：长进的途径－计算",
        "title_en": "Chapter 4: The Path of Progress: Reckoning",
        "desc": "长进的第二步：计算（算自己向罪是死的）；信心的计算建立在神的话上；试炼与失败是对信心的考验；住在基督里面。",
        "en_file": "normal_christian_life/extracted_en/04_Chapter_04.md",
        "zh_file": "normal_christian_life/extracted_zh/04_Chapter_04.md",
    },
    {
        "id": "chap-05",
        "art_code": "05",
        "num_label": "05",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第五章：十字架的分界",
        "title_en": "Chapter 5: The Divide of the Cross",
        "desc": "两个完全不同的创造系统；受浸的属灵意义：埋葬标志旧造的终结；在复活的荣耀里向神活出新生命。",
        "en_file": "normal_christian_life/extracted_en/05_Chapter_05.md",
        "zh_file": "normal_christian_life/extracted_zh/05_Chapter_05.md",
    },
    {
        "id": "chap-06",
        "art_code": "06",
        "num_label": "06",
        "part": "第一部分：救赎与得胜根基",
        "part_en": "Part One: Foundations of Redemption",
        "title_zh": "第六章：长进的途径－将自己献给神",
        "title_en": "Chapter 6: The Path of Progress: Presenting Ourselves to God",
        "desc": "长进的第三步：献上（将自己献给神作活祭）；从死里复活者的奉献；主权转移与完全归主；作基督的仆人与爱戴的奴仆。",
        "en_file": "normal_christian_life/extracted_en/06_Chapter_06.md",
        "zh_file": "normal_christian_life/extracted_zh/06_Chapter_06.md",
    },
    {
        "id": "chap-07",
        "art_code": "07",
        "num_label": "07",
        "part": "第二部分：永远目的与圣灵",
        "part_en": "Part Two: The Eternal Purpose & The Holy Spirit",
        "title_zh": "第七章：永远的目的",
        "title_en": "Chapter 7: The Eternal Purpose",
        "desc": "神永远的旨意：在许多弟兄中作长子；一粒麦子落在地里死了；亚当面对生命树的选择；基督是一切属灵生命的源头。",
        "en_file": "normal_christian_life/extracted_en/07_Chapter_07.md",
        "zh_file": "normal_christian_life/extracted_zh/07_Chapter_07.md",
    },
    {
        "id": "chap-08",
        "art_code": "08",
        "num_label": "08",
        "part": "第二部分：永远目的与圣灵",
        "part_en": "Part Two: The Eternal Purpose & The Holy Spirit",
        "title_zh": "第八章：圣灵",
        "title_en": "Chapter 8: The Holy Spirit",
        "desc": "圣灵的浇灌与圣灵的内住；得着恩膏与能力的秘诀在于信心；经历的多样性；宝贝放在瓦器里；基督绝对的主权与管理。",
        "en_file": "normal_christian_life/extracted_en/08_Chapter_08.md",
        "zh_file": "normal_christian_life/extracted_zh/08_Chapter_08.md",
    },
    {
        "id": "chap-09",
        "art_code": "09",
        "num_label": "09",
        "part": "第三部分：脱离律法与随灵生活",
        "part_en": "Part Three: Deliverance from Law & Walking in the Spirit",
        "title_zh": "第九章：罗马第七章的意义与价值",
        "title_en": "Chapter 9: The Meaning and Value of Romans Seven",
        "desc": "肉体与人的彻底无能；律法的真正用意：显明过犯与暴露全然败坏；基督是律法的总结；人的尽头是神的起头；保罗的凯歌。",
        "en_file": "normal_christian_life/extracted_en/09_Chapter_09.md",
        "zh_file": "normal_christian_life/extracted_zh/09_Chapter_09.md",
    },
    {
        "id": "chap-10",
        "art_code": "10",
        "num_label": "10",
        "part": "第三部分：脱离律法与随灵生活",
        "part_en": "Part Three: Deliverance from Law & Walking in the Spirit",
        "title_zh": "第十章：长进的途径－随从灵而行",
        "title_en": "Chapter 10: The Path of Progress: Walking in the Spirit",
        "desc": "肉体与圣灵的争战；基督是我们的生命；生命之灵的律胜过罪与死的律；长进的第四步：随从灵而行；让主在凡事上作当家的。",
        "en_file": "normal_christian_life/extracted_en/10_Chapter_10.md",
        "zh_file": "normal_christian_life/extracted_zh/10_Chapter_10.md",
    },
    {
        "id": "chap-11",
        "art_code": "11",
        "num_label": "11",
        "part": "第四部分：基督身体与福音目标",
        "part_en": "Part Four: The Body of Christ, Soul-Life & Gospel's Goal",
        "title_zh": "第十一章：在基督里面一个身体",
        "title_en": "Chapter 11: One Body in Christ",
        "desc": "关口与道路的联结；十字架的四重工作全貌；基督的爱与活祭的奉献；在基督的身体里同归于一；靠着爱我们的主得胜有余。",
        "en_file": "normal_christian_life/extracted_en/11_Chapter_11.md",
        "zh_file": "normal_christian_life/extracted_zh/11_Chapter_11.md",
    },
    {
        "id": "chap-12",
        "art_code": "12",
        "num_label": "12",
        "part": "第四部分：基督身体与福音目标",
        "part_en": "Part Four: The Body of Christ, Soul-Life & Gospel's Goal",
        "title_zh": "第十二章：十字架与魂生命",
        "title_en": "Chapter 12: The Cross and the Soul Life",
        "desc": "堕落的真正本质；根本问题：人的魂生命与天然才能；天然能力与神圣圣灵之工的区别；神的光照与真正的自知。",
        "en_file": "normal_christian_life/extracted_en/12_Chapter_12.md",
        "zh_file": "normal_christian_life/extracted_zh/12_Chapter_12.md",
    },
    {
        "id": "chap-13",
        "art_code": "13",
        "num_label": "13",
        "part": "第四部分：基督身体与福音目标",
        "part_en": "Part Four: The Body of Christ, Soul-Life & Gospel's Goal",
        "title_zh": "第十三章：长进的途径－背十字架",
        "title_en": "Chapter 13: The Path of Progress: Bearing the Cross",
        "desc": "一切真实职事的根基；十字架的主观经历；背负十字架与结出属天果子；黑夜之后的复活早晨；真正的基督仆人。",
        "en_file": "normal_christian_life/extracted_en/13_Chapter_13.md",
        "zh_file": "normal_christian_life/extracted_zh/13_Chapter_13.md",
    },
    {
        "id": "chap-14",
        "art_code": "14",
        "num_label": "14",
        "part": "第四部分：基督身体与福音目标",
        "part_en": "Part Four: The Body of Christ, Soul-Life & Gospel's Goal",
        "title_zh": "第十四章：福音的目的",
        "title_en": "Chapter 14: The Goal of the Gospel",
        "desc": "伯大尼马利亚打破玉瓶膏主；“何用这样枉费？”；向主枉费是一切事奉的核心；散发出基督馨香之气；使神的心得着完满的喜悦。",
        "en_file": "normal_christian_life/extracted_en/14_Chapter_14.md",
        "zh_file": "normal_christian_life/extracted_zh/14_Chapter_14.md",
    },
    {
        "id": "chap-app",
        "art_code": "app",
        "num_label": "附录",
        "part": "附录与文献考证",
        "part_en": "Appendix & Critical Notes",
        "title_zh": "附录：全书神学详注与原版考证",
        "title_en": "Appendix: Theological Endnotes & Textual References",
        "desc": "英文原版编者注（Ed.）与倪柝声原注（W.N.）；希腊文关键神学词汇辨析（katargeo, sumphytos, paristemi）；历史文献考据。",
        "en_file": "normal_christian_life/extracted_en/15_Endnotes.md",
        "zh_file": "normal_christian_life/extracted_zh/15_Endnotes.md",
    }
]

def markdown_to_html(md_text, lang='zh'):
    subheading_cls = f"{lang}-subheading"
    minorheading_cls = f"{lang}-minor-heading"
    
    lines = md_text.split('\n')
    output = []
    
    in_ul = False
    in_ol = False
    in_bq = False
    
    def close_blocks():
        nonlocal in_ul, in_ol, in_bq
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
        return res

    def inline_format(text):
        text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text

    for line in lines:
        raw = line.strip()
        
        if not raw:
            output.extend(close_blocks())
            continue
            
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

    grid_cards_html = []
    for item in CHAPTER_DEFS:
        grid_cards_html.append(f'''
        <a href="#{item["id"]}" class="grid-card">
          <div class="grid-card-num">{item["part_en"]} · {item["num_label"]}</div>
          <div class="grid-card-title">{html.escape(item["title_zh"])}</div>
          <div class="grid-card-en">{html.escape(item["title_en"])}</div>
          <div class="grid-card-desc">{html.escape(item["desc"])}</div>
        </a>''')

    articles_html = []
    total_chaps = len(CHAPTER_DEFS)
    for idx, item in enumerate(CHAPTER_DEFS):
        prev_item = CHAPTER_DEFS[idx - 1] if idx > 0 else None
        next_item = CHAPTER_DEFS[idx + 1] if idx < total_chaps - 1 else None

        with open(item["zh_file"], "r", encoding="utf-8") as f:
            zh_raw = f.read()
        with open(item["en_file"], "r", encoding="utf-8") as f:
            en_raw = f.read()

        zh_rendered = markdown_to_html(zh_raw, lang='zh')
        en_rendered = markdown_to_html(en_raw, lang='en')

        prev_btn = f'<a href="#{prev_item["id"]}" class="art-nav-btn">← 上一章：{html.escape(prev_item["title_zh"])}</a>' if prev_item else '<span class="art-nav-disabled">已是第一章</span>'
        next_btn = f'<a href="#{next_item["id"]}" class="art-nav-btn">下一章：{html.escape(next_item["title_zh"])} →</a>' if next_item else '<a href="#cover" class="art-nav-btn">返回全书顶部 ⇡</a>'

        article_block = f'''
    <!-- ARTICLE: {item["title_zh"]} -->
    <article id="{item["id"]}" class="article-section" data-art="{item["art_code"]}">
      <nav class="article-top-nav">
        <a href="index.html" class="article-back-home">🏠 首页</a>
        <span class="article-nav-sep">/</span>
        <a href="#cover" class="article-nav-crumb">正常的基督徒生活</a>
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

      <div class="bilingual-grid">
        <div class="col-zh">
          <div class="col-lang-tag tag-zh">🇨🇳 中文经典译文 · 倪柝声文集第二辑第13册</div>
          {zh_rendered}
        </div>
        <div class="col-en">
          <div class="col-lang-tag tag-en">🇬🇧 English Original Text · Watchman Nee</div>
          {en_rendered}
        </div>
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
<title>《正常的基督徒生活》（中英双语典藏全集）- The Normal Christian Life</title>
<meta name="description" content="倪柝声基督徒灵命经典《正常的基督徒生活》（The Normal Christian Life）中英双语对照权威典藏全集。全书14章深入阐释罗马书一至八章生命经历与十字架工作。">
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

  /* Dark Mode */
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

  /* Sepia Mode */
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

  #progress-bar {{
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--apple-blue), var(--apple-purple));
    width: 0%;
    z-index: 10001;
    transition: width 0.1s ease-out;
  }}

  #sidebar {{
    width: var(--sidebar-width);
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    background: var(--bg-sidebar);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border-right: 1px solid var(--sidebar-border);
    display: flex;
    flex-direction: column;
    z-index: 100;
    overflow: hidden;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.3s ease;
  }}

  .sidebar-header {{
    padding: 24px 20px 16px 20px;
    border-bottom: 1px solid var(--sidebar-border);
  }}
  .sidebar-badge {{
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--apple-blue);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .sidebar-badge-close {{
    display: none;
    background: rgba(0, 0, 0, 0.06);
    border: none;
    border-radius: 50%;
    width: 26px;
    height: 26px;
    cursor: pointer;
    font-size: 14px;
    align-items: center;
    justify-content: center;
    color: var(--sidebar-text-muted);
  }}
  .sidebar-title {{
    font-family: var(--font-apple-display);
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: var(--sidebar-text);
    margin: 0 0 4px 0;
    line-height: 1.3;
  }}
  .sidebar-subtitle {{
    font-size: 12px;
    color: var(--sidebar-text-muted);
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .sidebar-nav {{
    flex: 1;
    overflow-y: auto;
    padding: 12px 10px 40px 10px;
    list-style: none;
    margin: 0;
  }}
  .nav-part-header {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--sidebar-text-muted);
    padding: 14px 12px 6px 12px;
    margin-top: 8px;
    border-top: 1px solid var(--sidebar-border);
  }}
  .nav-part-header:first-child {{
    border-top: none;
    margin-top: 0;
    padding-top: 4px;
  }}
  .nav-item {{
    margin-bottom: 2px;
  }}
  .nav-link {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 12px;
    border-radius: 8px;
    text-decoration: none;
    color: var(--sidebar-text);
    transition: all 0.18s ease;
    font-size: 13px;
    line-height: 1.4;
  }}
  .nav-link:hover {{
    background: rgba(0, 0, 0, 0.05);
    color: var(--apple-blue);
  }}
  body.theme-dark .nav-link:hover {{
    background: rgba(255, 255, 255, 0.08);
  }}
  .nav-item.active .nav-link {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    font-weight: 600;
  }}
  .nav-num {{
    font-size: 11px;
    font-weight: 700;
    color: var(--apple-blue);
    padding-top: 2px;
    flex-shrink: 0;
    min-width: 22px;
  }}
  .nav-link-content {{
    flex: 1;
    min-width: 0;
  }}
  .nav-title {{
    font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .nav-en {{
    font-size: 11px;
    color: var(--sidebar-text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  #sidebar-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 99;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
  }}
  #sidebar-backdrop.active {{
    opacity: 1;
    pointer-events: auto;
  }}

  #main-content {{
    margin-left: var(--sidebar-width);
    flex: 1;
    max-width: 1360px;
    padding: 72px 48px 120px 48px;
    min-height: 100vh;
    transition: margin-left 0.35s ease;
  }}

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
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .btn-primary {{
    background: var(--apple-blue);
    color: #FFFFFF;
    box-shadow: 0 4px 12px rgba(0, 113, 227, 0.3);
  }}
  .btn-primary:hover {{
    background: var(--apple-blue-hover);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(0, 113, 227, 0.4);
  }}
  .btn-secondary {{
    background: var(--bg-card-subtle);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
  }}
  .btn-secondary:hover {{
    background: var(--border-color);
    transform: translateY(-1px);
  }}

  /* Directory Grid Section */
  .grid-section {{
    margin-bottom: 50px;
  }}
  .section-heading-row {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
  }}
  .section-h2 {{
    font-family: var(--font-apple-display);
    font-size: 20px;
    font-weight: 700;
    margin: 0;
  }}
  .section-h2-sub {{
    font-size: 12.5px;
    color: var(--text-secondary);
  }}
  .dir-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
  }}
  .grid-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 16px 18px;
    text-decoration: none;
    color: var(--text-primary);
    box-shadow: var(--card-shadow);
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
  }}
  .grid-card:hover {{
    transform: translateY(-2px);
    border-color: var(--apple-blue);
    box-shadow: 0 8px 24px rgba(0, 113, 227, 0.12);
  }}
  .grid-card-num {{
    font-size: 11px;
    font-weight: 700;
    color: var(--apple-blue);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
  }}
  .grid-card-title {{
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 4px;
    line-height: 1.35;
  }}
  .grid-card-en {{
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 8px;
    line-height: 1.3;
  }}
  .grid-card-desc {{
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-top: auto;
    opacity: 0.85;
  }}

  /* Chapter Article Section */
  .article-section {{
    background: var(--bg-card);
    border-radius: 20px;
    border: 1px solid var(--border-color);
    padding: 38px 40px;
    margin-bottom: 40px;
    box-shadow: var(--card-shadow);
    transition: background-color 0.3s ease, border-color 0.3s ease;
  }}
  .article-top-nav {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    color: var(--text-secondary);
    margin-bottom: 24px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border-color);
  }}
  .article-back-home {{
    color: var(--apple-blue);
    text-decoration: none;
    font-weight: 500;
  }}
  .article-back-home:hover {{
    text-decoration: underline;
  }}
  .article-nav-sep {{
    opacity: 0.4;
  }}
  .article-nav-crumb {{
    text-decoration: none;
    color: var(--text-secondary);
  }}
  .article-nav-crumb:hover {{
    color: var(--apple-blue);
  }}
  .article-header-wrapper {{
    margin-bottom: 30px;
    padding-bottom: 22px;
    border-bottom: 1px solid var(--border-color);
  }}
  .article-badge-row {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
  }}
  .article-badge {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
    font-size: 11.5px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
    letter-spacing: 0.03em;
  }}
  .article-badge-sub {{
    font-size: 12px;
    color: var(--text-secondary);
  }}
  .bilingual-header-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
  }}
  .article-title {{
    font-family: var(--font-apple-display);
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.3;
    margin: 0;
  }}
  .article-title-en {{
    font-family: var(--font-apple-display);
    font-size: 22px;
    font-weight: 600;
    letter-spacing: -0.015em;
    line-height: 1.35;
    margin: 0;
    color: var(--text-secondary);
  }}

  /* Bilingual Content Grid */
  .bilingual-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    margin-bottom: 24px;
  }}
  .col-zh {{
    font-family: var(--font-apple);
    font-size: var(--reader-fs-zh);
    line-height: var(--reader-lh-zh);
    color: var(--text-primary);
  }}
  .col-en {{
    font-family: var(--font-en);
    font-size: var(--reader-fs-en);
    line-height: var(--reader-lh-en);
    color: var(--text-secondary);
  }}
  .col-lang-tag {{
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 18px;
    padding: 4px 10px;
    border-radius: 6px;
    display: inline-block;
  }}
  .tag-zh {{
    background: var(--apple-blue-subtle);
    color: var(--apple-blue);
  }}
  .tag-en {{
    background: rgba(0, 0, 0, 0.05);
    color: var(--text-secondary);
  }}
  body.theme-dark .tag-en {{
    background: rgba(255, 255, 255, 0.08);
  }}

  .col-zh p, .col-en p {{
    margin: 0 0 16px 0;
    text-align: justify;
  }}
  .zh-subheading {{
    font-size: 18px;
    font-weight: 700;
    margin: 28px 0 14px 0;
    padding-left: 10px;
    border-left: 3px solid var(--apple-blue);
    line-height: 1.4;
    color: var(--text-primary);
  }}
  .en-subheading {{
    font-size: 17px;
    font-weight: 600;
    margin: 28px 0 14px 0;
    padding-left: 10px;
    border-left: 3px solid var(--apple-gray);
    line-height: 1.4;
    color: var(--text-primary);
  }}
  .zh-minor-heading {{
    font-size: 15.5px;
    font-weight: 600;
    margin: 20px 0 10px 0;
    color: var(--text-primary);
  }}
  .en-minor-heading {{
    font-size: 14.5px;
    font-weight: 600;
    margin: 20px 0 10px 0;
    color: var(--text-primary);
  }}
  blockquote {{
    margin: 18px 0;
    padding: 12px 18px;
    background: var(--bg-card-subtle);
    border-left: 4px solid var(--apple-blue);
    border-radius: 0 8px 8px 0;
    font-style: italic;
  }}
  blockquote p {{
    margin: 0;
  }}
  ul, ol {{
    margin: 0 0 16px 0;
    padding-left: 22px;
  }}
  li {{
    margin-bottom: 8px;
    line-height: 1.7;
  }}

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
  body.view-zh-only .header-en {{
    display: none !important;
  }}
  body.view-zh-only .bilingual-grid,
  body.view-zh-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

  body.view-en-only .col-zh,
  body.view-en-only .header-zh {{
    display: none !important;
  }}
  body.view-en-only .bilingual-grid,
  body.view-en-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

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

  /* Responsive Breakpoints */
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
    .sidebar-badge-close {{
      display: flex;
    }}
    #main-content {{
      margin-left: 0;
      padding: 68px 18px 100px 18px;
    }}
    .bilingual-grid,
    .bilingual-header-grid {{
      grid-template-columns: 1fr;
      gap: 20px;
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
    .top-toolbar {{
      display: none !important;
    }}
    .toolbar-trigger-btn {{
      display: none !important;
    }}

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
    .article-footer-nav {{
      flex-direction: column;
      align-items: stretch;
      gap: 12px;
    }}
    .article-footer-left, .article-footer-right {{
      justify-content: space-between;
      width: 100%;
    }}
    .art-nav-btn {{
      flex: 1;
      justify-content: center;
      text-align: center;
      padding: 10px 14px;
    }}
  }}
</style>
</head>
<body class="view-bilingual">

<div id="progress-bar"></div>

<div id="sidebar-backdrop" onclick="toggleSidebar(false)"></div>

<aside id="sidebar">
  <div class="sidebar-header">
    <div class="sidebar-badge">
      <span>CLASSIC READING</span>
      <button class="sidebar-badge-close" onclick="toggleSidebar(false)">✕</button>
    </div>
    <h1 class="sidebar-title">正常的基督徒生活</h1>
    <p class="sidebar-subtitle">The Normal Christian Life · 倪柝声</p>
  </div>
  <ul class="sidebar-nav">
    { "".join(sidebar_items_html) }
  </ul>
</aside>

<div class="top-toolbar" id="top-toolbar">
  <a href="index.html" class="tool-btn" title="返回 Evan's Thinking 首页">🏠 首页</a>
  <span class="toolbar-divider"></span>
  <button class="tool-btn" id="btn-theme-light" onclick="setTheme('light')">☀️ 浅色</button>
  <button class="tool-btn" id="btn-theme-sepia" onclick="setTheme('sepia')">📜 羊皮纸</button>
  <button class="tool-btn" id="btn-theme-dark" onclick="setTheme('dark')">🌙 深色</button>
  <span class="toolbar-divider"></span>
  <button class="tool-btn active" id="btn-view-bi" onclick="setViewMode('bilingual')">🌐 双语</button>
  <button class="tool-btn" id="btn-view-zh" onclick="setViewMode('zh-only')">中</button>
  <button class="tool-btn" id="btn-view-en" onclick="setViewMode('en-only')">EN</button>
  <span class="toolbar-divider"></span>
  <button class="tool-btn" onclick="cycleFontSize()" id="btn-font-scale">Aa</button>
  <span class="toolbar-divider"></span>
  <button class="tool-btn" onclick="toggleSidebar()" id="sidebar-toggle-btn">☰ 目录</button>
</div>

<button class="toolbar-trigger-btn" id="toolbar-trigger-btn" onclick="restoreToolbar()">
  <span class="trigger-dot"></span> 展开工具栏 ⚙️
</button>

<main id="main-content">

  <section class="cover-card" id="cover">
    <div class="cover-layout">
      <div class="cover-img-col">
        <img src="normal_christian_life_cover.jpg" alt="正常的基督徒生活 书影" class="cover-img">
      </div>
      <div class="cover-info-col">
        <span class="cover-badge">THEOLOGICAL HERITAGE · 典藏文献</span>
        <h1 class="cover-title">正常的基督徒生活</h1>
        <div class="cover-subtitle">The Normal Christian Life · 中英双语权威典藏版</div>
        <div class="cover-meta">
          <strong>著作背景：</strong>《正常的基督徒生活》（英语：The Normal Christian Life）是倪柝声于1938年至1939年旅行欧洲时完成的著名作品，首先用英语在英国（开西大会）、丹麦讲道时发表，回中国后由上海福音书房出版了中文文本。该书被许多基督徒视为经典著作，这也是西方基督教界最熟悉的一本倪柝声著作。该书已经用多种语言出版，至今至少出版了25万册。<br>
          <strong>双语对照：</strong>中文精选《倪柝声文集》权威原版，英文采官方英译本，逐章对照并收录全书神学详注与原版考证。
        </div>
        <div class="cover-action-row">
          <a href="#chap-01" class="cover-action-btn btn-primary">📖 开始阅读第一章</a>
          <a href="#dir-grid-section" class="cover-action-btn btn-secondary">📑 查看全书目录</a>
          <a href="index.html" class="cover-action-btn btn-secondary">🏠 返回首页</a>
        </div>
      </div>
    </div>
  </section>

  <section class="grid-section" id="dir-grid-section">
    <div class="section-heading-row">
      <h2 class="section-h2">全书章节目录总览</h2>
      <span class="section-h2-sub">14 Chapters + Theological Appendix</span>
    </div>
    <div class="dir-grid">
      { "".join(grid_cards_html) }
    </div>
  </section>

  { "".join(articles_html) }

</main>

<div class="mobile-reading-dock" id="mobile-dock">
  <a href="index.html" class="dock-btn dock-home" title="返回首页">
    <span class="dock-icon">🏠</span>
    <span class="dock-label">首页</span>
  </a>
  <button class="dock-btn" onclick="toggleSidebar()" title="章节目录">
    <span class="dock-icon">☰</span>
    <span class="dock-label">目录</span>
  </button>
  <button class="dock-btn" onclick="cycleMobileViewMode()" id="dock-view-btn" title="中英视图切换">
    <span class="dock-icon">🌐</span>
    <span class="dock-label" id="dock-view-label">双语</span>
  </button>
  <button class="dock-btn" onclick="cycleMobileTheme()" id="dock-theme-btn" title="模式切换">
    <span class="dock-icon" id="dock-theme-icon">☀️</span>
    <span class="dock-label" id="dock-theme-label">主题</span>
  </button>
  <button class="dock-btn" onclick="cycleFontSize()" title="字号调节">
    <span class="dock-icon">Aa</span>
    <span class="dock-label" id="dock-font-label">字号</span>
  </button>
  <button class="dock-btn" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="回顶部">
    <span class="dock-icon">↑</span>
    <span class="dock-label">顶部</span>
  </button>
</div>

<button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="返回顶部">↑</button>

<script>
  let currentTheme = localStorage.getItem('ncl_theme') || 'light';
  let currentView = localStorage.getItem('ncl_view') || 'bilingual';
  let fontScales = [1, 1.12, 1.25, 0.9];
  let fontScaleIdx = parseInt(localStorage.getItem('ncl_font_scale_idx') || '0', 10);

  function applyTheme(theme) {{
    document.body.classList.remove('theme-dark', 'theme-sepia');
    document.querySelectorAll('.tool-btn[id^="btn-theme-"]').forEach(b => b.classList.remove('active'));
    
    if (theme === 'dark') {{
      document.body.classList.add('theme-dark');
      const b = document.getElementById('btn-theme-dark');
      if (b) b.classList.add('active');
    }} else if (theme === 'sepia') {{
      document.body.classList.add('theme-sepia');
      const b = document.getElementById('btn-theme-sepia');
      if (b) b.classList.add('active');
    }} else {{
      const b = document.getElementById('btn-theme-light');
      if (b) b.classList.add('active');
    }}
    
    const dockIcon = document.getElementById('dock-theme-icon');
    const dockLabel = document.getElementById('dock-theme-label');
    if (dockIcon && dockLabel) {{
      if (theme === 'dark') {{
        dockIcon.textContent = '🌙';
        dockLabel.textContent = '深色';
      }} else if (theme === 'sepia') {{
        dockIcon.textContent = '📜';
        dockLabel.textContent = '羊皮纸';
      }} else {{
        dockIcon.textContent = '☀️';
        dockLabel.textContent = '浅色';
      }}
    }}
    
    currentTheme = theme;
    localStorage.setItem('ncl_theme', theme);
  }}

  function setTheme(theme) {{
    applyTheme(theme);
  }}

  function cycleMobileTheme() {{
    if (currentTheme === 'light') setTheme('sepia');
    else if (currentTheme === 'sepia') setTheme('dark');
    else setTheme('light');
  }}

  function applyViewMode(mode) {{
    document.body.classList.remove('view-bilingual', 'view-zh-only', 'view-en-only');
    document.querySelectorAll('.tool-btn[id^="btn-view-"]').forEach(b => b.classList.remove('active'));
    
    if (mode === 'zh-only') {{
      document.body.classList.add('view-zh-only');
      const b = document.getElementById('btn-view-zh');
      if (b) b.classList.add('active');
    }} else if (mode === 'en-only') {{
      document.body.classList.add('view-en-only');
      const b = document.getElementById('btn-view-en');
      if (b) b.classList.add('active');
    }} else {{
      document.body.classList.add('view-bilingual');
      const b = document.getElementById('btn-view-bi');
      if (b) b.classList.add('active');
    }}

    const dockLabel = document.getElementById('dock-view-label');
    if (dockLabel) {{
      if (mode === 'zh-only') dockLabel.textContent = '仅中文';
      else if (mode === 'en-only') dockLabel.textContent = 'English';
      else dockLabel.textContent = '双语';
    }}

    currentView = mode;
    localStorage.setItem('ncl_view', mode);
  }}

  function setViewMode(mode) {{
    applyViewMode(mode);
  }}

  function cycleMobileViewMode() {{
    if (currentView === 'bilingual') setViewMode('zh-only');
    else if (currentView === 'zh-only') setViewMode('en-only');
    else setViewMode('bilingual');
  }}

  function applyFontScale() {{
    const scale = fontScales[fontScaleIdx];
    document.documentElement.style.fontSize = (16 * scale) + 'px';
    const btn = document.getElementById('btn-font-scale');
    if (btn) {{
      if (scale === 1) btn.textContent = 'Aa';
      else if (scale > 1) btn.textContent = 'Aa+';
      else btn.textContent = 'Aa-';
    }}
    const dockFont = document.getElementById('dock-font-label');
    if (dockFont) {{
      if (scale === 1) dockFont.textContent = '标准';
      else if (scale === 1.12) dockFont.textContent = '放大';
      else if (scale === 1.25) dockFont.textContent = '特大';
      else dockFont.textContent = '精细';
    }}
    localStorage.setItem('ncl_font_scale_idx', fontScaleIdx);
  }}

  function cycleFontSize() {{
    fontScaleIdx = (fontScaleIdx + 1) % fontScales.length;
    applyFontScale();
  }}

  function toggleSidebar(force) {{
    const sb = document.getElementById('sidebar');
    const bd = document.getElementById('sidebar-backdrop');
    if (typeof force === 'boolean') {{
      if (force) {{
        sb.classList.add('show-mobile');
        bd.classList.add('active');
      }} else {{
        sb.classList.remove('show-mobile');
        bd.classList.remove('active');
      }}
    }} else {{
      sb.classList.toggle('show-mobile');
      bd.classList.toggle('active');
    }}
  }}

  let lastScrollY = window.scrollY;
  const topToolbar = document.getElementById('top-toolbar');
  const triggerBtn = document.getElementById('toolbar-trigger-btn');
  const mobileDock = document.getElementById('mobile-dock');
  const backToTop = document.getElementById('back-to-top');
  const progressBar = document.getElementById('progress-bar');

  function restoreToolbar() {{
    if (topToolbar) topToolbar.classList.remove('toolbar-hidden');
    if (triggerBtn) triggerBtn.classList.remove('trigger-visible');
  }}

  window.addEventListener('scroll', () => {{
    const currentY = window.scrollY;
    
    // Progress bar
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    if (maxScroll > 0) {{
      const pct = Math.min(100, Math.max(0, (currentY / maxScroll) * 100));
      progressBar.style.width = pct + '%';
    }}

    // Back to top button
    if (currentY > 400) {{
      backToTop.style.display = 'flex';
    }} else {{
      backToTop.style.display = 'none';
    }}

    // Hide/show toolbars on scroll
    if (currentY > lastScrollY && currentY > 200) {{
      // Scrolling down
      if (topToolbar) topToolbar.classList.add('toolbar-hidden');
      if (triggerBtn) triggerBtn.classList.add('trigger-visible');
      if (mobileDock) mobileDock.classList.add('dock-hidden');
    }} else if (currentY < lastScrollY) {{
      // Scrolling up
      if (topToolbar) topToolbar.classList.remove('toolbar-hidden');
      if (triggerBtn) triggerBtn.classList.remove('trigger-visible');
      if (mobileDock) mobileDock.classList.remove('dock-hidden');
    }}
    lastScrollY = currentY;
  }}, {{ passive: true }});

  // IntersectionObserver for active section in sidebar
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        const artCode = entry.target.getAttribute('data-art');
        document.querySelectorAll('.nav-item').forEach(el => {{
          el.classList.toggle('active', el.getAttribute('data-art') === artCode);
        }});
      }}
    }});
  }}, {{ threshold: 0.1, rootMargin: '-100px 0px -70% 0px' }});

  document.querySelectorAll('.article-section').forEach(sec => observer.observe(sec));

  // Initialize preferences
  applyTheme(currentTheme);
  applyViewMode(currentView);
  applyFontScale();

  // Close sidebar on link click (mobile)
  document.querySelectorAll('.nav-link').forEach(link => {{
    link.addEventListener('click', () => {{
      if (window.innerWidth <= 1024) {{
        toggleSidebar(false);
      }}
    }});
  }});
</script>
</body>
</html>
'''
    return full_html

if __name__ == '__main__':
    print("Building full bilingual reader for The Normal Christian Life...")
    html_content = build_full_html()
    
    out_dist = 'pages_dist/normal_christian_life_reader.html'
    with open(out_dist, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {out_dist} ({len(html_content)} bytes)")
    
    out_root = 'normal_christian_life_reader.html'
    with open(out_root, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {out_root} ({len(html_content)} bytes)")
