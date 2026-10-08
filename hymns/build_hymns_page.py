#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《诗歌宝藏》—— 华人教会传唱诗歌选集 页面生成器
构建极简、高贵、响应式的诗歌选集阅读与播放器应用
"""

import os
import json

def generate_hymns_html():
    if os.path.exists('hymns.html'):
        with open('hymns.html', 'r', encoding='utf-8') as f:
            html = f.read()
        import shutil
        os.makedirs('pages_dist/hymns', exist_ok=True)
        os.makedirs('Google云端硬盘上传发布包/hymns', exist_ok=True)
        with open('pages_dist/hymns.html', 'w', encoding='utf-8') as f: f.write(html.strip())
        with open('pages_dist/hymns/index.html', 'w', encoding='utf-8') as f: f.write(html.strip())
        with open('hymns/index.html', 'w', encoding='utf-8') as f: f.write(html.strip())
        with open('Google云端硬盘上传发布包/hymns.html', 'w', encoding='utf-8') as f: f.write(html.strip())
        with open('Google云端硬盘上传发布包/hymns/index.html', 'w', encoding='utf-8') as f: f.write(html.strip())
        if os.path.exists('hymns/hymns_data.js'):
            shutil.copyfile('hymns/hymns_data.js', 'pages_dist/hymns/hymns_data.js')
            shutil.copyfile('hymns/hymns_data.js', 'Google云端硬盘上传发布包/hymns/hymns_data.js')
        print("Successfully synced all hymn files from canonical hymns.html")
        return

    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark-theme">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
<title>诗歌宝藏 · 华人教会传唱诗歌选集</title>
<meta name="description" content="适合华人教会信徒、团契、诗班传唱的经典诗歌选集，包含原版高清简谱歌谱、大字歌词、智能钢琴伴奏与敬拜赞美视频。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">

<style>
  :root {{
    --bg-main: #0B0E14;
    --bg-surface: #141822;
    --bg-surface-elevated: #1C2230;
    --bg-card: #181D29;
    --border-color: rgba(255, 255, 255, 0.08);
    --border-highlight: rgba(245, 158, 11, 0.35);
    
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
    
    --gold-primary: #F59E0B;
    --gold-subtle: rgba(245, 158, 11, 0.12);
    --gold-border: rgba(245, 158, 11, 0.25);
    
    --blue-accent: #38BDF8;
    --blue-subtle: rgba(56, 189, 248, 0.12);
    
    --apple-font: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Serif SC", serif;
    --serif-font: "Noto Serif SC", Georgia, "Songti SC", serif;
    
    --sidebar-width: 340px;
    --header-height: 64px;
    --player-height: 80px;
    --border-radius: 14px;
    --font-size-lyrics: 22px;
    --font-size-score: 18px;
  }}

  /* Light Theme */
  html.light-theme {{
    --bg-main: #F8F9FA;
    --bg-surface: #FFFFFF;
    --bg-surface-elevated: #F1F5F9;
    --bg-card: #FFFFFF;
    --border-color: rgba(0, 0, 0, 0.08);
    --border-highlight: rgba(217, 119, 6, 0.3);
    
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-muted: #94A3B8;
    
    --gold-primary: #D97706;
    --gold-subtle: rgba(217, 119, 6, 0.08);
    --gold-border: rgba(217, 119, 6, 0.2);
    
    --blue-accent: #0284C7;
    --blue-subtle: rgba(2, 132, 199, 0.08);
  }}

  /* Sepia Theme */
  html.sepia-theme {{
    --bg-main: #F4EFE6;
    --bg-surface: #FCFAF6;
    --bg-surface-elevated: #ECE5DA;
    --bg-card: #FCFAF6;
    --border-color: rgba(120, 53, 15, 0.1);
    --border-highlight: rgba(180, 83, 9, 0.3);
    
    --text-primary: #291E13;
    --text-secondary: #574433;
    --text-muted: #87715F;
    
    --gold-primary: #B45309;
    --gold-subtle: rgba(180, 83, 9, 0.1);
    --gold-border: rgba(180, 83, 9, 0.25);
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
  }}

  body {{
    background: var(--bg-main);
    color: var(--text-primary);
    font-family: var(--apple-font);
    line-height: 1.6;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    transition: background 0.3s ease, color 0.3s ease;
  }}

  /* Global Top Navigation Bar */
  .app-header {{
    position: sticky;
    top: 0;
    z-index: 100;
    height: var(--header-height);
    background: rgba(11, 14, 20, 0.85);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    transition: background 0.3s ease, border-color 0.3s ease;
  }}

  html.light-theme .app-header {{
    background: rgba(255, 255, 255, 0.88);
  }}
  html.sepia-theme .app-header {{
    background: rgba(244, 239, 230, 0.9);
  }}

  .header-left {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .btn-sidebar-toggle {{
    background: var(--bg-surface-elevated);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 7px 12px;
    border-radius: 9px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }}
  .btn-sidebar-toggle:hover {{
    border-color: var(--gold-primary);
    color: var(--gold-primary);
  }}

  .app-brand {{
    display: flex;
    align-items: baseline;
    gap: 8px;
    text-decoration: none;
  }}
  .brand-title {{
    font-family: var(--serif-font);
    font-size: 20px;
    font-weight: 900;
    color: var(--gold-primary);
    letter-spacing: 0.5px;
  }}
  .brand-sub {{
    font-size: 12px;
    color: var(--text-muted);
    font-weight: 500;
  }}

  .header-right {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .header-btn {{
    background: var(--bg-surface-elevated);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 7px 12px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: all 0.2s;
  }}
  .header-btn:hover {{
    background: var(--gold-subtle);
    border-color: var(--gold-border);
    color: var(--gold-primary);
  }}
  .header-btn.btn-home {{
    color: var(--blue-accent);
    background: var(--blue-subtle);
    border-color: rgba(56, 189, 248, 0.25);
  }}

  /* Main Container Layout */
  .app-container {{
    display: flex;
    flex: 1;
    height: calc(100vh - var(--header-height) - var(--player-height));
    position: relative;
    overflow: hidden;
  }}

  /* Sidebar Catalog Drawer */
  .sidebar-catalog {{
    width: var(--sidebar-width);
    background: var(--bg-surface);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    z-index: 50;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background 0.3s;
  }}

  .sidebar-search-box {{
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-color);
    background: var(--bg-surface);
  }}
  .search-input-wrapper {{
    position: relative;
    display: flex;
    align-items: center;
  }}
  .search-input-wrapper .search-icon {{
    position: absolute;
    left: 12px;
    color: var(--text-muted);
    font-size: 14px;
    pointer-events: none;
  }}
  .search-input {{
    width: 100%;
    padding: 9px 12px 9px 36px;
    background: var(--bg-surface-elevated);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    color: var(--text-primary);
    font-size: 13.5px;
    outline: none;
    transition: all 0.2s;
  }}
  .search-input:focus {{
    border-color: var(--gold-primary);
    background: var(--bg-card);
    box-shadow: 0 0 0 3px var(--gold-subtle);
  }}

  /* Category Filter Pills */
  .category-filter-bar {{
    display: flex;
    gap: 6px;
    padding: 10px 16px;
    overflow-x: auto;
    border-bottom: 1px solid var(--border-color);
    scrollbar-width: none;
  }}
  .category-filter-bar::-webkit-scrollbar {{
    display: none;
  }}
  .cat-pill {{
    flex-shrink: 0;
    padding: 4px 11px;
    border-radius: 20px;
    font-size: 12px;
    border: 1px solid var(--border-color);
    background: transparent;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s;
  }}
  .cat-pill:hover {{
    color: var(--text-primary);
    border-color: var(--text-muted);
  }}
  .cat-pill.active {{
    background: var(--gold-primary);
    color: #000000;
    font-weight: 600;
    border-color: var(--gold-primary);
  }}

  /* Hymns List */
  .hymn-list {{
    flex: 1;
    overflow-y: auto;
    list-style: none;
    padding: 8px 10px;
  }}
  .hymn-item {{
    padding: 12px 14px;
    margin-bottom: 6px;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: all 0.2s ease;
    border: 1px solid transparent;
  }}
  .hymn-item:hover {{
    background: var(--bg-surface-elevated);
    border-color: var(--border-color);
  }}
  .hymn-item.active {{
    background: var(--gold-subtle);
    border-color: var(--gold-border);
  }}
  .hymn-item-left {{
    display: flex;
    align-items: center;
    gap: 12px;
    overflow: hidden;
  }}
  .hymn-num-badge {{
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: var(--bg-surface-elevated);
    border: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: var(--serif-font);
    font-weight: 700;
    color: var(--gold-primary);
    font-size: 15px;
    flex-shrink: 0;
  }}
  .hymn-item.active .hymn-num-badge {{
    background: var(--gold-primary);
    color: #000;
  }}
  .hymn-info {{
    overflow: hidden;
  }}
  .hymn-item-title {{
    font-size: 15px;
    font-weight: 600;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .hymn-item-meta {{
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
    display: flex;
    gap: 6px;
  }}
  .hymn-item-right {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .playing-wave {{
    display: none;
    align-items: flex-end;
    gap: 2px;
    height: 14px;
  }}
  .hymn-item.is-playing .playing-wave {{
    display: flex;
  }}
  .wave-bar {{
    width: 2.5px;
    height: 100%;
    background: var(--gold-primary);
    animation: waveBounce 0.8s infinite ease-in-out alternate;
  }}
  .wave-bar:nth-child(2) {{ animation-delay: 0.2s; }}
  .wave-bar:nth-child(3) {{ animation-delay: 0.4s; }}
  @keyframes waveBounce {{
    0% {{ height: 3px; }}
    100% {{ height: 14px; }}
  }}

  /* Main Viewing Stage */
  .stage-content {{
    flex: 1;
    overflow-y: auto;
    padding: 24px 32px 48px;
    background: var(--bg-main);
    display: flex;
    flex-direction: column;
    align-items: center;
  }}

  .stage-inner {{
    width: 100%;
    max-width: 820px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }}

  /* Hymn Header Card */
  .hymn-detail-header {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 22px 26px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  }}

  .detail-top-tags {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
  }}
  .tag-group {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .pill-badge {{
    font-size: 12px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
  }}
  .pill-gold {{
    background: var(--gold-subtle);
    color: var(--gold-primary);
    border: 1px solid var(--gold-border);
  }}
  .pill-blue {{
    background: var(--blue-subtle);
    color: var(--blue-accent);
    border: 1px solid rgba(56, 189, 248, 0.25);
  }}

  .hymn-headline-row {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 8px;
  }}
  .hymn-main-title {{
    font-family: var(--serif-font);
    font-size: 28px;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: 0.5px;
  }}
  .hymn-main-num {{
    font-family: var(--serif-font);
    font-size: 20px;
    color: var(--gold-primary);
    font-weight: 700;
  }}

  .hymn-meta-line {{
    font-size: 13.5px;
    color: var(--text-secondary);
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 4px;
  }}

  .hymn-bg-desc {{
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px dashed var(--border-color);
    font-size: 13.5px;
    color: var(--text-secondary);
    line-height: 1.6;
  }}

  /* Action Buttons Toolbar in Detail Card */
  .hymn-actions-bar {{
    margin-top: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}

  .action-btn {{
    padding: 8px 16px;
    border-radius: 9px;
    font-size: 13.5px;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border: 1px solid var(--border-color);
    background: var(--bg-surface-elevated);
    color: var(--text-primary);
    transition: all 0.2s;
  }}
  .action-btn:hover {{
    border-color: var(--gold-primary);
    color: var(--gold-primary);
    transform: translateY(-1px);
  }}
  .action-btn.btn-play-primary {{
    background: var(--gold-primary);
    color: #000;
    border-color: var(--gold-primary);
  }}
  .action-btn.btn-play-primary:hover {{
    filter: brightness(1.1);
  }}
  .action-btn.btn-video {{
    color: #EF4444;
    background: rgba(239, 68, 68, 0.1);
    border-color: rgba(239, 68, 68, 0.25);
  }}
  .action-btn.btn-video:hover {{
    background: rgba(239, 68, 68, 0.2);
    border-color: #EF4444;
  }}

  /* Mode Switch Bar (Score vs Lyrics) */
  .view-mode-tabs {{
    display: inline-flex;
    background: rgba(120, 120, 128, 0.08);
    padding: 3px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    gap: 3px;
  }}
  .mode-tab {{
    padding: 5px 14px;
    border-radius: 6px;
    border: none;
    background: transparent;
    color: var(--text-secondary);
    font-family: var(--apple-font);
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .mode-tab.active {{
    background: #E5E7EB;
    color: #111827;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
  }}
  html.dark-theme .mode-tab.active {{
    background: #2D3748;
    color: #F9FAFB;
  }}

  /* Text Score Viewer Card (纯文字简谱视窗) */
  .text-score-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 24px 28px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.2);
    position: relative;
    overflow: hidden;
    transition: background 0.3s, border-color 0.3s;
  }}
  .score-card-toolbar {{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 20px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border-color);
  }}
  .score-ctrl-actions {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    gap: 12px;
    flex-wrap: wrap;
  }}
  .score-sub-tabs {{
    display: inline-flex;
    background: rgba(120, 120, 128, 0.08);
    padding: 3px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    gap: 3px;
  }}
  .sub-tab-btn {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-family: var(--apple-font);
    font-size: 12.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .sub-tab-btn.active {{
    background: #E5E7EB;
    color: #111827;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06);
  }}
  html.dark-theme .sub-tab-btn.active {{
    background: #2D3748;
    color: #F9FAFB;
  }}
  .score-font-ctrls {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .font-ctrl-label {{
    font-size: 12.5px;
    font-weight: 700;
    color: var(--text-muted);
  }}
  .font-ctrl-btn {{
    background: #F3F4F6;
    color: #111827;
    border: 1px solid rgba(0, 0, 0, 0.1);
    font-family: var(--apple-font);
    font-weight: 700;
    min-width: 30px;
    height: 30px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.15s;
    padding: 0 8px;
  }}
  html.dark-theme .font-ctrl-btn {{
    background: #262E3D;
    color: #E2E8F0;
    border-color: rgba(255, 255, 255, 0.1);
  }}
  .font-ctrl-btn:hover {{
    background: #E5E7EB;
    color: #000000;
  }}
  html.dark-theme .font-ctrl-btn:hover {{
    background: #374151;
    color: #FFFFFF;
  }}
  .copy-score-btn {{
    width: auto !important;
    padding: 0 12px !important;
    font-family: var(--apple-font);
    font-weight: 700;
  }}

  /* ============================================================
     Unified Single-Page Vector Sheet Music (整版自适应矢量歌谱)
     整曲同一大版面呈现 · 绝不换行断节 · 手机平板电脑全自适应
     ============================================================ */
  .score-formatted-container {{
    width: 100%;
    display: flex;
    justify-content: center;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding: 6px 0 16px;
  }}
  .unified-score-sheet {{
    width: 100%;
    max-width: 860px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 24px 28px 36px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.25);
    transition: background 0.3s, border-color 0.3s;
    box-sizing: border-box;
  }}
  .unified-score-svg {{
    width: 100%;
    height: auto;
    display: block;
  }}
  /* Vector Sheet Classes mapped to Theme Variables */
  .sc-num {{
    font-size: 26px;
    font-weight: 800;
    font-family: var(--serif-font);
    fill: var(--gold-primary);
  }}
  .sc-title {{
    font-size: 22px;
    font-weight: 700;
    font-family: var(--serif-font);
    text-anchor: middle;
    fill: var(--text-primary);
  }}
  .sc-meta {{
    font-size: 13.5px;
    font-family: var(--apple-font);
    fill: var(--text-secondary);
  }}
  .sc-author {{
    font-size: 12px;
    font-family: var(--apple-font);
    text-anchor: end;
    fill: var(--text-muted);
  }}
  .sc-sub {{
    font-size: 14px;
    font-family: var(--serif-font);
    text-anchor: end;
    fill: var(--gold-primary);
    font-weight: 600;
  }}
  .sc-divider {{
    stroke: var(--border-color);
    stroke-width: 1;
  }}
  .sc-pill-bg {{
    fill: var(--gold-subtle);
    stroke: var(--gold-border);
    stroke-width: 0.8;
    rx: 4;
  }}
  .sc-pill {{
    font-size: 11px;
    font-weight: 700;
    font-family: var(--apple-font);
    fill: var(--gold-primary);
    letter-spacing: 0.5px;
  }}
  .sc-note {{
    font-size: 19px;
    font-weight: 700;
    font-family: var(--apple-font);
    text-anchor: middle;
    fill: var(--text-primary);
    user-select: none;
  }}
  .sc-dot {{
    fill: var(--text-primary);
  }}
  .sc-uline {{
    stroke: var(--text-primary);
    stroke-width: 1.8;
    stroke-linecap: round;
  }}
  .sc-slur {{
    stroke: var(--text-primary);
    stroke-width: 1.2;
    fill: none;
    opacity: 0.8;
  }}
  .sc-bar {{
    stroke: var(--text-muted);
    stroke-width: 1.2;
    opacity: 0.65;
  }}
  .sc-dbar {{
    stroke: var(--text-muted);
    stroke-width: 2.8;
    opacity: 0.85;
  }}
  .sc-stave-sep {{
    stroke: var(--border-color);
    stroke-width: 0.8;
    stroke-dasharray: 4,4;
    opacity: 0.35;
  }}
  .sc-lyric,
  .sc-v1,
  .sc-v2,
  .sc-v3 {{
    font-size: 14.5px;
    font-family: var(--apple-font);
    text-anchor: middle;
    letter-spacing: 0px;
    fill: var(--text-primary) !important;
    font-weight: 500;
  }}
  .sc-verse-prefix {{
    font-size: 11px;
    font-family: var(--apple-font);
    font-weight: 700;
    fill: var(--text-muted);
  }}
  .sc-lyric-punct {{
    font-size: 13px;
    font-family: var(--apple-font);
    font-weight: 500;
    fill: var(--text-secondary);
  }}
  .verse-filter-btn {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 11.5px;
    font-weight: 600;
    padding: 3px 7px;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .verse-filter-btn.active {{
    background: var(--bg-card);
    color: var(--gold-primary);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
  }}
  .score-verse-filter {{
    display: inline-flex;
    align-items: center;
    background: var(--bg-surface);
    padding: 2px 4px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    gap: 2px;
  }}

  /* Score Raw Pre View (纯文本简谱) */
  .score-raw-container {{
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }}
  .raw-score-pre {{
    font-family: ui-monospace, "SF Mono", Monaco, Menlo, Consolas, "Courier New", monospace;
    font-size: var(--font-size-score, 18px);
    line-height: 1.7;
    color: var(--text-primary);
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 22px;
    white-space: pre;
    overflow-x: auto;
    letter-spacing: 0.5px;
    tab-size: 4;
  }}

  /* Lyrics Viewer Card */
  .lyrics-viewer-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px 36px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  }}

  .lyrics-toolbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-color);
  }}
  .font-size-ctrls {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .font-ctrl-btn {{
    width: 28px;
    height: 28px;
    border-radius: 6px;
    border: 1px solid var(--border-color);
    background: var(--bg-surface-elevated);
    color: var(--text-primary);
    cursor: pointer;
    font-size: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
  }}
  .font-ctrl-btn:hover {{
    border-color: var(--gold-primary);
    color: var(--gold-primary);
  }}

  .lyrics-content-body {{
    font-family: var(--serif-font);
    font-size: var(--font-size-lyrics);
    line-height: 2.1;
    color: var(--text-primary);
  }}

  .lyrics-section-block {{
    margin-bottom: 28px;
  }}
  .lyrics-section-badge {{
    display: inline-block;
    font-family: var(--apple-font);
    font-size: 13px;
    font-weight: 700;
    color: var(--gold-primary);
    background: var(--gold-subtle);
    padding: 2px 10px;
    border-radius: 5px;
    margin-bottom: 8px;
    border: 1px solid var(--gold-border);
  }}
  .lyrics-line {{
    margin-bottom: 4px;
    letter-spacing: 0.5px;
  }}
  .lyrics-note-hint {{
    font-size: 14px;
    color: var(--text-muted);
    font-style: italic;
    margin-top: 10px;
  }}

  /* Video Modal / Floating Video */
  .video-modal-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(10px);
    z-index: 2000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .video-modal-backdrop.open {{
    display: flex;
  }}
  .video-modal-content {{
    width: 100%;
    max-width: 860px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
  }}
  .video-modal-header {{
    padding: 14px 20px;
    background: var(--bg-surface-elevated);
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
  }}
  .video-modal-title {{
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
  }}
  .video-modal-close {{
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 20px;
    cursor: pointer;
  }}
  .video-modal-close:hover {{
    color: #EF4444;
  }}
  .video-embed-box {{
    position: relative;
    padding-bottom: 56.25%; /* 16:9 ratio */
    height: 0;
    background: #000;
  }}
  .video-embed-box iframe {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
  }}


  /* Sticky Bottom Multimedia Player Bar */
  .app-player-bar {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: var(--player-height);
    background: rgba(18, 22, 31, 0.94);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-top: 1px solid var(--border-color);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    transition: background 0.3s;
  }}
  html.light-theme .app-player-bar {{
    background: rgba(255, 255, 255, 0.95);
  }}
  html.sepia-theme .app-player-bar {{
    background: rgba(244, 239, 230, 0.96);
  }}

  .player-track-info {{
    display: flex;
    align-items: center;
    gap: 14px;
    width: 250px;
    overflow: hidden;
  }}
  .player-track-badge {{
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: var(--gold-subtle);
    border: 1px solid var(--gold-border);
    color: var(--gold-primary);
    font-family: var(--serif-font);
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    flex-shrink: 0;
  }}
  .player-track-meta {{
    overflow: hidden;
  }}
  .player-track-name {{
    font-size: 14.5px;
    font-weight: 700;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .player-track-sub {{
    font-size: 12px;
    color: var(--text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  /* Player Middle Controls */
  .player-center-controls {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    flex: 1;
    max-width: 520px;
  }}

  .player-btn-row {{
    display: flex;
    align-items: center;
    gap: 18px;
  }}

  .ctrl-icon-btn {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 17px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: color 0.2s;
  }}
  .ctrl-icon-btn:hover {{
    color: var(--text-primary);
  }}
  .ctrl-play-main {{
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--gold-primary);
    color: #000000;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    cursor: pointer;
    transition: transform 0.2s, filter 0.2s;
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4);
  }}
  .ctrl-play-main:hover {{
    transform: scale(1.05);
    filter: brightness(1.1);
  }}

  /* Progress Bar */
  .player-progress-row {{
    display: flex;
    align-items: center;
    gap: 10px;
    width: 100%;
  }}
  .time-text {{
    font-size: 11.5px;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
    width: 38px;
  }}
  .progress-slider-container {{
    flex: 1;
    height: 5px;
    background: var(--bg-surface-elevated);
    border-radius: 5px;
    position: relative;
    cursor: pointer;
  }}
  .progress-bar-fill {{
    height: 100%;
    width: 0%;
    background: var(--gold-primary);
    border-radius: 5px;
    position: relative;
  }}
  .progress-slider-container:hover .progress-bar-fill::after {{
    content: '';
    position: absolute;
    right: -5px;
    top: -3px;
    width: 11px;
    height: 11px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
  }}

  /* Player Right Controls */
  .player-right-controls {{
    display: flex;
    align-items: center;
    gap: 12px;
    width: 250px;
    justify-content: flex-end;
  }}
  .audio-type-pill {{
    font-size: 11.5px;
    padding: 3px 8px;
    border-radius: 6px;
    background: var(--gold-subtle);
    color: var(--gold-primary);
    border: 1px solid var(--gold-border);
    cursor: pointer;
  }}

  /* Backdrop for mobile sidebar */
  .sidebar-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    z-index: 40;
    display: none;
  }}
  .sidebar-backdrop.active {{
    display: block;
  }}

  /* Responsive Adjustments */
  @media (max-width: 900px) {{
    .sidebar-catalog {{
      position: fixed;
      top: var(--header-height);
      left: 0;
      bottom: var(--player-height);
      height: auto;
      transform: translateX(-100%);
      box-shadow: 10px 0 30px rgba(0, 0, 0, 0.5);
    }}
    .sidebar-catalog.open {{
      transform: translateX(0);
    }}
    .stage-content {{
      padding: 16px 14px 40px;
    }}
    .hymn-detail-header {{
      padding: 16px;
    }}
    .hymn-main-title {{
      font-size: 22px;
    }}
    .text-score-card {{
      padding: 18px 14px;
    }}
    .score-card-toolbar {{
      flex-direction: column;
      align-items: flex-start;
      gap: 12px;
    }}
    .score-ctrl-actions {{
      width: 100%;
      justify-content: space-between;
      flex-wrap: wrap;
    }}
    .lyrics-viewer-card {{
      padding: 20px 18px;
    }}
    .player-track-info {{
      width: 160px;
    }}
    .player-right-controls {{
      width: auto;
    }}
    .player-right-controls .vol-slider {{
      display: none;
    }}
  }}

  @media (max-width: 600px) {{
    .app-header {{
      padding: 0 12px;
    }}
    .brand-sub {{
      display: none;
    }}
    .view-mode-tabs {{
      width: 100%;
      margin-top: 10px;
      justify-content: center;
    }}
    .hymn-actions-bar {{
      justify-content: flex-start;
    }}
    .action-btn {{
      padding: 6px 12px;
      font-size: 12.5px;
    }}
    .player-track-sub {{
      display: none;
    }}
    .player-track-info {{
      width: 120px;
    }}
    .text-score-card {{
      padding: 14px 6px;
    }}
    .score-formatted-container {{
      padding: 0 0 10px;
    }}
    .unified-score-sheet {{
      padding: 14px 6px 20px;
      border-radius: 6px;
    }}
  }}
</style>
</head>

<body>

<!-- Header -->
<header class="app-header">
  <div class="header-left">
    <button class="btn-sidebar-toggle" onclick="toggleSidebar()" title="展开/收起歌单">
      <span>☰ 歌单</span>
    </button>
    <a href="hymns.html" class="app-brand">
      <span class="brand-title">诗歌宝藏</span>
      <span class="brand-sub">华人教会传唱诗歌选集</span>
    </a>
  </div>

  <div class="header-right">
    <button class="header-btn" onclick="toggleTheme()" title="切换明亮/深色模式">
      <span id="theme-btn-icon">🌓</span> 外观
    </button>
    <a href="index.html" class="header-btn btn-home" title="返回 Evan's Thinking 首页">
      <span>🏠 返回主站</span>
    </a>
  </div>
</header>

<!-- App Main Container -->
<div class="app-container">
  
  <!-- Backdrop for mobile drawer -->
  <div class="sidebar-backdrop" id="sidebar-backdrop" onclick="toggleSidebar(false)"></div>

  <!-- Left Sidebar Catalog -->
  <aside class="sidebar-catalog" id="sidebar-catalog">
    <div class="sidebar-search-box">
      <div class="search-input-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="hymn-search-input" class="search-input" placeholder="输入首号、歌名、或歌词..." oninput="handleSearch(this.value)">
      </div>
    </div>

    <ul class="hymn-list" id="hymn-list">
      <!-- Generated Dynamically by JS -->
    </ul>
  </aside>

  <!-- Right Stage Content -->
  <main class="stage-content" id="stage-content">
    <div class="stage-inner">
      
      <!-- Current Hymn Header Card -->
      <section class="hymn-detail-header" id="hymn-header-card">
        <div class="hymn-headline-row">
          <h1 class="hymn-main-title" id="disp-title">是谁从远处看见认识我</h1>

          <!-- Mode Tabs: 歌谱模式 / 歌词模式 -->
          <div class="view-mode-tabs">
            <button class="mode-tab active" id="tab-score" onclick="switchViewMode('score')">歌谱模式</button>
            <button class="mode-tab" id="tab-lyrics" onclick="switchViewMode('lyrics')">歌词模式</button>
          </div>
        </div>
      </section>

      <!-- Text Score Viewer Card -->
      <section class="text-score-card" id="score-viewer-panel">
        <!-- Formatted Staves -->
        <div class="score-formatted-container" id="disp-score-formatted">
<div class="unified-score-sheet" style="max-width: 860px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 544" width="100%" height="auto" class="unified-score-svg" style="display:block; overflow:visible;"><text x="36" y="38" class="sc-meta" style="font-size: 15px; font-weight: 600;">1=G  4/4</text><text x="380" y="38" class="sc-title">是谁从远处看见认识我</text><line x1="36" y1="52" x2="724" y2="52" class="sc-divider" /><text x="49.76" y="92" class="sc-note">6</text><circle cx="49.76" cy="103" r="1.8" class="sc-dot" /><line x1="41.26" y1="97" x2="58.26" y2="97" class="sc-uline" /><text x="40.76" y="117" class="sc-verse-prefix" text-anchor="end">1.</text><text x="49.76" y="117" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="40.76" y="136" class="sc-verse-prefix" text-anchor="end">2.</text><text x="49.76" y="136" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="40.76" y="155" class="sc-verse-prefix" text-anchor="end">3.</text><text x="49.76" y="155" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="77.28" y="92" class="sc-note">7</text><circle cx="77.28" cy="103" r="1.8" class="sc-dot" /><line x1="68.78" y1="97" x2="85.78" y2="97" class="sc-uline" /><path d="M 47.76 75 Q 63.519999999999996 70 79.28 75" class="sc-slur" /><text x="104.8" y="92" class="sc-note">1</text><text x="104.8" y="117" class="sc-lyric sc-v1" text-anchor="middle">谁</text><text x="104.8" y="136" class="sc-lyric sc-v2" text-anchor="middle">谁</text><text x="104.8" y="155" class="sc-lyric sc-v3" text-anchor="middle">谁</text><text x="132.32" y="92" class="sc-note">1</text><line x1="123.82" y1="97" x2="140.82" y2="97" class="sc-uline" /><text x="132.32" y="117" class="sc-lyric sc-v1" text-anchor="middle">从</text><text x="132.32" y="136" class="sc-lyric sc-v2" text-anchor="middle">从</text><text x="132.32" y="155" class="sc-lyric sc-v3" text-anchor="middle">担</text><text x="159.84" y="92" class="sc-note">2</text><line x1="151.34" y1="97" x2="168.34" y2="97" class="sc-uline" /><text x="159.84" y="117" class="sc-lyric sc-v1" text-anchor="middle">远</text><text x="159.84" y="136" class="sc-lyric sc-v2" text-anchor="middle">灰</text><text x="159.84" y="155" class="sc-lyric sc-v3" text-anchor="middle">当</text><text x="187.36" y="92" class="sc-note">3</text><line x1="178.86" y1="97" x2="195.86" y2="97" class="sc-uline" /><text x="187.36" y="117" class="sc-lyric sc-v1" text-anchor="middle">处</text><text x="187.36" y="136" class="sc-lyric sc-v2" text-anchor="middle">尘</text><text x="187.36" y="155" class="sc-lyric sc-v3" text-anchor="middle">全</text><text x="214.88" y="92" class="sc-note">3</text><line x1="206.38" y1="97" x2="223.38" y2="97" class="sc-uline" /><text x="214.88" y="117" class="sc-lyric sc-v1" text-anchor="middle">看</text><text x="214.88" y="136" class="sc-lyric sc-v2" text-anchor="middle">中</text><text x="214.88" y="155" class="sc-lyric sc-v3" text-anchor="middle">人</text><text x="242.4" y="92" class="sc-note">2</text><line x1="233.9" y1="97" x2="250.9" y2="97" class="sc-uline" /><text x="242.4" y="117" class="sc-lyric sc-v1" text-anchor="middle">见</text><text x="242.4" y="136" class="sc-lyric sc-v2" text-anchor="middle">抬</text><text x="242.4" y="155" class="sc-lyric sc-v3" text-anchor="middle">类</text><text x="269.92" y="92" class="sc-note">1</text><line x1="261.42" y1="97" x2="278.42" y2="97" class="sc-uline" /><text x="269.92" y="117" class="sc-lyric sc-v1" text-anchor="middle">认</text><text x="269.92" y="136" class="sc-lyric sc-v2" text-anchor="middle">举</text><text x="269.92" y="155" class="sc-lyric sc-v3" text-anchor="middle">的</text><text x="297.44" y="92" class="sc-note">2</text><text x="297.44" y="117" class="sc-lyric sc-v1" text-anchor="middle">识</text><text x="297.44" y="136" class="sc-lyric sc-v2" text-anchor="middle">了</text><text x="297.44" y="155" class="sc-lyric sc-v3" text-anchor="middle">刑</text><text x="324.96000000000004" y="92" class="sc-note">5</text><circle cx="324.96000000000004" cy="103" r="1.8" class="sc-dot" /><line x1="316.46000000000004" y1="97" x2="333.46000000000004" y2="97" class="sc-uline" /><text x="324.96000000000004" y="117" class="sc-lyric sc-v1" text-anchor="middle">我</text><text x="332.96000000000004" y="117" class="sc-lyric-punct" text-anchor="start">？</text><text x="324.96000000000004" y="136" class="sc-lyric sc-v2" text-anchor="middle">我</text><text x="332.96000000000004" y="136" class="sc-lyric-punct" text-anchor="start">？</text><text x="324.96000000000004" y="155" class="sc-lyric sc-v3" text-anchor="middle">罚</text><text x="332.96000000000004" y="155" class="sc-lyric-punct" text-anchor="start">？</text><text x="352.48" y="92" class="sc-note">5</text><circle cx="352.48" cy="100" r="1.8" class="sc-dot" /><path d="M 295.44 75 Q 324.96000000000004 68.3952 354.48 75" class="sc-slur" /><text x="380" y="92" class="sc-note">-</text><text x="407.52" y="92" class="sc-note">1</text><circle cx="407.52" cy="103" r="1.8" class="sc-dot" /><line x1="399.02" y1="97" x2="416.02" y2="97" class="sc-uline" /><text x="407.52" y="117" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="407.52" y="136" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="407.52" y="155" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="435.03999999999996" y="92" class="sc-note">7</text><circle cx="435.03999999999996" cy="103" r="1.8" class="sc-dot" /><line x1="426.53999999999996" y1="97" x2="443.53999999999996" y2="97" class="sc-uline" /><path d="M 405.52 75 Q 421.28 70 437.03999999999996 75" class="sc-slur" /><text x="462.56" y="92" class="sc-note">6</text><circle cx="462.56" cy="100" r="1.8" class="sc-dot" /><text x="462.56" y="117" class="sc-lyric sc-v1" text-anchor="middle">谁</text><text x="462.56" y="136" class="sc-lyric sc-v2" text-anchor="middle">谁</text><text x="462.56" y="155" class="sc-lyric sc-v3" text-anchor="middle">谁</text><text x="490.08000000000004" y="92" class="sc-note">6</text><circle cx="490.08000000000004" cy="103" r="1.8" class="sc-dot" /><line x1="481.58000000000004" y1="97" x2="498.58000000000004" y2="97" class="sc-uline" /><text x="490.08000000000004" y="117" class="sc-lyric sc-v1" text-anchor="middle">千</text><text x="490.08000000000004" y="136" class="sc-lyric sc-v2" text-anchor="middle">从</text><text x="490.08000000000004" y="155" class="sc-lyric sc-v3" text-anchor="middle">要</text><text x="517.6" y="92" class="sc-note">7</text><circle cx="517.6" cy="103" r="1.8" class="sc-dot" /><line x1="509.1" y1="97" x2="526.1" y2="97" class="sc-uline" /><text x="517.6" y="117" class="sc-lyric sc-v1" text-anchor="middle">万</text><text x="517.6" y="136" class="sc-lyric sc-v2" text-anchor="middle">粪</text><text x="517.6" y="155" class="sc-lyric sc-v3" text-anchor="middle">洗</text><text x="545.12" y="92" class="sc-note">1</text><line x1="536.62" y1="97" x2="553.62" y2="97" class="sc-uline" /><text x="545.12" y="117" class="sc-lyric sc-v1" text-anchor="middle">人</text><text x="545.12" y="136" class="sc-lyric sc-v2" text-anchor="middle">堆</text><text x="545.12" y="155" class="sc-lyric sc-v3" text-anchor="middle">净</text><text x="572.64" y="92" class="sc-note">1</text><line x1="564.14" y1="97" x2="581.14" y2="97" class="sc-uline" /><text x="572.64" y="117" class="sc-lyric sc-v1" text-anchor="middle">中</text><text x="572.64" y="136" class="sc-lyric sc-v2" text-anchor="middle">中</text><text x="572.64" y="155" class="sc-lyric sc-v3" text-anchor="middle">全</text><text x="600.1600000000001" y="92" class="sc-note">7</text><circle cx="600.1600000000001" cy="103" r="1.8" class="sc-dot" /><line x1="591.6600000000001" y1="97" x2="608.6600000000001" y2="97" class="sc-uline" /><text x="600.1600000000001" y="117" class="sc-lyric sc-v1" text-anchor="middle">题</text><text x="600.1600000000001" y="136" class="sc-lyric sc-v2" text-anchor="middle">提</text><text x="600.1600000000001" y="155" class="sc-lyric sc-v3" text-anchor="middle">人</text><text x="627.6800000000001" y="92" class="sc-note">6</text><circle cx="627.6800000000001" cy="103" r="1.8" class="sc-dot" /><line x1="619.1800000000001" y1="97" x2="636.1800000000001" y2="97" class="sc-uline" /><text x="627.6800000000001" y="117" class="sc-lyric sc-v1" text-anchor="middle">名</text><text x="627.6800000000001" y="136" class="sc-lyric sc-v2" text-anchor="middle">拔</text><text x="627.6800000000001" y="155" class="sc-lyric sc-v3" text-anchor="middle">类</text><text x="655.2" y="92" class="sc-note">7</text><circle cx="655.2" cy="100" r="1.8" class="sc-dot" /><text x="655.2" y="117" class="sc-lyric sc-v1" text-anchor="middle">召</text><text x="655.2" y="136" class="sc-lyric sc-v2" text-anchor="middle">了</text><text x="655.2" y="155" class="sc-lyric sc-v3" text-anchor="middle">过</text><text x="682.72" y="92" class="sc-note">3</text><text x="682.72" y="117" class="sc-lyric sc-v1" text-anchor="middle">我</text><text x="690.72" y="117" class="sc-lyric-punct" text-anchor="start">？</text><text x="682.72" y="136" class="sc-lyric sc-v2" text-anchor="middle">我</text><text x="690.72" y="136" class="sc-lyric-punct" text-anchor="start">？</text><text x="682.72" y="155" class="sc-lyric sc-v3" text-anchor="middle">犯</text><text x="690.72" y="155" class="sc-lyric-punct" text-anchor="start">？</text><text x="710.24" y="92" class="sc-note">-</text><line x1="36" y1="178" x2="724" y2="178" class="sc-stave-sep" /><text x="50.33333333333333" y="206" class="sc-note">6</text><circle cx="50.33333333333333" cy="217" r="1.8" class="sc-dot" /><line x1="41.83333333333333" y1="211" x2="58.83333333333333" y2="211" class="sc-uline" /><text x="41.33333333333333" y="231" class="sc-verse-prefix" text-anchor="end">1.</text><text x="50.33333333333333" y="231" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="41.33333333333333" y="250" class="sc-verse-prefix" text-anchor="end">2.</text><text x="50.33333333333333" y="250" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="41.33333333333333" y="269" class="sc-verse-prefix" text-anchor="end">3.</text><text x="50.33333333333333" y="269" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="79" y="206" class="sc-note">7</text><circle cx="79" cy="217" r="1.8" class="sc-dot" /><line x1="70.5" y1="211" x2="87.5" y2="211" class="sc-uline" /><path d="M 48.33333333333333 189 Q 64.66666666666666 184 81 189" class="sc-slur" /><text x="107.66666666666666" y="206" class="sc-note">1</text><text x="107.66666666666666" y="231" class="sc-lyric sc-v1" text-anchor="middle">谁</text><text x="107.66666666666666" y="250" class="sc-lyric sc-v2" text-anchor="middle">谁</text><text x="107.66666666666666" y="269" class="sc-lyric sc-v3" text-anchor="middle">谁</text><text x="136.33333333333331" y="206" class="sc-note">1</text><line x1="127.83333333333331" y1="211" x2="144.83333333333331" y2="211" class="sc-uline" /><text x="136.33333333333331" y="231" class="sc-lyric sc-v1" text-anchor="middle">为</text><text x="136.33333333333331" y="250" class="sc-lyric sc-v2" text-anchor="middle">为</text><text x="136.33333333333331" y="269" class="sc-lyric sc-v3" text-anchor="middle">背</text><text x="165" y="206" class="sc-note">2</text><line x1="156.5" y1="211" x2="173.5" y2="211" class="sc-uline" /><text x="165" y="231" class="sc-lyric sc-v1" text-anchor="middle">寻</text><text x="165" y="250" class="sc-lyric sc-v2" text-anchor="middle">代</text><text x="165" y="269" class="sc-lyric sc-v3" text-anchor="middle">负</text><text x="193.66666666666669" y="206" class="sc-note">3</text><line x1="185.16666666666669" y1="211" x2="202.16666666666669" y2="211" class="sc-uline" /><text x="193.66666666666669" y="231" class="sc-lyric sc-v1" text-anchor="middle">找</text><text x="193.66666666666669" y="250" class="sc-lyric sc-v2" text-anchor="middle">替</text><text x="193.66666666666669" y="269" class="sc-lyric sc-v3" text-anchor="middle">全</text><text x="222.33333333333331" y="206" class="sc-note">1</text><line x1="213.83333333333331" y1="211" x2="230.83333333333331" y2="211" class="sc-uline" /><text x="222.33333333333331" y="231" class="sc-lyric sc-v1" text-anchor="middle">我</text><text x="222.33333333333331" y="250" class="sc-lyric sc-v2" text-anchor="middle">我</text><text x="222.33333333333331" y="269" class="sc-lyric sc-v3" text-anchor="middle">人</text><text x="251" y="206" class="sc-note">4</text><line x1="242.5" y1="211" x2="259.5" y2="211" class="sc-uline" /><text x="251" y="231" class="sc-lyric sc-v1" text-anchor="middle">降</text><text x="251" y="250" class="sc-lyric sc-v2" text-anchor="middle">甘</text><text x="251" y="269" class="sc-lyric sc-v3" text-anchor="middle">类</text><text x="279.6666666666667" y="206" class="sc-note">3</text><line x1="271.1666666666667" y1="211" x2="288.1666666666667" y2="211" class="sc-uline" /><text x="279.6666666666667" y="231" class="sc-lyric sc-v1" text-anchor="middle">生</text><text x="279.6666666666667" y="250" class="sc-lyric sc-v2" text-anchor="middle">心</text><text x="279.6666666666667" y="269" class="sc-lyric sc-v3" text-anchor="middle">的</text><text x="308.3333333333333" y="206" class="sc-note">2</text><text x="308.3333333333333" y="231" class="sc-lyric sc-v1" text-anchor="middle">尘</text><text x="308.3333333333333" y="250" class="sc-lyric sc-v2" text-anchor="middle">舍</text><text x="308.3333333333333" y="269" class="sc-lyric sc-v3" text-anchor="middle">忧</text><text x="337" y="206" class="sc-note">7</text><circle cx="337" cy="217" r="1.8" class="sc-dot" /><line x1="328.5" y1="211" x2="345.5" y2="211" class="sc-uline" /><text x="337" y="231" class="sc-lyric sc-v1" text-anchor="middle">世</text><text x="345" y="231" class="sc-lyric-punct" text-anchor="start">？</text><text x="337" y="250" class="sc-lyric sc-v2" text-anchor="middle">命</text><text x="345" y="250" class="sc-lyric-punct" text-anchor="start">？</text><text x="337" y="269" class="sc-lyric sc-v3" text-anchor="middle">患</text><text x="345" y="269" class="sc-lyric-punct" text-anchor="start">？</text><text x="365.6666666666667" y="206" class="sc-note">6</text><circle cx="365.6666666666667" cy="217" r="1.8" class="sc-dot" /><line x1="357.1666666666667" y1="211" x2="374.1666666666667" y2="211" class="sc-uline" /><text x="394.33333333333337" y="206" class="sc-note">5</text><circle cx="394.33333333333337" cy="214" r="1.8" class="sc-dot" /><path d="M 306.3333333333333 189 Q 351.33333333333337 179 396.33333333333337 189" class="sc-slur" /><text x="423" y="206" class="sc-note">1</text><circle cx="423" cy="217" r="1.8" class="sc-dot" /><line x1="414.5" y1="211" x2="431.5" y2="211" class="sc-uline" /><text x="423" y="231" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="423" y="250" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="423" y="269" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="451.6666666666667" y="206" class="sc-note">7</text><circle cx="451.6666666666667" cy="217" r="1.8" class="sc-dot" /><line x1="443.1666666666667" y1="211" x2="460.1666666666667" y2="211" class="sc-uline" /><path d="M 421 189 Q 437.33333333333337 184 453.6666666666667 189" class="sc-slur" /><text x="480.3333333333333" y="206" class="sc-note">6</text><circle cx="480.3333333333333" cy="214" r="1.8" class="sc-dot" /><text x="480.3333333333333" y="231" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="488.3333333333333" y="231" class="sc-lyric-punct" text-anchor="start">，</text><text x="480.3333333333333" y="250" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="488.3333333333333" y="250" class="sc-lyric-punct" text-anchor="start">，</text><text x="480.3333333333333" y="269" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="488.3333333333333" y="269" class="sc-lyric-punct" text-anchor="start">，</text><text x="509" y="206" class="sc-note">6</text><circle cx="509" cy="217" r="1.8" class="sc-dot" /><line x1="500.5" y1="211" x2="517.5" y2="211" class="sc-uline" /><text x="509" y="231" class="sc-lyric sc-v1" text-anchor="middle">主</text><text x="509" y="250" class="sc-lyric sc-v2" text-anchor="middle">主</text><text x="509" y="269" class="sc-lyric sc-v3" text-anchor="middle">主</text><text x="537.6666666666666" y="206" class="sc-note">7</text><circle cx="537.6666666666666" cy="217" r="1.8" class="sc-dot" /><line x1="529.1666666666666" y1="211" x2="546.1666666666666" y2="211" class="sc-uline" /><text x="537.6666666666666" y="231" class="sc-lyric sc-v1" text-anchor="middle">耶</text><text x="537.6666666666666" y="250" class="sc-lyric sc-v2" text-anchor="middle">耶</text><text x="537.6666666666666" y="269" class="sc-lyric sc-v3" text-anchor="middle">耶</text><text x="566.3333333333334" y="206" class="sc-note">1</text><text x="566.3333333333334" y="231" class="sc-lyric sc-v1" text-anchor="middle">稣</text><text x="566.3333333333334" y="250" class="sc-lyric sc-v2" text-anchor="middle">稣</text><text x="566.3333333333334" y="269" class="sc-lyric sc-v3" text-anchor="middle">稣</text><text x="595" y="206" class="sc-note">1</text><line x1="586.5" y1="211" x2="603.5" y2="211" class="sc-uline" /><text x="595" y="231" class="sc-lyric sc-v1" text-anchor="middle">唯</text><text x="595" y="250" class="sc-lyric sc-v2" text-anchor="middle">唯</text><text x="595" y="269" class="sc-lyric sc-v3" text-anchor="middle">唯</text><text x="623.6666666666667" y="206" class="sc-note">7</text><circle cx="623.6666666666667" cy="217" r="1.8" class="sc-dot" /><line x1="615.1666666666667" y1="211" x2="632.1666666666667" y2="211" class="sc-uline" /><text x="623.6666666666667" y="231" class="sc-lyric sc-v1" text-anchor="middle">有</text><text x="623.6666666666667" y="250" class="sc-lyric sc-v2" text-anchor="middle">有</text><text x="623.6666666666667" y="269" class="sc-lyric sc-v3" text-anchor="middle">有</text><text x="652.3333333333334" y="206" class="sc-note">6</text><circle cx="652.3333333333334" cy="214" r="1.8" class="sc-dot" /><text x="652.3333333333334" y="231" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="660.3333333333334" y="231" class="sc-lyric-punct" text-anchor="start">；</text><text x="652.3333333333334" y="250" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="660.3333333333334" y="250" class="sc-lyric-punct" text-anchor="start">；</text><text x="652.3333333333334" y="269" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="660.3333333333334" y="269" class="sc-lyric-punct" text-anchor="start">；</text><text x="681" y="206" class="sc-note">-</text><text x="709.6666666666666" y="206" class="sc-note">-</text><line x1="36" y1="292" x2="724" y2="292" class="sc-stave-sep" /><text x="51.63636363636364" y="320" class="sc-note">1</text><line x1="43.13636363636364" y1="325" x2="60.13636363636364" y2="325" class="sc-uline" /><text x="42.63636363636364" y="345" class="sc-verse-prefix" text-anchor="end">1.</text><text x="51.63636363636364" y="345" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="42.63636363636364" y="364" class="sc-verse-prefix" text-anchor="end">2.</text><text x="51.63636363636364" y="364" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="42.63636363636364" y="383" class="sc-verse-prefix" text-anchor="end">3.</text><text x="51.63636363636364" y="383" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="82.9090909090909" y="320" class="sc-note">2</text><line x1="74.4090909090909" y1="325" x2="91.4090909090909" y2="325" class="sc-uline" /><path d="M 49.63636363636364 303 Q 67.27272727272728 298 84.9090909090909 303" class="sc-slur" /><text x="114.18181818181819" y="320" class="sc-note">3</text><text x="114.18181818181819" y="345" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="122.18181818181819" y="345" class="sc-lyric-punct" text-anchor="start">，</text><text x="114.18181818181819" y="364" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="122.18181818181819" y="364" class="sc-lyric-punct" text-anchor="start">，</text><text x="114.18181818181819" y="383" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="122.18181818181819" y="383" class="sc-lyric-punct" text-anchor="start">，</text><text x="145.45454545454544" y="320" class="sc-note">3</text><line x1="136.95454545454544" y1="325" x2="153.95454545454544" y2="325" class="sc-uline" /><text x="145.45454545454544" y="345" class="sc-lyric sc-v1" text-anchor="middle">主</text><text x="145.45454545454544" y="364" class="sc-lyric sc-v2" text-anchor="middle">主</text><text x="145.45454545454544" y="383" class="sc-lyric sc-v3" text-anchor="middle">主</text><text x="176.72727272727272" y="320" class="sc-note">4</text><line x1="168.22727272727272" y1="325" x2="185.22727272727272" y2="325" class="sc-uline" /><text x="176.72727272727272" y="345" class="sc-lyric sc-v1" text-anchor="middle">耶</text><text x="176.72727272727272" y="364" class="sc-lyric sc-v2" text-anchor="middle">耶</text><text x="176.72727272727272" y="383" class="sc-lyric sc-v3" text-anchor="middle">耶</text><text x="208" y="320" class="sc-note">3</text><text x="208" y="345" class="sc-lyric sc-v1" text-anchor="middle">稣</text><text x="208" y="364" class="sc-lyric sc-v2" text-anchor="middle">稣</text><text x="208" y="383" class="sc-lyric sc-v3" text-anchor="middle">稣</text><text x="239.27272727272725" y="320" class="sc-note">1</text><line x1="230.77272727272725" y1="325" x2="247.77272727272725" y2="325" class="sc-uline" /><text x="239.27272727272725" y="345" class="sc-lyric sc-v1" text-anchor="middle">唯</text><text x="239.27272727272725" y="364" class="sc-lyric sc-v2" text-anchor="middle">唯</text><text x="239.27272727272725" y="383" class="sc-lyric sc-v3" text-anchor="middle">唯</text><text x="270.5454545454545" y="320" class="sc-note">3</text><line x1="262.0454545454545" y1="325" x2="279.0454545454545" y2="325" class="sc-uline" /><text x="270.5454545454545" y="345" class="sc-lyric sc-v1" text-anchor="middle">有</text><text x="270.5454545454545" y="364" class="sc-lyric sc-v2" text-anchor="middle">有</text><text x="270.5454545454545" y="383" class="sc-lyric sc-v3" text-anchor="middle">有</text><text x="301.8181818181818" y="320" class="sc-note">2</text><text x="301.8181818181818" y="345" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="309.8181818181818" y="345" class="sc-lyric-punct" text-anchor="start">；</text><text x="301.8181818181818" y="364" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="309.8181818181818" y="364" class="sc-lyric-punct" text-anchor="start">；</text><text x="301.8181818181818" y="383" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="309.8181818181818" y="383" class="sc-lyric-punct" text-anchor="start">；</text><text x="333.0909090909091" y="320" class="sc-note">-</text><text x="364.3636363636364" y="320" class="sc-note">-</text><text x="395.6363636363636" y="320" class="sc-note">2</text><line x1="387.1363636363636" y1="325" x2="404.1363636363636" y2="325" class="sc-uline" /><text x="395.6363636363636" y="345" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="395.6363636363636" y="364" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="395.6363636363636" y="383" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="426.9090909090909" y="320" class="sc-note">3</text><line x1="418.4090909090909" y1="325" x2="435.4090909090909" y2="325" class="sc-uline" /><path d="M 393.6363636363636 303 Q 411.27272727272725 298 428.9090909090909 303" class="sc-slur" /><text x="458.18181818181813" y="320" class="sc-note">4</text><text x="458.18181818181813" y="345" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="466.18181818181813" y="345" class="sc-lyric-punct" text-anchor="start">，</text><text x="458.18181818181813" y="364" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="466.18181818181813" y="364" class="sc-lyric-punct" text-anchor="start">，</text><text x="458.18181818181813" y="383" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="466.18181818181813" y="383" class="sc-lyric-punct" text-anchor="start">，</text><text x="489.4545454545454" y="320" class="sc-note">4</text><line x1="480.9545454545454" y1="325" x2="497.9545454545454" y2="325" class="sc-uline" /><text x="489.4545454545454" y="345" class="sc-lyric sc-v1" text-anchor="middle">主</text><text x="489.4545454545454" y="364" class="sc-lyric sc-v2" text-anchor="middle">主</text><text x="489.4545454545454" y="383" class="sc-lyric sc-v3" text-anchor="middle">主</text><text x="520.7272727272726" y="320" class="sc-note">5</text><line x1="512.2272727272726" y1="325" x2="529.2272727272726" y2="325" class="sc-uline" /><text x="520.7272727272726" y="345" class="sc-lyric sc-v1" text-anchor="middle">耶</text><text x="520.7272727272726" y="364" class="sc-lyric sc-v2" text-anchor="middle">耶</text><text x="520.7272727272726" y="383" class="sc-lyric sc-v3" text-anchor="middle">耶</text><text x="552" y="320" class="sc-note">4</text><text x="552" y="345" class="sc-lyric sc-v1" text-anchor="middle">稣</text><text x="552" y="364" class="sc-lyric sc-v2" text-anchor="middle">稣</text><text x="552" y="383" class="sc-lyric sc-v3" text-anchor="middle">稣</text><text x="583.2727272727273" y="320" class="sc-note">2</text><line x1="574.7727272727273" y1="325" x2="591.7727272727273" y2="325" class="sc-uline" /><text x="583.2727272727273" y="345" class="sc-lyric sc-v1" text-anchor="middle">唯</text><text x="583.2727272727273" y="364" class="sc-lyric sc-v2" text-anchor="middle">唯</text><text x="583.2727272727273" y="383" class="sc-lyric sc-v3" text-anchor="middle">唯</text><text x="614.5454545454545" y="320" class="sc-note">4</text><line x1="606.0454545454545" y1="325" x2="623.0454545454545" y2="325" class="sc-uline" /><text x="614.5454545454545" y="345" class="sc-lyric sc-v1" text-anchor="middle">有</text><text x="614.5454545454545" y="364" class="sc-lyric sc-v2" text-anchor="middle">有</text><text x="614.5454545454545" y="383" class="sc-lyric sc-v3" text-anchor="middle">有</text><text x="645.8181818181818" y="320" class="sc-note">3</text><text x="645.8181818181818" y="345" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="653.8181818181818" y="345" class="sc-lyric-punct" text-anchor="start">。</text><text x="645.8181818181818" y="364" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="653.8181818181818" y="364" class="sc-lyric-punct" text-anchor="start">。</text><text x="645.8181818181818" y="383" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="653.8181818181818" y="383" class="sc-lyric-punct" text-anchor="start">。</text><text x="677.090909090909" y="320" class="sc-note">-</text><text x="708.3636363636363" y="320" class="sc-note">-</text><line x1="36" y1="406" x2="724" y2="406" class="sc-stave-sep" /><text x="50.33333333333333" y="434" class="sc-note">1</text><line x1="41.83333333333333" y1="439" x2="58.83333333333333" y2="439" class="sc-uline" /><text x="41.33333333333333" y="459" class="sc-verse-prefix" text-anchor="end">1.</text><text x="50.33333333333333" y="459" class="sc-lyric sc-v1" text-anchor="middle">唯</text><text x="41.33333333333333" y="478" class="sc-verse-prefix" text-anchor="end">2.</text><text x="50.33333333333333" y="478" class="sc-lyric sc-v2" text-anchor="middle">唯</text><text x="41.33333333333333" y="497" class="sc-verse-prefix" text-anchor="end">3.</text><text x="50.33333333333333" y="497" class="sc-lyric sc-v3" text-anchor="middle">唯</text><text x="79" y="434" class="sc-note">2</text><line x1="70.5" y1="439" x2="87.5" y2="439" class="sc-uline" /><text x="79" y="459" class="sc-lyric sc-v1" text-anchor="middle">有</text><text x="79" y="478" class="sc-lyric sc-v2" text-anchor="middle">有</text><text x="79" y="497" class="sc-lyric sc-v3" text-anchor="middle">有</text><text x="107.66666666666666" y="434" class="sc-note">3</text><text x="107.66666666666666" y="459" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="115.66666666666666" y="459" class="sc-lyric-punct" text-anchor="start">，</text><text x="107.66666666666666" y="478" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="115.66666666666666" y="478" class="sc-lyric-punct" text-anchor="start">，</text><text x="107.66666666666666" y="497" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="115.66666666666666" y="497" class="sc-lyric-punct" text-anchor="start">，</text><text x="136.33333333333331" y="434" class="sc-note">3</text><line x1="127.83333333333331" y1="439" x2="144.83333333333331" y2="439" class="sc-uline" /><text x="136.33333333333331" y="459" class="sc-lyric sc-v1" text-anchor="middle">为</text><text x="136.33333333333331" y="478" class="sc-lyric sc-v2" text-anchor="middle">为</text><text x="136.33333333333331" y="497" class="sc-lyric sc-v3" text-anchor="middle">背</text><text x="165" y="434" class="sc-note">3</text><line x1="156.5" y1="439" x2="173.5" y2="439" class="sc-uline" /><text x="165" y="459" class="sc-lyric sc-v1" text-anchor="middle">寻</text><text x="165" y="478" class="sc-lyric sc-v2" text-anchor="middle">代</text><text x="165" y="497" class="sc-lyric sc-v3" text-anchor="middle">负</text><text x="193.66666666666669" y="434" class="sc-note">4</text><line x1="185.16666666666669" y1="439" x2="202.16666666666669" y2="439" class="sc-uline" /><text x="193.66666666666669" y="459" class="sc-lyric sc-v1" text-anchor="middle">找</text><text x="193.66666666666669" y="478" class="sc-lyric sc-v2" text-anchor="middle">替</text><text x="193.66666666666669" y="497" class="sc-lyric sc-v3" text-anchor="middle">全</text><text x="222.33333333333331" y="434" class="sc-note">3</text><line x1="213.83333333333331" y1="439" x2="230.83333333333331" y2="439" class="sc-uline" /><text x="222.33333333333331" y="459" class="sc-lyric sc-v1" text-anchor="middle">我</text><text x="222.33333333333331" y="478" class="sc-lyric sc-v2" text-anchor="middle">我</text><text x="222.33333333333331" y="497" class="sc-lyric sc-v3" text-anchor="middle">人</text><text x="251" y="434" class="sc-note">2</text><line x1="242.5" y1="439" x2="259.5" y2="439" class="sc-uline" /><text x="251" y="459" class="sc-lyric sc-v1" text-anchor="middle">降</text><text x="251" y="478" class="sc-lyric sc-v2" text-anchor="middle">甘</text><text x="251" y="497" class="sc-lyric sc-v3" text-anchor="middle">类</text><text x="279.6666666666667" y="434" class="sc-note">1</text><line x1="271.1666666666667" y1="439" x2="288.1666666666667" y2="439" class="sc-uline" /><text x="279.6666666666667" y="459" class="sc-lyric sc-v1" text-anchor="middle">生</text><text x="279.6666666666667" y="478" class="sc-lyric sc-v2" text-anchor="middle">心</text><text x="279.6666666666667" y="497" class="sc-lyric sc-v3" text-anchor="middle">的</text><text x="308.3333333333333" y="434" class="sc-note">2</text><text x="308.3333333333333" y="459" class="sc-lyric sc-v1" text-anchor="middle">尘</text><text x="308.3333333333333" y="478" class="sc-lyric sc-v2" text-anchor="middle">舍</text><text x="308.3333333333333" y="497" class="sc-lyric sc-v3" text-anchor="middle">忧</text><text x="337" y="434" class="sc-note">7</text><circle cx="337" cy="445" r="1.8" class="sc-dot" /><line x1="328.5" y1="439" x2="345.5" y2="439" class="sc-uline" /><text x="337" y="459" class="sc-lyric sc-v1" text-anchor="middle">世</text><text x="345" y="459" class="sc-lyric-punct" text-anchor="start">，</text><text x="337" y="478" class="sc-lyric sc-v2" text-anchor="middle">命</text><text x="345" y="478" class="sc-lyric-punct" text-anchor="start">，</text><text x="337" y="497" class="sc-lyric sc-v3" text-anchor="middle">患</text><text x="345" y="497" class="sc-lyric-punct" text-anchor="start">，</text><text x="365.6666666666667" y="434" class="sc-note">6</text><circle cx="365.6666666666667" cy="445" r="1.8" class="sc-dot" /><line x1="357.1666666666667" y1="439" x2="374.1666666666667" y2="439" class="sc-uline" /><text x="394.33333333333337" y="434" class="sc-note">5</text><circle cx="394.33333333333337" cy="442" r="1.8" class="sc-dot" /><path d="M 306.3333333333333 417 Q 351.33333333333337 407 396.33333333333337 417" class="sc-slur" /><text x="423" y="434" class="sc-note">1</text><circle cx="423" cy="445" r="1.8" class="sc-dot" /><line x1="414.5" y1="439" x2="431.5" y2="439" class="sc-uline" /><text x="423" y="459" class="sc-lyric sc-v1" text-anchor="middle">是</text><text x="423" y="478" class="sc-lyric sc-v2" text-anchor="middle">是</text><text x="423" y="497" class="sc-lyric sc-v3" text-anchor="middle">是</text><text x="451.6666666666667" y="434" class="sc-note">7</text><circle cx="451.6666666666667" cy="445" r="1.8" class="sc-dot" /><line x1="443.1666666666667" y1="439" x2="460.1666666666667" y2="439" class="sc-uline" /><path d="M 421 417 Q 437.33333333333337 412 453.6666666666667 417" class="sc-slur" /><text x="480.3333333333333" y="434" class="sc-note">6</text><circle cx="480.3333333333333" cy="442" r="1.8" class="sc-dot" /><text x="480.3333333333333" y="459" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="488.3333333333333" y="459" class="sc-lyric-punct" text-anchor="start">，</text><text x="480.3333333333333" y="478" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="488.3333333333333" y="478" class="sc-lyric-punct" text-anchor="start">，</text><text x="480.3333333333333" y="497" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="488.3333333333333" y="497" class="sc-lyric-punct" text-anchor="start">，</text><text x="509" y="434" class="sc-note">6</text><circle cx="509" cy="445" r="1.8" class="sc-dot" /><line x1="500.5" y1="439" x2="517.5" y2="439" class="sc-uline" /><text x="509" y="459" class="sc-lyric sc-v1" text-anchor="middle">主</text><text x="509" y="478" class="sc-lyric sc-v2" text-anchor="middle">主</text><text x="509" y="497" class="sc-lyric sc-v3" text-anchor="middle">主</text><text x="537.6666666666666" y="434" class="sc-note">7</text><circle cx="537.6666666666666" cy="445" r="1.8" class="sc-dot" /><line x1="529.1666666666666" y1="439" x2="546.1666666666666" y2="439" class="sc-uline" /><text x="537.6666666666666" y="459" class="sc-lyric sc-v1" text-anchor="middle">耶</text><text x="537.6666666666666" y="478" class="sc-lyric sc-v2" text-anchor="middle">耶</text><text x="537.6666666666666" y="497" class="sc-lyric sc-v3" text-anchor="middle">耶</text><text x="566.3333333333334" y="434" class="sc-note">1</text><text x="566.3333333333334" y="459" class="sc-lyric sc-v1" text-anchor="middle">稣</text><text x="566.3333333333334" y="478" class="sc-lyric sc-v2" text-anchor="middle">稣</text><text x="566.3333333333334" y="497" class="sc-lyric sc-v3" text-anchor="middle">稣</text><text x="595" y="434" class="sc-note">1</text><line x1="586.5" y1="439" x2="603.5" y2="439" class="sc-uline" /><text x="595" y="459" class="sc-lyric sc-v1" text-anchor="middle">唯</text><text x="595" y="478" class="sc-lyric sc-v2" text-anchor="middle">唯</text><text x="595" y="497" class="sc-lyric sc-v3" text-anchor="middle">唯</text><text x="623.6666666666667" y="434" class="sc-note">7</text><circle cx="623.6666666666667" cy="445" r="1.8" class="sc-dot" /><line x1="615.1666666666667" y1="439" x2="632.1666666666667" y2="439" class="sc-uline" /><text x="623.6666666666667" y="459" class="sc-lyric sc-v1" text-anchor="middle">有</text><text x="623.6666666666667" y="478" class="sc-lyric sc-v2" text-anchor="middle">有</text><text x="623.6666666666667" y="497" class="sc-lyric sc-v3" text-anchor="middle">有</text><text x="652.3333333333334" y="434" class="sc-note">6</text><circle cx="652.3333333333334" cy="442" r="1.8" class="sc-dot" /><text x="652.3333333333334" y="459" class="sc-lyric sc-v1" text-anchor="middle">祢</text><text x="660.3333333333334" y="459" class="sc-lyric-punct" text-anchor="start">。</text><text x="652.3333333333334" y="478" class="sc-lyric sc-v2" text-anchor="middle">祢</text><text x="660.3333333333334" y="478" class="sc-lyric-punct" text-anchor="start">。</text><text x="652.3333333333334" y="497" class="sc-lyric sc-v3" text-anchor="middle">祢</text><text x="660.3333333333334" y="497" class="sc-lyric-punct" text-anchor="start">。</text><text x="681" y="434" class="sc-note">-</text><text x="709.6666666666666" y="434" class="sc-note">-</text><line x1="720" y1="416" x2="720" y2="442" class="sc-bar" /><line x1="724" y1="416" x2="724" y2="442" class="sc-dbar" /><line x1="36" y1="520" x2="724" y2="520" class="sc-stave-sep" /></svg></div>
        </div>

        <!-- Raw Plain Text Pre -->
        <div class="score-raw-container" id="disp-score-raw" style="display: none;">
          <pre class="raw-score-pre" id="disp-raw-pre"></pre>
        </div>
      </section>

      <!-- Lyrics Viewer Card -->
      <section class="lyrics-viewer-card" id="lyrics-viewer-panel" style="display: none;">
        <div class="lyrics-content-body" id="disp-lyrics-body">
          <!-- Lyrics will be rendered here -->
        </div>
      </section>

    </div>
  </main>
</div>

<!-- Sticky Bottom Player Bar -->
<footer class="app-player-bar">
  <div class="player-track-info">
    <div class="player-track-meta">
      <div class="player-track-name" id="player-title">是谁从远处看见认识我</div>
    </div>
  </div>

  <div class="player-center-controls">
    <div class="player-btn-row">
      <button class="ctrl-icon-btn" onclick="prevHymn()" title="上一首诗歌">⏮️</button>
      <button class="ctrl-play-main" id="player-bar-play-btn" onclick="togglePlay()" title="播放/暂停">▶</button>
      <button class="ctrl-icon-btn" onclick="nextHymn()" title="下一首诗歌">⏭️</button>
      <button class="ctrl-icon-btn" id="btn-loop-mode" onclick="toggleLoopMode()" title="循环播放">🔁</button>
    </div>

    <div class="player-progress-row">
      <span class="time-text" id="disp-curr-time">00:00</span>
      <div class="progress-slider-container" id="progress-container" onclick="seekAudio(event)">
        <div class="progress-bar-fill" id="progress-bar-fill"></div>
      </div>
      <span class="time-text" id="disp-total-time">02:30</span>
    </div>
  </div>

  <div class="player-right-controls">
    <span class="audio-type-pill" onclick="toggleAudioEngine()" id="btn-audio-engine">🎹 钢琴伴奏</span>
    <button class="header-btn" onclick="openVideoModal()" title="观看敬拜视频" style="padding: 5px 9px; font-size: 12px;">
      🎬 视频
    </button>
  </div>
</footer>


<!-- Video Modal -->
<div class="video-modal-backdrop" id="video-modal" onclick="if(event.target===this) closeVideoModal()">
  <div class="video-modal-content">
    <div class="video-modal-header">
      <div class="video-modal-title" id="video-modal-title">敬拜赞美视频</div>
      <button class="video-modal-close" onclick="closeVideoModal()">✕</button>
    </div>
    <div class="video-embed-box" id="video-embed-box">
      <!-- Iframe inserted dynamically -->
    </div>
  </div>
</div>

<!-- Hymns Database Script -->
<script>
{js_data_content}
</script>

<!-- App Interactive Logic -->
<script>
  let currentHymnIndex = 0;
  let currentCategory = '全部';
  let viewMode = 'score'; // 'score' or 'lyrics'
  let isPlaying = false;
  let isLooping = false;
  let lyricsFontSize = 22;
  let scoreFontSize = 18;
  let scoreFormat = 'formatted'; // 'formatted' or 'raw'
  let playbackTimer = null;
  let playbackProgress = 0; // seconds
  let totalPlaybackDuration = 150; // default seconds

  // Web Audio Synthesizer Context
  let audioCtx = null;
  let activeMelodyTimeouts = [];

  function initApp() {{
    renderSidebarList();

    // Event delegation on sidebar hymn list
    const hymnListEl = document.getElementById('hymn-list');
    if (hymnListEl) {{
      hymnListEl.addEventListener('click', (e) => {{
        const item = e.target.closest('.hymn-item');
        if (item) {{
          const idx = parseInt(item.getAttribute('data-index'), 10);
          if (!isNaN(idx)) {{
            loadHymn(idx);
            if (window.innerWidth <= 900) {{
              toggleSidebar(false);
            }}
          }}
        }}
      }});
    }}

    // Check URL parameter ?id=... or #...
    const urlParams = new URLSearchParams(window.location.search);
    const paramId = urlParams.get('id') || window.location.hash.replace('#', '').replace('hymn-', '');
    let targetIdx = 0;
    if (paramId) {{
      const foundIdx = HYMNS_DATABASE.findIndex(h => h.id === paramId || String(h.number) === paramId);
      if (foundIdx !== -1) {{
        targetIdx = foundIdx;
      }}
    }}
    loadHymn(targetIdx);
    initKeyboardShortcuts();

    window.addEventListener('popstate', () => {{
      const params = new URLSearchParams(window.location.search);
      const pid = params.get('id');
      if (pid) {{
        const fIdx = HYMNS_DATABASE.findIndex(h => h.id === pid || String(h.number) === pid);
        if (fIdx !== -1 && fIdx !== currentHymnIndex) {{
          loadHymn(fIdx);
        }}
      }}
    }});
  }}

  // Filter Hymns
  function filterCategory(cat) {{
    currentCategory = cat;
    document.querySelectorAll('.cat-pill').forEach(btn => {{
      btn.classList.toggle('active', btn.innerText.includes(cat) || (cat==='全部' && btn.innerText.includes('全部')));
    }});
    renderSidebarList();
  }}

  function handleSearch(query) {{
    renderSidebarList(query.trim().toLowerCase());
  }}

  // Render Sidebar List
  function renderSidebarList(filter = '') {{
    const list = document.getElementById('hymn-list');
    if (!list) return;
    list.innerHTML = '';

    HYMNS_DATABASE.forEach((hymn, idx) => {{
      // Category check
      if (currentCategory !== '全部' && hymn.category !== currentCategory) {{
        return;
      }}
      // Search check
      if (filter) {{
        const searchStr = `${{hymn.number}} ${{hymn.title}} ${{hymn.category}} ${{hymn.author}} ${{JSON.stringify(hymn.lyrics)}}`.toLowerCase();
        if (!searchStr.includes(filter)) return;
      }}

      const li = document.createElement('li');
      li.className = `hymn-item ${{idx === currentHymnIndex ? 'active' : ''}} ${{idx === currentHymnIndex && isPlaying ? 'is-playing' : ''}}`;
      li.setAttribute('data-index', idx);
      li.setAttribute('data-id', hymn.id);
      li.onclick = (e) => {{
        e.stopPropagation();
        loadHymn(idx);
        if (window.innerWidth <= 900) {{
          toggleSidebar(false);
        }}
      }};

      li.innerHTML = `
        <div class="hymn-item-left">
          <div class="hymn-info">
            <div class="hymn-item-title">${{escapeHtml(hymn.title)}}</div>
          </div>
        </div>
        <div class="hymn-item-right">
          <div class="playing-wave">
            <div class="wave-bar"></div>
            <div class="wave-bar"></div>
            <div class="wave-bar"></div>
          </div>
        </div>
      `;
      list.appendChild(li);
    }});
  }}

  // Load Specific Hymn
  function loadHymn(idx) {{
    if (idx < 0 || idx >= HYMNS_DATABASE.length) return;
    
    try {{
      // Stop any ongoing synthesis
      stopWebAudioMelody();
      isPlaying = false;
      playbackProgress = 0;
      updatePlayStateUI();

      currentHymnIndex = idx;
      const hymn = HYMNS_DATABASE[idx];

      // Detail Header - Pure Song Title
      const titleEl = document.getElementById('disp-title');
      if (titleEl) titleEl.innerText = hymn.title;

      // URL query sync without page reload
      try {{
        const url = new URL(window.location.href);
        url.searchParams.set('id', hymn.id);
        window.history.replaceState({{ hymnId: hymn.id }}, hymn.title, url.toString());
      }} catch (e) {{}}

      // Text Score View
      activeVerseFilter = 'all';
      ['all', '1', '2', '3'].forEach(v => {{
        const btn = document.getElementById(`btn-verse-${{v}}`);
        if (btn) btn.classList.toggle('active', v === 'all');
      }});
      renderTextScore(hymn);

      // Lyrics View
      const lyricsBody = document.getElementById('disp-lyrics-body');
      if (lyricsBody) {{
        lyricsBody.innerHTML = '';
        if (hymn.lyrics && hymn.lyrics.length) {{
          hymn.lyrics.forEach(sec => {{
            const secDiv = document.createElement('div');
            secDiv.className = 'lyrics-section-block';
            let secHtml = '';
            if (sec.section && sec.section !== '注') {{
              secHtml += `<div class="lyrics-section-badge">${{escapeHtml(sec.section)}}</div>`;
            }}
            secHtml += sec.lines.map(line => `<div class="lyrics-line">${{escapeHtml(line)}}</div>`).join('');
            secDiv.innerHTML = secHtml;
            lyricsBody.appendChild(secDiv);
          }});
        }}
      }}

      // Player Bar - Pure Song Title
      const playerTitle = document.getElementById('player-title');
      if (playerTitle) playerTitle.innerText = hymn.title;
      const currTime = document.getElementById('disp-curr-time');
      if (currTime) currTime.innerText = '00:00';
      
      // Estimate duration based on melody
      let totalDur = 120;
      if (hymn.melody && hymn.melody.length) {{
        totalDur = Math.round(hymn.melody.reduce((acc, m) => acc + m.dur * 0.75, 0));
      }}
      totalPlaybackDuration = totalDur;
      const totalTime = document.getElementById('disp-total-time');
      if (totalTime) totalTime.innerText = formatTime(totalDur);
      const progFill = document.getElementById('progress-bar-fill');
      if (progFill) progFill.style.width = '0%';

      // Update Sidebar Active state
      document.querySelectorAll('.hymn-item').forEach((item, i) => {{
        item.classList.toggle('active', i === currentHymnIndex);
      }});
    }} catch (err) {{
      console.error('Error loading hymn:', err);
    }}
  }}

  // Switch View Mode (Score vs Lyrics)
  function switchViewMode(mode) {{
    viewMode = mode;
    const scorePanel = document.getElementById('score-viewer-panel');
    const lyricsPanel = document.getElementById('lyrics-viewer-panel');
    const tabScore = document.getElementById('tab-score');
    const tabLyrics = document.getElementById('tab-lyrics');

    if (mode === 'score') {{
      if (scorePanel) scorePanel.style.display = 'block';
      if (lyricsPanel) lyricsPanel.style.display = 'none';
      if (tabScore) tabScore.classList.add('active');
      if (tabLyrics) tabLyrics.classList.remove('active');
    }} else {{
      if (scorePanel) scorePanel.style.display = 'none';
      if (lyricsPanel) lyricsPanel.style.display = 'block';
      if (tabScore) tabScore.classList.remove('active');
      if (tabLyrics) tabLyrics.classList.add('active');
    }}
  }}

  function toggleSidebar(force) {{
    const sidebar = document.getElementById('sidebar-catalog');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (typeof force === 'boolean') {{
      sidebar.classList.toggle('open', force);
      backdrop.classList.toggle('active', force);
    }} else {{
      sidebar.classList.toggle('open');
      backdrop.classList.toggle('active');
    }}
  }}

  function escapeHtml(str) {{
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }}

  let activeVerseFilter = 'all'; // 'all', '1', '2', '3'

  function setVerseFilter(verseNum) {{
    activeVerseFilter = verseNum;
    ['all', '1', '2', '3'].forEach(v => {{
      const btn = document.getElementById(`btn-verse-${{v}}`);
      if (btn) btn.classList.toggle('active', v === verseNum);
    }});
    
    const hymn = HYMNS_DATABASE[currentHymnIndex];
    if (hymn && hymn.jianpuStaves && hymn.jianpuStaves.length > 0) {{
      const formattedContainer = document.getElementById('disp-score-formatted');
      if (formattedContainer) {{
        formattedContainer.innerHTML = generateUnifiedJianpuSvg(hymn, activeVerseFilter);
      }}
    }}
  }}

  function generateUnifiedJianpuSvg(hymn, activeVerse) {{
    const staves = hymn.jianpuStaves;
    if (!staves || staves.length === 0) return '';

    const viewW = 760;
    const marginL = 36;
    const marginR = 36;
    const usableW = viewW - marginL - marginR;

    const headerH = 68;
    let currY = headerH;
    const stavePositions = [];

    staves.forEach(stave => {{
      let maxV = 1;
      stave.measures.forEach(m => {{
        m.units.forEach(u => {{
          if (u.lyrics && u.lyrics.length > maxV) {{
            maxV = u.lyrics.length;
          }}
        }});
      }});
      const effectiveV = (activeVerse !== 'all') ? 1 : maxV;
      let staveH = 72;
      if (effectiveV === 2) staveH = 92;
      else if (effectiveV >= 3) staveH = 114;

      if (stave.sectionMarker) {{
        staveH += 22;
      }}

      stavePositions.push({{
        stave: stave,
        y: currY,
        height: staveH,
        maxV: maxV
      }});
      currY += staveH;
    }});

    const totalH = currY + 20;

    let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${{viewW}} ${{totalH}}" width="100%" height="auto" class="unified-score-svg" style="display:block; overflow:visible;">`;

    // Key & Meter on left, Song Title centered
    const keySig = (hymn.textScore && hymn.textScore.keySignature) || hymn.key || '1=C';
    const timeSig = (hymn.textScore && hymn.textScore.timeSignature) || hymn.timeSignature || '4/4';

    svg += `<text x="${{marginL}}" y="38" class="sc-meta" style="font-size: 15px; font-weight: 600;">${{escapeHtml(keySig)}}  ${{escapeHtml(timeSig)}}</text>`;
    svg += `<text x="${{viewW / 2}}" y="38" class="sc-title">${{escapeHtml(hymn.title)}}</text>`;

    // Subtle divider
    svg += `<line x1="${{marginL}}" y1="52" x2="${{viewW - marginR}}" y2="52" class="sc-divider" />`;

    // Render each stave
    stavePositions.forEach(sInfo => {{
      const stave = sInfo.stave;
      let baseY = sInfo.y;

      if (stave.sectionMarker) {{
        svg += `<text x="${{viewW / 2}}" y="${{baseY + 12}}" text-anchor="middle" class="sc-meta" style="font-size: 13.5px; font-weight: 700; fill: var(--text-secondary);">${{escapeHtml(stave.sectionMarker)}}</text>`;
        baseY += 18;
      }}

      const noteY = baseY + 24;

      let currentSlurStartX = null;
      let currentSlurHigh = false;

      let currentVolta = null;
      let currentVoltaStartX = null;

      let totalUnits = 0;
      stave.measures.forEach(m => {{
        totalUnits += m.units.length;
      }});
      if (totalUnits === 0) return;

      let currMx = marginL;

      stave.measures.forEach(m => {{
        const mUnitsCount = m.units.length;
        const mW = (mUnitsCount / totalUnits) * usableW;

        if (m.volta) {{
          currentVolta = m.volta;
          currentVoltaStartX = currMx;
        }}

        // Bar Left
        if (m.barLeft) {{
          const bSym = m.barLeft;
          if (bSym === '|:') {{
            svg += `<line x1="${{currMx}}" y1="${{noteY - 18}}" x2="${{currMx}}" y2="${{noteY + 8}}" class="sc-dbar" />`;
            svg += `<line x1="${{currMx + 3.5}}" y1="${{noteY - 18}}" x2="${{currMx + 3.5}}" y2="${{noteY + 8}}" class="sc-bar" />`;
            svg += `<circle cx="${{currMx + 7.5}}" cy="${{noteY - 9}}" r="1.6" class="sc-dot" />`;
            svg += `<circle cx="${{currMx + 7.5}}" cy="${{noteY - 1}}" r="1.6" class="sc-dot" />`;
          }} else if (bSym === '|') {{
            svg += `<line x1="${{currMx}}" y1="${{noteY - 18}}" x2="${{currMx}}" y2="${{noteY + 8}}" class="sc-bar" />`;
          }}
        }}

        // Units
        const unitSpacing = mW / mUnitsCount;
        m.units.forEach((u, uIdx) => {{
          const ux = currMx + (uIdx + 0.5) * unitSpacing;
          const pitch = u.pitch || '';
          const octave = u.octave || 0;
          const underlines = u.underlines || 0;
          const dot = !!u.dot;
          const lyrics = u.lyrics || [];

          // Note Pitch digit
          svg += `<text x="${{ux}}" y="${{noteY}}" class="sc-note">${{escapeHtml(pitch)}}</text>`;

          // Dotted note dot
          if (dot) {{
            svg += `<circle cx="${{ux + 9}}" cy="${{noteY - 8}}" r="1.8" class="sc-dot" />`;
          }}

          // High octave dot
          if (octave > 0) {{
            svg += `<circle cx="${{ux}}" cy="${{noteY - 20}}" r="1.8" class="sc-dot" />`;
          }}

          // Low octave dot
          if (octave < 0) {{
            const lowY = (underlines === 0) ? (noteY + 8) : ((underlines === 1) ? (noteY + 11) : (noteY + 14));
            svg += `<circle cx="${{ux}}" cy="${{lowY}}" r="1.8" class="sc-dot" />`;
          }}

          // Underlines (减时线)
          if (underlines === 1) {{
            svg += `<line x1="${{ux - 8.5}}" y1="${{noteY + 5}}" x2="${{ux + 8.5}}" y2="${{noteY + 5}}" class="sc-uline" />`;
          }} else if (underlines === 2) {{
            svg += `<line x1="${{ux - 8.5}}" y1="${{noteY + 4}}" x2="${{ux + 8.5}}" y2="${{noteY + 4}}" class="sc-uline" />`;
            svg += `<line x1="${{ux - 8.5}}" y1="${{noteY + 7.5}}" x2="${{ux + 8.5}}" y2="${{noteY + 7.5}}" class="sc-uline" />`;
          }}

          // Slur / Tie arcs
          if (u.slurEnd && currentSlurStartX !== null) {{
            const endX = ux;
            const startX = currentSlurStartX;
            const arcTopY = currentSlurHigh ? (noteY - 25) : (noteY - 17);
            const midX = (startX + endX) / 2;
            const arcPeakY = arcTopY - Math.min(10, Math.max(5, (endX - startX) * 0.12));
            svg += `<path d="M ${{startX - 2}} ${{arcTopY}} Q ${{midX}} ${{arcPeakY}} ${{endX + 2}} ${{arcTopY}}" class="sc-slur" />`;
            currentSlurStartX = null;
            currentSlurHigh = false;
          }}
          if (u.slurStart) {{
            currentSlurStartX = ux;
            currentSlurHigh = (octave > 0);
          }}

          // Lyrics lines (100% exact note-to-character vertical alignment)
          lyrics.forEach((lyricText, vIdx) => {{
            if (!lyricText) return;
            const vNum = vIdx + 1;
            if (activeVerse !== 'all' && activeVerse !== String(vNum)) {{
              return;
            }}

            const lineRowIdx = (activeVerse === 'all') ? vIdx : 0;
            const lyricY = noteY + 25 + lineRowIdx * 19;
            const vClass = `sc-v${{vNum}}`;

            let vPrefix = '';
            let charGlyph = '';
            let punct = '';

            // 1. Extract verse prefix e.g. "1. ", "2. ", "3. "
            const prefixMatch = lyricText.match(/^(\d+\.\s*)(.*)$/);
            let body = lyricText;
            if (prefixMatch) {{
              vPrefix = prefixMatch[1];
              body = prefixMatch[2];
            }}

            // 2. Extract trailing punctuation e.g. "，", "。", "！", "？", "；", "："
            const punctMatch = body.match(/^(.*?)([\，\。\！\!\？\?\；\;\:\：]+)$/);
            if (punctMatch) {{
              charGlyph = punctMatch[1];
              punct = punctMatch[2];
            }} else {{
              charGlyph = body;
            }}

            // 3. Render verse prefix if present (anchored to the left of the syllable)
            if (vPrefix) {{
              svg += `<text x="${{ux - 9}}" y="${{lyricY}}" class="sc-verse-prefix" text-anchor="end">${{escapeHtml(vPrefix.trim())}}</text>`;
            }}

            // 4. Render Chinese character dead-centered at ux (matches note digit horizontal center perfectly!)
            if (charGlyph) {{
              svg += `<text x="${{ux}}" y="${{lyricY}}" class="sc-lyric ${{vClass}}" text-anchor="middle">${{escapeHtml(charGlyph)}}</text>`;
            }}

            // 5. Render trailing punctuation if present (anchored immediately following the character)
            if (punct) {{
              svg += `<text x="${{ux + 8}}" y="${{lyricY}}" class="sc-lyric-punct" text-anchor="start">${{escapeHtml(punct)}}</text>`;
            }}
          }});
        }});

        // Bar Right
        if (m.barRight) {{
          const rSym = m.barRight;
          if (rSym === ':|') {{
            svg += `<circle cx="${{currMx + mW - 7.5}}" cy="${{noteY - 9}}" r="1.6" class="sc-dot" />`;
            svg += `<circle cx="${{currMx + mW - 7.5}}" cy="${{noteY - 1}}" r="1.6" class="sc-dot" />`;
            svg += `<line x1="${{currMx + mW - 3.5}}" y1="${{noteY - 18}}" x2="${{currMx + mW - 3.5}}" y2="${{noteY + 8}}" class="sc-bar" />`;
            svg += `<line x1="${{currMx + mW}}" y1="${{noteY - 18}}" x2="${{currMx + mW}}" y2="${{noteY + 8}}" class="sc-dbar" />`;
          }} else if (rSym === '||') {{
            svg += `<line x1="${{currMx + mW - 4}}" y1="${{noteY - 18}}" x2="${{currMx + mW - 4}}" y2="${{noteY + 8}}" class="sc-bar" />`;
            svg += `<line x1="${{currMx + mW}}" y1="${{noteY - 18}}" x2="${{currMx + mW}}" y2="${{noteY + 8}}" class="sc-dbar" />`;
          }}
        }}

        // Render Volta bracket if ending at this measure or single measure
        if (currentVolta && (m.barRight === ':|' || m.barRight === '||' || !m.volta)) {{
          const vY = noteY - 24;
          const vStartX = currentVoltaStartX !== null ? currentVoltaStartX : currMx;
          const vEndX = currMx + mW;
          svg += `<line x1="${{vStartX}}" y1="${{vY}}" x2="${{vEndX}}" y2="${{vY}}" class="sc-bar" />`;
          svg += `<line x1="${{vStartX}}" y1="${{vY}}" x2="${{vStartX}}" y2="${{vY + 7}}" class="sc-bar" />`;
          svg += `<text x="${{vStartX + 4}}" y="${{vY - 3}}" class="sc-meta" style="font-size: 11px; font-weight: 700; fill: currentColor;">${{escapeHtml(currentVolta)}}</text>`;
          if (m.barRight === ':|') {{
            svg += `<line x1="${{vEndX}}" y1="${{vY}}" x2="${{vEndX}}" y2="${{vY + 7}}" class="sc-bar" />`;
          }}
          currentVolta = null;
          currentVoltaStartX = null;
        }}

        currMx += mW;
      }});

      // Light stave bottom separator
      svg += `<line x1="${{marginL}}" y1="${{baseY + sInfo.height - 4}}" x2="${{viewW - marginR}}" y2="${{baseY + sInfo.height - 4}}" class="sc-stave-sep" />`;
    }});

    if (hymn.footnote) {{
      svg += `<text x="${{viewW / 2}}" y="${{totalH - 6}}" text-anchor="middle" class="sc-meta" style="font-size: 13px; font-weight: 500; fill: var(--text-secondary);">${{escapeHtml(hymn.footnote)}}</text>`;
    }}

    svg += '</svg>';
    return `<div class="unified-score-sheet" style="max-width: ${{Math.round(860 * (scoreZoom / 100))}}px;">${{svg}}</div>`;
  }}

    function renderTextScore(hymn) {{
    const ts = hymn.textScore || {{}};
    const dispKey = document.getElementById('disp-score-key');
    const dispMeter = document.getElementById('disp-score-meter');
    const dispTempo = document.getElementById('disp-score-tempo');
    if (dispKey) dispKey.innerText = ts.keySignature || hymn.key || '';
    if (dispMeter) dispMeter.innerText = ts.timeSignature || hymn.timeSignature || '';
    if (dispTempo) dispTempo.innerText = ts.tempo ? `· ${{ts.tempo}}` : '';

    // Check how many verses exist in this hymn
    let maxVerses = 1;
    if (hymn.jianpuStaves) {{
      hymn.jianpuStaves.forEach(stave => {{
        stave.measures.forEach(m => {{
          m.units.forEach(u => {{
            if (u.lyrics && u.lyrics.length > maxVerses) {{
              maxVerses = u.lyrics.length;
            }}
          }});
        }});
      }});
    }}

    // Update verse button visibility
    const btnV2 = document.getElementById('btn-verse-2');
    const btnV3 = document.getElementById('btn-verse-3');
    if (btnV2) btnV2.style.display = maxVerses >= 2 ? 'inline-block' : 'none';
    if (btnV3) btnV3.style.display = maxVerses >= 3 ? 'inline-block' : 'none';

    // Render formatted unified jianpu sheet
    const formattedContainer = document.getElementById('disp-score-formatted');
    if (formattedContainer) {{
      if (hymn.jianpuStaves && hymn.jianpuStaves.length > 0) {{
        formattedContainer.innerHTML = generateUnifiedJianpuSvg(hymn, activeVerseFilter);
      }} else {{
        formattedContainer.innerHTML = '<div style="color: var(--text-muted); padding: 30px; text-align: center;">暂无曲谱数据</div>';
      }}
    }}

    // Render raw text pre
    const rawPre = document.getElementById('disp-raw-pre');
    if (rawPre) {{
      rawPre.innerText = ts.rawText || '';
    }}
  }}

  function switchScoreFormat(fmt) {{
    scoreFormat = fmt;
    const formattedBox = document.getElementById('disp-score-formatted');
    const rawBox = document.getElementById('disp-score-raw');
    const subFormatted = document.getElementById('subtab-formatted');
    const subRaw = document.getElementById('subtab-raw');
    if (fmt === 'formatted') {{
      if (formattedBox) formattedBox.style.display = 'flex';
      if (rawBox) rawBox.style.display = 'none';
      if (subFormatted) subFormatted.classList.add('active');
      if (subRaw) subRaw.classList.remove('active');
    }} else {{
      if (formattedBox) formattedBox.style.display = 'none';
      if (rawBox) rawBox.style.display = 'block';
      if (subFormatted) subFormatted.classList.remove('active');
      if (subRaw) subRaw.classList.add('active');
    }}
  }}

  let scoreZoom = 100; // percent: 75% to 140%
  function adjustScoreFontSize(delta) {{
    if (scoreFormat === 'formatted') {{
      scoreZoom = Math.max(75, Math.min(135, scoreZoom + delta * 5));
      const sheet = document.querySelector('.unified-score-sheet');
      if (sheet) {{
        sheet.style.maxWidth = `${{Math.round(860 * (scoreZoom / 100))}}px`;
      }}
    }} else {{
      scoreFontSize = Math.max(13, Math.min(30, scoreFontSize + delta));
      document.documentElement.style.setProperty('--font-size-score', `${{scoreFontSize}}px`);
    }}
  }}

  function copyTextScore() {{
    const hymn = HYMNS_DATABASE[currentHymnIndex];
    const text = (hymn.textScore && hymn.textScore.rawText) ? hymn.textScore.rawText : `${{hymn.number}}. ${{hymn.title}}`;
    navigator.clipboard.writeText(text).then(() => {{
      showToast('已成功复制纯文本歌谱！');
    }}).catch(() => {{
      showToast('已选中纯文本歌谱，可按快捷键复制。');
    }});
  }}

  function adjustLyricsFontSize(delta) {{
    lyricsFontSize = Math.max(16, Math.min(36, lyricsFontSize + delta));
    document.documentElement.style.setProperty('--font-size-lyrics', `${{lyricsFontSize}}px`);
  }}

  function copyLyrics() {{
    const hymn = HYMNS_DATABASE[currentHymnIndex];
    let text = `${{hymn.number}}. ${{hymn.title}}\\n${{hymn.key}} ${{hymn.timeSignature}}\\n\\n`;
    hymn.lyrics.forEach(sec => {{
      text += `【${{sec.section}}】\\n` + sec.lines.join('\\n') + '\\n\\n';
    }});
    navigator.clipboard.writeText(text).then(() => {{
      showToast('已成功复制歌词到剪贴板！');
    }}).catch(() => {{
      showToast('复制失败，请手动选取歌词复制。');
    }});
  }}

  function showToast(msg) {{
    let toast = document.getElementById('app-toast');
    if (!toast) {{
      toast = document.createElement('div');
      toast.id = 'app-toast';
      toast.style.cssText = 'position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(15,23,42,0.94);color:#F8FAFC;padding:10px 22px;border-radius:24px;border:1px solid rgba(245,158,11,0.35);box-shadow:0 10px 30px rgba(0,0,0,0.5);font-size:14px;font-weight:600;z-index:9999;pointer-events:none;transition:opacity 0.3s;opacity:0;';
      document.body.appendChild(toast);
    }}
    toast.innerText = msg;
    toast.style.opacity = '1';
    setTimeout(() => {{
      toast.style.opacity = '0';
    }}, 2200);
  }}

  // Web Audio Piano Synthesizer
  function getAudioContext() {{
    if (!audioCtx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioCtx();
    }}
    if (audioCtx.state === 'suspended') {{
      audioCtx.resume();
    }}
    return audioCtx;
  }}

  const NOTE_FREQS = {{
    "B3": 246.94, "C4": 261.63, "C#4": 277.18, "D4": 293.66, "Eb4": 311.13,
    "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30,
    "A4": 440.00, "Bb4": 466.16, "B4": 493.88, "C5": 523.25, "C#5": 554.37,
    "D5": 587.33, "Eb5": 622.25, "E5": 659.25, "F5": 698.46, "G5": 783.99,
    "A3": 220.00, "Bb3": 233.08
  }};

  function playPianoTone(freq, startTime, duration) {{
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    // Warm triangle/sine blend for piano/reed timbre
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, startTime);

    // Natural piano ADSR envelope
    gain.gain.setValueAtTime(0.0001, startTime);
    gain.gain.linearRampToValueAtTime(0.35, startTime + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.15, startTime + 0.15);
    gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(startTime);
    osc.stop(startTime + duration + 0.05);
  }}

  function startWebAudioMelody() {{
    const hymn = HYMNS_DATABASE[currentHymnIndex];
    if (!hymn.melody || !hymn.melody.length) return;

    const ctx = getAudioContext();
    let now = ctx.currentTime + 0.1;
    const tempoSecPerBeat = 0.65; // ~92 BPM graceful tempo

    activeMelodyTimeouts.forEach(t => clearTimeout(t));
    activeMelodyTimeouts = [];

    let totalOffset = 0;
    hymn.melody.forEach((item, i) => {{
      const durSec = item.dur * tempoSecPerBeat;
      const freq = NOTE_FREQS[item.note] || 440;
      playPianoTone(freq, now + totalOffset, durSec * 0.92);

      // Timeout for visual progress
      const t = setTimeout(() => {{
        playbackProgress = Math.round(totalOffset);
        updateProgressUI();
      }}, totalOffset * 1000);
      activeMelodyTimeouts.push(t);

      totalOffset += durSec;
    }});

    // Finish callback
    const finishTimeout = setTimeout(() => {{
      if (isLooping) {{
        startWebAudioMelody();
      }} else {{
        nextHymn();
      }}
    }}, totalOffset * 1000 + 500);
    activeMelodyTimeouts.push(finishTimeout);
  }}

  function stopWebAudioMelody() {{
    activeMelodyTimeouts.forEach(t => clearTimeout(t));
    activeMelodyTimeouts = [];
  }}

  // Play / Pause Logic
  function togglePlay() {{
    if (isPlaying) {{
      pausePlayback();
    }} else {{
      startPlayback();
    }}
  }}

  function startPlayback() {{
    isPlaying = true;
    updatePlayStateUI();
    startWebAudioMelody();

    // Progress counter
    if (playbackTimer) clearInterval(playbackTimer);
    playbackTimer = setInterval(() => {{
      playbackProgress++;
      if (playbackProgress > totalPlaybackDuration) {{
        playbackProgress = totalPlaybackDuration;
      }}
      updateProgressUI();
    }}, 1000);
  }}

  function pausePlayback() {{
    isPlaying = false;
    updatePlayStateUI();
    stopWebAudioMelody();
    if (playbackTimer) clearInterval(playbackTimer);
  }}

  function updatePlayStateUI() {{
    const mainIcon = document.getElementById('main-play-icon');
    const mainBtn = document.getElementById('btn-main-play');
    const barPlayBtn = document.getElementById('player-bar-play-btn');

    if (isPlaying) {{
      if (mainIcon) mainIcon.innerText = '⏸';
      if (mainBtn) mainBtn.innerHTML = '<span>⏸</span> 暂停琴音伴奏';
      if (barPlayBtn) barPlayBtn.innerText = '⏸';
    }} else {{
      if (mainIcon) mainIcon.innerText = '▶';
      if (mainBtn) mainBtn.innerHTML = '<span>▶</span> 播放钢琴伴奏';
      if (barPlayBtn) barPlayBtn.innerText = '▶';
    }}

    // Update active sidebar wave
    document.querySelectorAll('.hymn-item').forEach((item, idx) => {{
      item.classList.toggle('is-playing', isPlaying && idx === currentHymnIndex);
    }});
  }}

  function updateProgressUI() {{
    document.getElementById('disp-curr-time').innerText = formatTime(playbackProgress);
    const pct = Math.min(100, (playbackProgress / totalPlaybackDuration) * 100);
    document.getElementById('progress-bar-fill').style.width = `${{pct}}%`;
  }}

  function seekAudio(e) {{
    const container = document.getElementById('progress-container');
    const rect = container.getBoundingClientRect();
    const pos = (e.clientX - rect.left) / rect.width;
    playbackProgress = Math.round(pos * totalPlaybackDuration);
    updateProgressUI();
  }}

  function prevHymn() {{
    let nextIdx = currentHymnIndex - 1;
    if (nextIdx < 0) nextIdx = HYMNS_DATABASE.length - 1;
    loadHymn(nextIdx);
    startPlayback();
  }}

  function nextHymn() {{
    let nextIdx = currentHymnIndex + 1;
    if (nextIdx >= HYMNS_DATABASE.length) nextIdx = 0;
    loadHymn(nextIdx);
    startPlayback();
  }}

  function toggleLoopMode() {{
    isLooping = !isLooping;
    const btn = document.getElementById('btn-loop-mode');
    btn.style.color = isLooping ? 'var(--gold-primary)' : 'var(--text-secondary)';
    btn.title = isLooping ? '当前：单曲循环' : '当前：顺序播放';
  }}

  function toggleAudioEngine() {{
    alert('已启用内置标准钢琴合成器，为信徒提供最精准的视唱伴奏！');
  }}

  // Video Modal
  function openVideoModal() {{
    const hymn = HYMNS_DATABASE[currentHymnIndex];
    document.getElementById('video-modal-title').innerText = `🎬 敬拜赞美视频 · 《${{hymn.title}}》`;
    const box = document.getElementById('video-embed-box');
    
    // YouTube embed with fallback search
    const ytid = hymn.youtubeId || '';
    if (ytid) {{
      box.innerHTML = `<iframe src="https://www.youtube.com/embed/${{ytid}}?autoplay=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
    }} else {{
      box.innerHTML = `<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#fff;gap:12px;padding:20px;text-align:center;">
        <p style="font-size:16px;">《${{hymn.title}}》敬拜合唱与赞美视频</p>
        <a href="https://www.youtube.com/results?search_query=${{encodeURIComponent(hymn.videoSearch || hymn.title)}}" target="_blank" style="padding:10px 20px;background:#EF4444;color:#fff;border-radius:8px;text-decoration:none;font-weight:bold;">在 YouTube 上观看教会敬拜合唱 →</a>
      </div>`;
    }}
    document.getElementById('video-modal').classList.add('open');
  }}

  function closeVideoModal() {{
    document.getElementById('video-modal').classList.remove('open');
    document.getElementById('video-embed-box').innerHTML = '';
  }}

  // Themes
  function toggleTheme() {{
    const html = document.documentElement;
    const icon = document.getElementById('theme-btn-icon');
    if (html.classList.contains('dark-theme')) {{
      html.classList.remove('dark-theme');
      html.classList.add('light-theme');
      icon.innerText = '☀️';
    }} else if (html.classList.contains('light-theme')) {{
      html.classList.remove('light-theme');
      html.classList.add('sepia-theme');
      icon.innerText = '📜';
    }} else {{
      html.classList.remove('sepia-theme');
      html.classList.add('dark-theme');
      icon.innerText = '🌓';
    }}
  }}

  function formatTime(sec) {{
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
  }}

  function initKeyboardShortcuts() {{
    window.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT') return;
      if (e.code === 'Space') {{
        e.preventDefault();
        togglePlay();
      }} else if (e.code === 'ArrowLeft') {{
        e.preventDefault();
        prevHymn();
      }} else if (e.code === 'ArrowRight') {{
        e.preventDefault();
        nextHymn();
      }} else if (e.code === 'Escape') {{
        closeVideoModal();
      }}
    }});
  }}

  // Boot
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initApp);
  }} else {{
    initApp();
  }}
</script>
</body>
</html>
'''
    import shutil
    os.makedirs('pages_dist/hymns', exist_ok=True)
    os.makedirs('Google云端硬盘上传发布包/hymns', exist_ok=True)

    with open('pages_dist/hymns.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    with open('pages_dist/hymns/index.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    print("Successfully generated pages_dist/hymns.html & index.html")

    with open('hymns.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    with open('hymns/index.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    print("Successfully generated hymns.html & hymns/index.html")

    with open('Google云端硬盘上传发布包/hymns.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    with open('Google云端硬盘上传发布包/hymns/index.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
    print("Successfully copied to Google云端硬盘上传发布包/hymns.html & index.html")

    shutil.copyfile('hymns/hymns_data.js', 'pages_dist/hymns/hymns_data.js')
    shutil.copyfile('hymns/hymns_data.js', 'Google云端硬盘上传发布包/hymns/hymns_data.js')
    print("Successfully synced hymns_data.js to dist directories")

if __name__ == '__main__':
    generate_hymns_html()
