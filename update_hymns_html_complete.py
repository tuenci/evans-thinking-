import json
import re

# Read complete 9 hymns from hymns/hymns_data.js
with open('hymns/hymns_data.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

m = re.search(r'const HYMNS_DATABASE = (\[.*\]);', js_text, re.DOTALL)
db_json_str = m.group(1)
complete_db = json.loads(db_json_str)
print(f"Loaded {len(complete_db)} hymns from hymns_data.js")

with open('hymns.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update cover index list
old_cover_list_regex = r'<span class="cover-index-count"[^>]*>.*?</div>\s*</div>\s*</div>'
new_cover_html = """<span class="cover-index-count" id="cover-index-count">共 9 首精选诗歌</span>
          </div>
          <div class="cover-index-list" id="cover-index-list">
            <div class="cover-index-item" onclick="loadHymn(0)">
              <span class="cover-item-name">是谁从远处看见认识我</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(1)">
              <span class="cover-item-name">耶稣爱你</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(2)">
              <span class="cover-item-name">有一位神</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(3)">
              <span class="cover-item-name">时空不能隔绝祂的爱</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(4)">
              <span class="cover-item-name">让我回到那起初的爱</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(5)">
              <span class="cover-item-name">坐在宝座上圣洁羔羊</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(6)">
              <span class="cover-item-name">神啊我的心切慕祢</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(7)">
              <span class="cover-item-name">有福的确据</span>
              <span class="cover-item-arrow">→</span>
            </div>
            <div class="cover-index-item" onclick="loadHymn(8)">
              <span class="cover-item-name">我的神我要敬拜祢</span>
              <span class="cover-item-arrow">→</span>
            </div>
          </div>
        </div>"""

pattern_cover = re.compile(r'<span class="cover-index-count"[^>]*>.*?</div>\s*</div>\s*</div>', re.DOTALL)
if pattern_cover.search(html):
    html = pattern_cover.sub(new_cover_html, html, count=1)
    print("Cover index list updated.")
else:
    print("WARNING: cover index list pattern not found!")

# 2. Update HYMNS_DATABASE inline
start = html.find('const HYMNS_DATABASE = ')
nxt = html.find('let currentHymnIndex', start)
semicolon_idx = html.rfind('];', start, nxt)
if start != -1 and semicolon_idx != -1:
    new_db_chunk = f"const HYMNS_DATABASE = {json.dumps(complete_db, ensure_ascii=False, indent=2)};"
    html = html[:start] + new_db_chunk + html[semicolon_idx+2:]
    print("HYMNS_DATABASE inline updated.")
else:
    print("WARNING: HYMNS_DATABASE inline not replaced!")

# 3. Update HYMN_PINYIN_MAP
new_pinyin_map = """const HYMN_PINYIN_MAP = {
    '360': ['swcy', 'swcykjrsw', 'sscy', 'shishicongyuan', 'shishicongyuanchukanjianrenshiwo'],
    '371': ['ysaw', 'yesuaiwo', 'yaw', 'ysan', 'yesuaini', 'yan'],
    '422': ['yyws', 'yws', 'youyiweishen', 'ywsh'],
    '447': ['skbn', 'skbngjtda', 'shikongbuneng', 'shikongbunenggejuedadeai', 'axlsm'],
    '471': ['rwht', 'rangwohuidaonaqichudeai', 'qicd', 'qichudeai', 'zwyq', 'zhuwoyaoqingni'],
    '476': ['zzbz', 'zuozaibaozuoshangshengjiegaoyang', 'sjgy', 'shengjiegaoyang'],
    '504': ['sawd', 'shenawodexinqiemuni', 'rkqm', 'ruludeqiemuxishui', 'qmxs'],
    '531': ['yfdq', 'youfudequeju', 'yfdqj'],
    '565': ['wdsw', 'wodeshenwoyaojingbaini', 'yjbn', 'woyaojingbaini']
  };"""

pinyin_pattern = re.compile(r'const HYMN_PINYIN_MAP = \{.*?\};', re.DOTALL)
if pinyin_pattern.search(html):
    html = pinyin_pattern.sub(new_pinyin_map, html, count=1)
    print("HYMN_PINYIN_MAP updated.")
else:
    print("WARNING: HYMN_PINYIN_MAP pattern not found!")

# 4. Update songIdMap in resolveAudioUrl
new_song_map = """const songIdMap = {
        '360': '50012',
        '371': '50023',
        '422': '50210',
        '447': '50235',
        '471': '50259',
        '476': '50264',
        '504': '50446',
        '531': '50473',
        '565': '50507'
      };"""

song_map_pattern = re.compile(r'const songIdMap = \{.*?\};', re.DOTALL)
if song_map_pattern.search(html):
    html = song_map_pattern.sub(new_song_map, html, count=1)
    print("songIdMap updated.")
else:
    print("WARNING: songIdMap pattern not found!")

with open('hymns.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated hymns.html successfully.")
