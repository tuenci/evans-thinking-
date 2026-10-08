# -*- coding: utf-8 -*-
"""
HTML Reader Generator for Wang Mingdao's 'The True Meaning of Being Born Again'
《重生真意》（中英双语权威典藏版）· 王明道 著
Following the exact Apple Books design system & responsive layout standards.
"""
import re
import os

chapters_meta = [
    {
        "id": "chapter-preface",
        "num": "PREFACE",
        "num_short": "序",
        "title_zh": "自序：四种称为基督徒的人",
        "title_en": "Author's Preface: Four Classes of Christians",
        "desc_zh": "四等称为基督徒之人的属灵鉴别与省察；分辨理论知识与真实生命的本质鸿沟。",
        "desc_en": "Four classes of professing Christians & the spiritual touchstone of genuine regeneration.",
        "file": "cszy_translation/00_preface.md"
    },
    {
        "id": "chapter-1",
        "num": "CHAPTER 1",
        "num_short": "01",
        "title_zh": "一、重生是什么意思？",
        "title_en": "What Does It Mean to Be Born Again?",
        "desc_zh": "从水和圣灵而生；神的道与圣灵的工作；清晰分辨「外面的人」与「里面的人」。",
        "desc_en": "Born of water and the Spirit: The spiritual reality of the Inner Man vs. the Outer Man.",
        "file": "cszy_translation/01_chapter1.md"
    },
    {
        "id": "chapter-2",
        "num": "CHAPTER 2",
        "num_short": "02",
        "title_zh": "二、为什么人必须重生？",
        "title_en": "Why Must Man Be Born Again?",
        "desc_zh": "神圣眼光中的人类全然败坏；道德自省的局限；从根本生命更新的治本之道。",
        "desc_en": "Total depravity before holy God: Dealing with the corrupt root rather than outward leaves.",
        "file": "cszy_translation/02_chapter2.md"
    },
    {
        "id": "chapter-3",
        "num": "CHAPTER 3",
        "num_short": "03",
        "title_zh": "三、人得了重生有什么表现？",
        "title_en": "What Are the Evidences of Being Born Again?",
        "desc_zh": "如风拂过必有明证：恨恶罪恶、渴慕圣洁、真诚爱神爱人、顺服圣道之活泼果效。",
        "desc_en": "The invisible wind with visible fruits: Transformations and spiritual proofs of the new nature.",
        "file": "cszy_translation/03_chapter3.md"
    },
    {
        "id": "chapter-4",
        "num": "CHAPTER 4",
        "num_short": "04",
        "title_zh": "四、怎样方能得重生？",
        "title_en": "How Can One Be Born Again?",
        "desc_zh": "旷野举铜蛇的历史预表；仰望十字架中保耶稣基督；四步信服立时得着永生。",
        "desc_en": "The lifted bronze serpent: Four steps of faith and instantaneous salvation in Christ.",
        "file": "cszy_translation/04_chapter4.md"
    },
    {
        "id": "chapter-5",
        "num": "CHAPTER 5",
        "num_short": "05",
        "title_zh": "五、得了重生的人还能犯罪吗？",
        "title_en": "Can a Person Who Is Born Again Still Sin?",
        "desc_zh": "两性情剧烈交战；羊与猪的本质区别；神赐属灵创伤药；三大仇敌与靠元帅基督得胜。",
        "desc_en": "Warfare of two natures, sheep vs. swine, God's healing balm & more than conquerors in Christ.",
        "file": "cszy_translation/05_chapter5.md"
    }
]

# 7 In-depth Logical Subheadings for Chapter 5
ch5_subheadings = {
    0: (
        "一、问题的核心与普遍的困惑：重生者是否仍有犯罪的可能性？",
        "1. The Core of the Question & Universal Confusion: Does the Possibility of Sinning Remain?"
    ),
    6: (
        "二、使徒约翰的启示：认罪赦免的恩典与神预备的「属灵创伤药」",
        "2. The Apostle John's Revelation: Grace of Confession & God's \"Spiritual Wound Medicine\""
    ),
    30: (
        "三、保罗书信的明证：哥林多与以弗所圣徒的真实警诫",
        "3. Evidence from Paul's Epistles: Apostolic Admonitions to Corinth & Ephesus"
    ),
    47: (
        "四、保罗自身的经历：罗马书七章新旧二人的激烈交战",
        "4. Paul's Personal Experience: The Fierce Warfare Between the Two Natures (Romans 7)"
    ),
    52: (
        "五、辨明难解经文：凡从神生的人不犯罪的属灵真义",
        "5. Clarifying the Difficult Passage: The True Meaning of \"Whoever Is Born of God Does Not Sin\""
    ),
    61: (
        "六、羊与猪的本质比喻：察验信徒对罪的根本态度",
        "6. The Parable of Sheep and Swine: Testing the Regenerate Heart's Attitude Toward Sin"
    ),
    72: (
        "七、两大性情、三大仇敌与靠元帅基督得胜有余",
        "7. Two Conflicting Natures, Three Deadly Foes & More Than Conquerors Through Christ"
    )
}

bible_books = [
    '创', '出', '利', '民', '申', '书', '士', '得', '撒', '王', '代', '拉', '尼', '斯',
    '伯', '诗', '箴', '传', '歌', '赛', '耶', '哀', '结', '但', '何', '珥', '摩', '俄',
    '拿', '弥', '鸿', '哈', '番', '该', '亚', '玛', '太', '可', '路', '约', '徒', '罗',
    '林', '加', '弗', '腓', '西', '帖', '提', '多', '门', '来', '雅', '彼', '壹', '贰',
    '叁', '犹', '启'
]

def is_scripture(zh_text):
    s = zh_text.strip()
    if s.startswith('「') and (s.endswith(')') or s.endswith('）')):
        for b in bible_books:
            if b in s[-25:]:
                return True
    return False

def parse_md_pairs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = text.split('\n---\n')
    pairs = []
    for part in parts[1:]:  # skip document header before first ---
        part = part.strip()
        if not part:
            continue
        m_zh = re.search(r'### 【中文】\s*\n(.*?)(?=\n### 【English】|\Z)', part, re.DOTALL)
        m_en = re.search(r'### 【English】\s*\n(.*)', part, re.DOTALL)
        if m_zh and m_en:
            zh = m_zh.group(1).strip()
            en = m_en.group(1).strip()
            pairs.append((zh, en))
            
    # The first pair in all files is just repeating the chapter title, discard it to avoid redundancy
    if pairs:
        pairs = pairs[1:]
    return pairs

def format_cell_paragraphs(text, is_zh=True, is_scripture_block=False):
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    if not paragraphs:
        return ""
    
    if is_scripture_block:
        inner = "".join([f"<p>{p}</p>" for p in paragraphs])
        return f"<blockquote>{inner}</blockquote>"
    else:
        return "".join([f"<p>{p}</p>" for p in paragraphs])

def generate_reader_html():
    parsed_chapters = []
    for ch in chapters_meta:
        pairs = parse_md_pairs(ch['file'])
        parsed_chapters.append({
            "meta": ch,
            "pairs": pairs
        })
        print(f"Loaded {ch['id']}: {len(pairs)} bilingual text pairs")

    # Build Sidebar Navigation List
    sidebar_nav_html = ""
    for idx, ch in enumerate(parsed_chapters):
        m = ch['meta']
        sidebar_nav_html += f'''
    <li class="nav-item" data-art="{m['id']}">
      <a href="#{m['id']}" class="nav-link">
        <span class="nav-num">{m['num_short']}</span>
        <div class="nav-link-content">
          <div class="nav-title">{m['title_zh']}</div>
          <div class="nav-en">{m['title_en']}</div>
        </div>
      </a>
    </li>
'''

    # Build TOC Overview Grid Cards
    dir_grid_html = ""
    for ch in parsed_chapters:
        m = ch['meta']
        dir_grid_html += f'''
      <a href="#{m['id']}" class="grid-card">
        <div class="grid-card-num">{m['num']}</div>
        <div class="grid-card-title">{m['title_zh']}</div>
        <div class="grid-card-en">{m['title_en']}</div>
        <div class="grid-card-desc">{m['desc_zh']}</div>
      </a>
'''

    # Build Article Sections
    articles_html = ""
    total_chapters = len(parsed_chapters)
    
    for ch_idx, ch in enumerate(parsed_chapters):
        m = ch['meta']
        is_ch5 = (m['id'] == 'chapter-5')
        
        # Navigation buttons
        if ch_idx == 0:
            prev_btn = '<span class="art-nav-disabled">已是全书首卷</span>'
        else:
            prev_m = parsed_chapters[ch_idx - 1]['meta']
            p_id = prev_m['id']
            p_title = prev_m['title_zh'][:10]
            prev_btn = f'<a href="#{p_id}" class="art-nav-btn">← 上一卷：{p_title}</a>'
            
        if ch_idx == total_chapters - 1:
            next_btn = '<a href="#cover" class="art-nav-btn art-home-action">⇡ 回全书顶部</a>'
        else:
            next_m = parsed_chapters[ch_idx + 1]['meta']
            n_id = next_m['id']
            n_title = next_m['title_zh'][:10]
            next_btn = f'<a href="#{n_id}" class="art-nav-btn art-home-action">下一卷：{n_title} →</a>'

        rows_html = f'''
        <div class="bilingual-row row-tags">
          <div class="row-cell"><span class="col-lang-tag tag-zh">🇨🇳 中文原著 · 王明道《重生真意》</span></div>
          <div class="row-cell"><span class="col-lang-tag tag-en">🇬🇧 English Translation · The True Meaning of Being Born Again</span></div>
        </div>
'''
        for p_idx, (zh, en) in enumerate(ch['pairs']):
            subheading_zh_html = ""
            subheading_en_html = ""
            if is_ch5 and p_idx in ch5_subheadings:
                zh_sub, en_sub = ch5_subheadings[p_idx]
                subheading_zh_html = f'<div class="zh-subheading">{zh_sub}</div>'
                subheading_en_html = f'<div class="en-subheading">{en_sub}</div>'

            # Detect scripture quote
            has_scripture = is_scripture(zh)
            zh_rendered = format_cell_paragraphs(zh, is_zh=True, is_scripture_block=has_scripture)
            en_rendered = format_cell_paragraphs(en, is_zh=False, is_scripture_block=has_scripture)

            rows_html += f'''
        <!-- Row {p_idx + 1} -->
        <div class="bilingual-row">
          <div class="row-cell cell-zh">
            {subheading_zh_html}
            {zh_rendered}
          </div>
          <div class="row-cell cell-en">
            {subheading_en_html}
            {en_rendered}
          </div>
        </div>
'''

        articles_html += f'''
    <!-- ==================== {m['num']}: {m['title_zh']} ==================== -->
    <article id="{m['id']}" class="article-section" data-art="{m['id']}">
      <nav class="article-top-nav">
        <a href="index.html" class="article-back-home">🏠 首页</a>
        <span class="article-nav-sep">/</span>
        <a href="#cover" class="article-nav-crumb">《重生真意》</a>
        <span class="article-nav-sep">/</span>
        <span class="article-nav-cur">{m['num']}</span>
      </nav>

      <div class="article-header-wrapper">
        <div class="article-badge-row">
          <span class="article-badge">{m['num']}</span>
          <span class="article-badge-sub">WANG MINGDAO · BILINGUAL EDITION</span>
        </div>
        <div class="bilingual-header-grid">
          <h2 class="article-title">{m['title_zh']}</h2>
          <h3 class="article-title-en">{m['title_en']}</h3>
        </div>
      </div>

      <div class="bilingual-rows-wrapper">
{rows_html}
      </div>

      <div class="article-footer-nav">
        <div class="article-footer-left">
          {prev_btn}
        </div>
        <div class="article-footer-right">
          <a href="#dir-grid-section" class="art-nav-btn">☰ 目录总览</a>
          {next_btn}
        </div>
      </div>
    </article>
'''

    # Assemble complete HTML
    html_output = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>《重生真意》（中英双语权威典藏版）- The True Meaning of Being Born Again · 王明道</title>
<meta name="description" content="中国教会属灵泰斗王明道（Wang Mingdao）里程碑式神学经典《重生真意》（The True Meaning of Being Born Again）中英双语对照权威典藏版。解明从水和圣灵生的真义、人类全然败坏的真相、新生命的活泼证据、十字架中保的仰望与信徒内里属灵交战得胜有余的终极安慰。">
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
    
    --accent-gold: #C98A2C;
    --accent-gold-subtle: rgba(201, 138, 44, 0.12);
    --accent-gold-border: rgba(201, 138, 44, 0.35);
    
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

  *, *::before, *::after {{
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
  }}
  html {{
    scroll-behavior: smooth;
    font-size: 16px;
    max-width: 100vw;
    overflow-x: hidden;
  }}

  body {{
    font-family: var(--font-apple);
    background-color: var(--bg-canvas);
    color: var(--text-primary);
    line-height: 1.8;
    margin: 0;
    padding: 0;
    display: flex;
    max-width: 100vw;
    overflow-x: hidden;
    transition: background-color 0.3s ease, color 0.3s ease;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }}

  /* Smooth Scrollbars */
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
    min-width: 0;
    width: 100%;
    max-width: 1540px;
    padding: 40px 48px 120px 48px;
    min-height: 100vh;
    box-sizing: border-box;
    overflow-x: hidden;
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
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
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
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
  }}
  .section-heading-row {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 12px;
  }}
  .section-h2 {{
    font-size: 20px;
    font-weight: 700;
    margin: 0;
    color: var(--text-primary);
    letter-spacing: -0.02em;
  }}
  .section-h2-sub {{
    font-size: 13px;
    color: var(--text-secondary);
  }}
  .dir-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
    min-width: 0;
    max-width: 100%;
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
    min-width: 0;
  }}
  .grid-card:hover {{
    transform: translateY(-2px);
    border-color: rgba(0, 113, 227, 0.5);
    background: rgba(0, 113, 227, 0.02);
    box-shadow: 0 8px 24px rgba(0, 113, 227, 0.12);
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
    letter-spacing: 0.05em;
  }}
  .grid-card-title {{
    font-size: 15.5px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
    line-height: 1.35;
  }}
  .grid-card-en {{
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 10px;
    line-height: 1.3;
  }}
  .grid-card-desc {{
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.55;
    margin-top: auto;
  }}

  /* Article Containers */
  .article-section {{
    background: var(--bg-card);
    border-radius: 20px;
    border: 1px solid var(--border-color);
    padding: 38px 40px;
    margin-bottom: 40px;
    box-shadow: var(--card-shadow);
    transition: background-color 0.3s ease, border-color 0.3s ease;
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}
  .article-top-nav {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    margin-bottom: 24px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-secondary);
    flex-wrap: wrap;
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
    text-decoration: none;
    color: var(--text-secondary);
  }}
  .article-nav-crumb:hover {{
    color: var(--apple-blue);
  }}
  .article-nav-cur {{
    font-weight: 600;
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
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 36px;
    min-width: 0;
    max-width: 100%;
  }}
  .article-title {{
    font-family: var(--font-apple-display);
    font-size: 26px;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    letter-spacing: -0.025em;
    line-height: 1.3;
    min-width: 0;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}
  .article-title-en {{
    font-size: 22px;
    font-weight: 600;
    color: var(--text-secondary);
    margin: 0;
    letter-spacing: -0.015em;
    line-height: 1.35;
    min-width: 0;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  /* Bilingual Rows Architecture (Locked-Row Alignment) */
  .bilingual-rows-wrapper {{
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-bottom: 24px;
    min-width: 0;
    max-width: 100%;
  }}

  .bilingual-row {{
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 36px;
    align-items: start;
    padding-top: 20px;
    padding-bottom: 24px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    transition: background-color 0.18s ease;
    min-width: 0;
    max-width: 100%;
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

  .row-cell {{
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  .cell-zh {{
    font-family: var(--font-apple);
    text-align: justify;
    text-justify: inter-ideograph;
    font-size: var(--reader-fs-zh, 16.5px);
    line-height: var(--reader-lh-zh, 1.9);
    min-width: 0;
    max-width: 100%;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  .cell-en {{
    font-family: var(--font-en);
    text-align: left;
    font-size: var(--reader-fs-en, 15.5px);
    line-height: var(--reader-lh-en, 1.8);
    min-width: 0;
    max-width: 100%;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  .bilingual-row .zh-subheading:first-child,
  .bilingual-row .en-subheading:first-child {{
    margin-top: 0;
  }}

  .bilingual-row p:first-child {{
    margin-top: 0;
  }}
  .col-lang-tag {{
    font-size: 11px;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 9999px;
    display: inline-block;
    margin-bottom: 14px;
    letter-spacing: 0.02em;
  }}
  .tag-zh {{ background: var(--apple-blue-subtle); color: var(--apple-blue); border: 1px solid rgba(0, 113, 227, 0.2); }}
  .tag-en {{ background: rgba(134, 134, 139, 0.08); color: var(--apple-gray); border: 1px solid rgba(134, 134, 139, 0.2); }}

  /* Subheadings inside columns */
  .zh-subheading {{
    font-size: 18.5px;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 24px;
    margin-bottom: 12px;
    border-left: 3.5px solid var(--apple-blue);
    padding-left: 10px;
    letter-spacing: -0.015em;
    line-height: 1.45;
  }}
  .en-subheading {{
    font-size: 17px;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 24px;
    margin-bottom: 12px;
    border-left: 3.5px solid var(--apple-gray);
    padding-left: 10px;
    font-family: var(--font-en);
    letter-spacing: -0.015em;
    line-height: 1.4;
  }}

  p {{
    margin: 14px 0;
    color: var(--text-primary);
  }}
  blockquote {{
    border-left: 4px solid var(--apple-blue);
    background: rgba(0, 113, 227, 0.05);
    padding: 14px 20px;
    margin: 18px 0;
    color: var(--text-primary);
    border-radius: 0 12px 12px 0;
    font-style: normal;
    line-height: 1.85;
  }}
  body.theme-dark blockquote {{
    background: rgba(41, 151, 255, 0.08);
    border-left-color: var(--apple-blue);
  }}
  body.theme-sepia blockquote {{
    background: rgba(142, 90, 45, 0.08);
    border-left-color: var(--apple-blue);
  }}
  blockquote p {{
    margin: 6px 0;
    color: inherit;
  }}

  /* Article Footer Nav */
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
  body.view-zh-only .cell-en,
  body.view-zh-only .article-title-en {{
    display: none !important;
  }}
  body.view-zh-only .bilingual-row,
  body.view-zh-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

  body.view-en-only .cell-zh,
  body.view-en-only .article-title {{
    display: none !important;
  }}
  body.view-en-only .bilingual-row,
  body.view-en-only .bilingual-header-grid {{
    grid-template-columns: 1fr !important;
  }}

  /* Back to Top */
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
    .sidebar-mobile-close {{
      display: flex;
    }}
    #main-content {{
      margin-left: 0;
      padding: 68px 18px 100px 18px;
      min-width: 0;
      max-width: 100%;
    }}
    .bilingual-row,
    .bilingual-header-grid {{
      grid-template-columns: minmax(0, 1fr) !important;
      gap: 20px !important;
      min-width: 0 !important;
      max-width: 100% !important;
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

    /* Mobile Reading Canvas */
    #main-content {{
      padding: 16px 14px calc(100px + env(safe-area-inset-bottom, 20px)) 14px;
      min-width: 0;
      max-width: 100%;
    }}
    .article-section {{
      padding: 20px 0 28px 0;
      border-radius: 0;
      border: none;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 24px;
      box-shadow: none;
      background: transparent;
      min-width: 0;
      max-width: 100%;
    }}
    .bilingual-row,
    .bilingual-header-grid {{
      grid-template-columns: minmax(0, 1fr) !important;
      gap: 16px !important;
      min-width: 0 !important;
      max-width: 100% !important;
    }}
    .row-cell, .cell-zh, .cell-en {{
      min-width: 0 !important;
      max-width: 100% !important;
      overflow-wrap: anywhere !important;
      word-break: break-word !important;
    }}
    .article-title {{
      font-size: 22px;
      line-height: 1.3;
    }}
    .article-title-en {{
      font-size: 17px;
      line-height: 1.35;
    }}
    .cell-zh {{
      font-size: 18px;
      line-height: 1.95;
      letter-spacing: 0.02em;
    }}
    .cell-en {{
      font-size: 16.5px;
      line-height: 1.82;
      letter-spacing: 0.01em;
    }}
    .cell-zh p, p {{
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
    blockquote {{
      padding: 14px 16px;
      font-size: 16.5px;
      line-height: 1.85;
      border-left-width: 4px;
      margin: 18px 0;
      border-radius: 0 12px 12px 0;
    }}
    .cover-card {{
      padding: 20px 0 24px 0;
      border-radius: 0;
      margin-bottom: 24px;
      border: none;
      border-bottom: 1px solid var(--border-color);
    }}
    .cover-title {{
      font-size: 24px;
      line-height: 1.3;
    }}
    .cover-subtitle {{
      font-size: 14px;
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
    .dir-grid {{
      grid-template-columns: 1fr;
      gap: 12px;
    }}
    .grid-card {{
      padding: 16px 18px;
      border-radius: 14px;
    }}
    #back-to-top {{
      bottom: calc(76px + env(safe-area-inset-bottom, 0px));
      right: 16px;
      width: 40px;
      height: 40px;
      font-size: 16px;
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

  @media (max-width: 360px) {{
    .mobile-reading-dock {{
      padding: 4px 6px;
      gap: 2px;
      width: calc(100% - 16px);
    }}
    .dock-btn {{
      padding: 5px 1px;
      gap: 1px;
    }}
    .dock-icon {{
      font-size: 15px;
    }}
    .dock-label {{
      font-size: 9.5px;
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
    .bilingual-row {{
      grid-template-columns: 1fr 1fr !important;
      gap: 24px !important;
    }}
  }}
</style>
</head>
<body class="view-bilingual">

<div id="progress-bar"></div>

<div id="sidebar-backdrop" class="sidebar-backdrop" onclick="toggleSidebar(false)"></div>

<aside id="sidebar">
  <div class="mac-window-controls">
    <span class="mac-dot mac-close" onclick="toggleSidebar(false)"></span>
    <span class="mac-dot mac-minimize" onclick="toggleSidebar(false)"></span>
    <span class="mac-dot mac-maximize" onclick="toggleSidebar(false)"></span>
    <span class="mac-window-title">Wang Mingdao Works</span>
  </div>

  <div class="sidebar-header">
    <div class="sidebar-badge">CHRISTIAN CLASSIC · 百年经典</div>
    <h1 class="sidebar-title">重生真意</h1>
    <p class="sidebar-subtitle">The True Meaning of Being Born Again</p>
  </div>

  <div class="search-box">
    <input type="text" class="search-input" placeholder="快速检索卷目与要道..." oninput="filterNav(this.value)">
  </div>

  <div class="sidebar-portal-nav">
    <a href="index.html" class="sidebar-portal-btn">
      <span>🏠 智库典藏首页</span>
      <span class="portal-btn-arrow">→</span>
    </a>
    <a href="index.html#bookshelf" class="sidebar-portal-btn">
      <span>📚 典藏文库总览</span>
      <span class="portal-btn-arrow">→</span>
    </a>
  </div>

  <ul class="nav-list">
{sidebar_nav_html}
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
        <img src="regeneration_cover.jpg" alt="重生真意 书影" class="cover-img">
      </div>
      <div class="cover-info-col">
        <span class="cover-badge">CHRISTIAN CLASSIC · 纯正圣道基石</span>
        <h1 class="cover-title">《重生真意》（中英双语权威典藏版）</h1>
        <div class="cover-subtitle">The True Meaning of Being Born Again · 王明道（Wang Mingdao）著</div>
        <div class="cover-meta">
          <strong>著者生平：</strong>王明道（Wang Mingdao，1900–1991），中国现代教会史上最具代表性的属灵领袖与布道家之一。一生持守纯正圣经真道，坚贞不屈，被公认为二十世纪华人教会的属灵灯台与信心榜样。<br>
          <strong>经典价值：</strong>本书深入浅出地解明主耶稣对尼哥底母所论「从水和圣灵而生」的真义；从圣经启示揭示人类全然败坏的真相；详述重生新生命的风中明证；并指明信徒内里属灵交战与靠元帅基督得胜有余的坚实应许。全书神学严谨、牧者心肠流露，是历经考验的教会经典。
        </div>
        <div class="tag-row">
          <span class="theology-tag">圣灵重生</span>
          <span class="theology-tag">全然败坏</span>
          <span class="theology-tag">十架救赎</span>
          <span class="theology-tag">属灵交战</span>
          <span class="theology-tag">得胜有余</span>
          <span class="theology-tag">纯正信仰</span>
        </div>
        <div class="cover-action-row">
          <a href="#chapter-preface" class="cover-action-btn cover-start-btn">📖 开启双语研读</a>
          <a href="index.html" class="cover-action-btn cover-portal-btn">🏠 返回智库首页</a>
        </div>
      </div>
    </div>
  </section>

  <section class="grid-section" id="dir-grid-section">
    <div class="section-heading-row">
      <h2 class="section-h2">全书卷目与要道总览</h2>
      <span class="section-h2-sub">Author's Preface + 5 In-depth Chapters</span>
    </div>
    <div class="dir-grid">
{dir_grid_html}
    </div>
  </section>

{articles_html}

</main>

<div class="mobile-reading-dock" id="mobile-dock">
  <a href="index.html" class="dock-btn dock-home">
    <span class="dock-icon">🏠</span>
    <span class="dock-label">首页</span>
  </a>
  <button class="dock-btn" onclick="toggleSidebar(true)">
    <span class="dock-icon">☰</span>
    <span class="dock-label">目录</span>
  </button>
  <button class="dock-btn" onclick="cycleMobileViewMode()">
    <span class="dock-icon">🌐</span>
    <span class="dock-label" id="dock-view-label">双语</span>
  </button>
  <button class="dock-btn" onclick="cycleFontSize()">
    <span class="dock-icon">Aa</span>
    <span class="dock-label" id="dock-font-label">标准</span>
  </button>
  <button class="dock-btn" onclick="cycleMobileTheme()">
    <span class="dock-icon">🌓</span>
    <span class="dock-label">主题</span>
  </button>
</div>

<button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="返回顶部">↑</button>

<script>
  let currentTheme = localStorage.getItem('regeneration_theme') || 'light';
  let currentView = localStorage.getItem('regeneration_view') || 'bilingual';
  const fontScales = [0.92, 1, 1.12, 1.25];
  let fontScaleIdx = 1;
  const savedFontIdx = localStorage.getItem('regeneration_font_scale_idx');
  if (savedFontIdx !== null) {{
    fontScaleIdx = parseInt(savedFontIdx, 10) || 1;
  }}

  function applyTheme(theme) {{
    document.body.classList.remove('theme-sepia', 'theme-dark');
    document.querySelectorAll('.tool-btn[id^="btn-theme-"]').forEach(b => b.classList.remove('active'));
    
    if (theme === 'sepia') {{
      document.body.classList.add('theme-sepia');
      const b = document.getElementById('btn-theme-sepia');
      if (b) b.classList.add('active');
    }} else if (theme === 'dark') {{
      document.body.classList.add('theme-dark');
      const b = document.getElementById('btn-theme-dark');
      if (b) b.classList.add('active');
    }} else {{
      const b = document.getElementById('btn-theme-light');
      if (b) b.classList.add('active');
    }}
    currentTheme = theme;
    localStorage.setItem('regeneration_theme', theme);
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
    localStorage.setItem('regeneration_view', mode);
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
    localStorage.setItem('regeneration_font_scale_idx', fontScaleIdx);
  }}

  function cycleFontSize() {{
    fontScaleIdx = (fontScaleIdx + 1) % fontScales.length;
    applyFontScale();
  }}

  function toggleSidebar(force) {{
    const sb = document.getElementById('sidebar');
    const bd = document.getElementById('sidebar-backdrop');
    const mc = document.getElementById('main-content');
    
    if (window.innerWidth <= 1024) {{
      const willShow = typeof force === 'boolean' ? force : !sb.classList.contains('show-mobile');
      sb.classList.toggle('show-mobile', willShow);
      bd.classList.toggle('active', willShow);
      document.body.style.overflow = willShow ? 'hidden' : '';
    }} else {{
      sb.classList.toggle('collapsed');
      mc.classList.toggle('expanded');
    }}
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
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    const progress = maxScroll > 0 ? (currentY / maxScroll) * 100 : 0;
    if (progressBar) progressBar.style.width = Math.min(100, Math.max(0, progress)) + '%';

    if (backToTop) {{
      backToTop.style.display = currentY > 400 ? 'flex' : 'none';
    }}

    if (window.innerWidth > 768 && topToolbar && triggerBtn) {{
      if (currentY > 200 && currentY > lastScrollY + 10) {{
        topToolbar.classList.add('toolbar-hidden');
        triggerBtn.classList.add('trigger-visible');
      }} else if (currentY < lastScrollY - 10) {{
        topToolbar.classList.remove('toolbar-hidden');
        triggerBtn.classList.remove('trigger-visible');
      }}
    }}

    if (window.innerWidth <= 768 && mobileDock) {{
      if (currentY > 150 && currentY > lastScrollY + 8) {{
        mobileDock.classList.add('dock-hidden');
      }} else if (currentY < lastScrollY - 8) {{
        mobileDock.classList.remove('dock-hidden');
      }}
    }}

    lastScrollY = currentY;

    // Active sidebar section highlight
    const articles = document.querySelectorAll('article.article-section');
    let currentArtId = null;
    articles.forEach(art => {{
      const rect = art.getBoundingClientRect();
      if (rect.top <= 180 && rect.bottom >= 100) {{
        currentArtId = art.id;
      }}
    }});
    if (currentArtId) {{
      document.querySelectorAll('.nav-list .nav-item').forEach(item => {{
        if (item.getAttribute('data-art') === currentArtId) {{
          item.classList.add('active');
        }} else {{
          item.classList.remove('active');
        }}
      }});
    }}
  }}, {{ passive: true }});

  // Close mobile sidebar upon clicking navigation link
  document.querySelectorAll('.nav-link').forEach(link => {{
    link.addEventListener('click', () => {{
      if (window.innerWidth <= 1024) {{
        toggleSidebar(false);
      }}
    }});
  }});

  // Keyboard navigation shortcuts
  window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 't' || e.key === 'T') cycleMobileTheme();
    if (e.key === 'v' || e.key === 'V') cycleMobileViewMode();
  }});

  // Initialize view and theme states
  applyTheme(currentTheme);
  applyViewMode(currentView);
  applyFontScale();
</script>
</body>
</html>
'''

    out_file = "regeneration_reader.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {out_file} ({len(html_output)} characters)")

if __name__ == "__main__":
    generate_reader_html()
