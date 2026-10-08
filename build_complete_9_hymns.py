import json
import re

# Load existing hymns
with open('hymns/hymns_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const HYMNS_DATABASE = (\[.*\]);', text, re.DOTALL)
existing_db = json.loads(m.group(1))

# Keep existing 4 hymns
h360 = existing_db[0]
h371 = existing_db[1]
h422 = existing_db[2]
h447 = existing_db[3]

# Ensure h447 has 祂 everywhere
h447['title'] = "时空不能隔绝祂的爱"
h447['videoSearch'] = "赞美之泉 爱喜乐生命 时空不能隔绝祂的爱"

# HYMN 471
h471 = {
  "id": "471",
  "number": 471,
  "title": "让我回到那起初的爱",
  "subtitle": "感激的话 · 又名《主，我邀请祢》",
  "category": "感激的话",
  "key": "1=F",
  "timeSignature": "4/4",
  "author": "经典敬拜赞美诗歌 · 启示录2:4-5",
  "background": "发人深省的心灵祈祷诗歌，引自启示录第二章关于“离弃起初爱心”的警戒与大卫诗篇“为我造清洁的心”的痛切呼求。带领信徒在加略山十架恩典前彻底降服，邀请基督重新登居心之宝座。",
  "youtubeId": "W97r_50259",
  "audioUrl": "https://play.izanm.org/song/p/50259.mp3",
  "audioSourceUrl": "https://www.zanmei.ai/song/50259.html",
  "audioPlayerUrl": "https://www.zanmei.ai/player/zan.html",
  "audioBackupUrl": "https://play.j53.net/song/p/50259.mp3",
  "audioLocalUrl": "hymns/audio/50259.mp3",
  "videoSearch": "让我回到那起初的爱 主我邀请祢",
  "textScore": {
    "keySignature": "1=F",
    "timeSignature": "4/4",
    "tempo": "诚挚深情地",
    "rawText": "471  让我回到那起初的爱  1=F 4/4  感激的话\n\n|: 3  6̣ 6̣  6̣  1 4 | 3· 2  2  2  2 7̣ 1 | 2  5̣ 5̣  2 2 | 2 3 3 - - |\n1. 让我回到那起 初的   爱，让我 对祢忠贞专 一。\n2. 让我时常回到 加略   山，让我 不负祢的恩 情。\n\n   3  6̣ 6̣  6̣  1 4 | 3  2 1  2  2 1 | [1.] 7̣  3̣ - 1 | 7̣ 6̣ - - :| [2.] 7̣ 6̣ - - |\n1. 为我再造一颗 清洁的心，让我 完全 属 于祢。\n2. 为我再次融化 冰冷的心，让我 全心 爱        慕祢。\n\n(副歌)\n   1 2 | 3 3 3 3 3 3 4 | 3 2 2 2 2 5 6 | 5 5 2 4 4 3 | 3 - -\n   主，我邀请祢，恭敬的邀请祢，再登上我心的宝 座。\n\n   2 3 | 4 4 4 4 4 4 3 | 3 2 2 2 7̣ 7̣ 1 | 2 3 1 7̣ 7̣ 6̣ | 6̣ - - - ||\n   主，我邀请祢，衷心的邀请祢，再登上我心的宝 座。"
  },
  "lyrics": [
    {
      "section": "",
      "lines": [
        "1. 让我回到那起初的爱，让我对祢忠贞专一。",
        "为我再造一颗清洁的心，让我完全属于祢。"
      ]
    },
    {
      "section": "",
      "lines": [
        "2. 让我时常回到加略山，让我不负祢的恩情。",
        "为我再次融化冰冷的心，让我全心爱慕祢。"
      ]
    },
    {
      "section": "",
      "lines": [
        "主，我邀请祢，恭敬的邀请祢，再登上我心的宝座。",
        "主，我邀请祢，衷心的邀请祢，再登上我心的宝座。"
      ]
    }
  ],
  "jianpuStaves": [
    {
      "measures": [
        {
          "barLeft": "|:", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["1. 让", "2. 让"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["我", "我"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["回", "时"]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["到", "常"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["那", "回"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["起", "到"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["初", "加"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": ["的", "略"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["爱，", "山，"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["让", "让"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["我", "我"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["对", "不"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["祢", "负"]},
            {"pitch": "5", "octave": -1, "underlines": 0, "lyrics": ["忠", "祢"]},
            {"pitch": "5", "octave": -1, "underlines": 0, "lyrics": ["贞", "的"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["专", "恩"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["", ""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["一。", "情。"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
            {"pitch": "3", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["1. 为", "2. 为"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["我", "我"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["再", "再"]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["造", "次"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["一", "融"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["颗", "化"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["清", "冰"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["洁", "冷"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["的", "的"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["心，", "心，"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["让", "让"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": ":|",
          "units": [
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["完", "全"]},
            {"pitch": "3", "octave": -1, "underlines": 1, "lyrics": ["全", "心"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["属", "爱"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["于", ""]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["祢。", ""]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "7", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["", "慕"]},
            {"pitch": "6", "octave": -1, "underlines": 0, "slurEnd": True, "lyrics": ["", "祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["主，", "主，"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["邀", "邀"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["请", "请"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["祢，", "祢，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["恭", "恭"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["敬", "敬"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["的", "的"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["邀", "邀"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["请", "请"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["祢，", "祢，"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["再", "再"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["登", "登"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["上", "上"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "我"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["心", "心"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["的", "的"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["宝", "宝"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
            {"pitch": "4", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["", ""]},
            {"pitch": "4", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["座。", "座。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["主，", "主，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["邀", "邀"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["请", "请"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["祢，", "祢，"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["衷", "衷"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["心", "心"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["的", "的"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["邀", "邀"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["请", "请"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["祢，", "祢，"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["再", "再"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["登", "登"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["上", "上"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["我", "我"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["心", "心"]}
          ]
        },
        {
          "barLeft": "", "barRight": "||",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["的", "的"]},
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["宝", "宝"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
            {"pitch": "7", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["", ""]},
            {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["", ""]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["座。", "座。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
          ]
        }
      ]
    }
  ]
}

# HYMN 476
h476 = {
  "id": "476",
  "number": 476,
  "title": "坐在宝座上圣洁羔羊",
  "subtitle": "赞美之声 · 启示录5:12-13",
  "category": "赞美之声",
  "key": "1=C",
  "timeSignature": "4/4",
  "author": "经典敬拜赞美诗歌 · 启示录5:12-13",
  "background": "宏伟肃穆的荣耀颂歌，全景式呈现启示录第四至五章天上千万天使与圣徒俯伏敬拜基督羔羊的壮丽图景。以层层递进的旋律高举羔羊的尊贵、权能与永恒配得。",
  "youtubeId": "W97r_50264",
  "audioUrl": "https://play.izanm.org/song/p/50264.mp3",
  "audioSourceUrl": "https://www.zanmei.ai/song/50264.html",
  "audioPlayerUrl": "https://www.zanmei.ai/player/zan.html",
  "audioBackupUrl": "https://play.j53.net/song/p/50264.mp3",
  "audioLocalUrl": "hymns/audio/50264.mp3",
  "videoSearch": "坐在宝座上圣洁羔羊 万王之王万主之主",
  "textScore": {
    "keySignature": "1=C",
    "timeSignature": "4/4",
    "tempo": "庄严崇敬地",
    "rawText": "476  坐在宝座上圣洁羔羊  1=C 4/4  赞美之声\n\n3 5 5 3 2 5 7̣ | 2· 1 1 - - | 6· 1 7̣ 1 4 6 | 5 - - - |\n坐在宝座上圣洁 羔  羊，       我们俯伏敬拜 祢，\n\n4· 1̇  7· 6 | 5 3 2 1 - | 4 3 2 1 4 3 2 1 | 2 - - - |\n昔 在，今 在 以后永在，  唯有祢是全能真   神。\n\n3 5 5 3 2 5 7̣ | 2· 1 1 - - | 6· 1 7̣ 1 4 6 | 5 - - - |\n坐在宝座上尊贵 羔  羊，       我们俯伏敬拜 祢，\n\n4· 1̇  7· 6 | 5 2̇  7 1̇ - | 6 7 1̇ 5 1̇ 7 1̇ | 2̇ - - - | 2̇ -\n颂 赞、尊 贵、荣耀、权 能，  都归给祢直到永 远。\n\n0 5 1̇ 7 | 1̇ - 0 5 1̇ 7 | 1̇ - - 0 6 7 | 1̇ 6 5 3̇ 2̇ 2̇ 1̇ 6· | 5 -\n万王之 王，  万主之 主，      唯有 祢 配得敬拜和尊  荣；\n\n0 5 1̇ 7 | 1̇ - 0 5 1̇ 7 | 1̇ - - 0 6 7 | 1̇ 6 5 3̇ 2̇  2̇ 1̇ 7· | 1̇ - - - ||\n万王之 王，  万主之 主，      我们 高举祢圣名，直到永  远。"
  },
  "lyrics": [
    {
      "section": "",
      "lines": [
        "坐在宝座上圣洁羔羊，我们俯伏敬拜祢，",
        "昔在，今在，以后永在，唯有祢是全能真神。",
        "坐在宝座上尊贵羔羊，我们俯伏敬拜祢，",
        "颂赞、尊贵、荣耀、权能，都归给祢直到永远。"
      ]
    },
    {
      "section": "",
      "lines": [
        "万王之王，万主之主，唯有祢配得敬拜和尊荣；",
        "万王之王，万主之主，我们高举祢圣名，直到永远。"
      ]
    }
  ],
  "jianpuStaves": [
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["坐"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["在"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["宝"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["座"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["上"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["圣"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["洁"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["羔"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": [""]},
            {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["羊，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["我"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["们"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["俯"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["伏"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["拜"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["昔"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["在，"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["今"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["在"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["以"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["后"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["永"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["在，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["唯"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["有"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["祢"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["是"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["全"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["能"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["真"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["神。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["坐"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["在"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["宝"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["座"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["上"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["尊"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["贵"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["羔"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": [""]},
            {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["羊，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["我"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["们"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["俯"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["伏"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["拜"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["颂"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["赞、"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["尊"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["贵、"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["荣"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["耀、"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "lyrics": ["权"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["能，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["都"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "lyrics": ["归"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["给"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["直"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "lyrics": ["到"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["永"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "2", "octave": 1, "underlines": 0, "lyrics": ["远。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["万"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["王"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["之"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["王，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["万"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["主"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["之"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["主，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "0", "octave": 0, "underlines": 2, "lyrics": [""]},
            {"pitch": "6", "octave": 0, "underlines": 2, "lyrics": ["唯"]},
            {"pitch": "7", "octave": 0, "underlines": 2, "lyrics": ["有"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "slurStart": True, "lyrics": ["祢"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["配"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["得"]},
            {"pitch": "3", "octave": 1, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["拜"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["和"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["尊"]},
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["荣；"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["万"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["王"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["之"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["王，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["万"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["主"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["之"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["主，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "0", "octave": 0, "underlines": 2, "lyrics": [""]},
            {"pitch": "6", "octave": 0, "underlines": 2, "lyrics": ["我"]},
            {"pitch": "7", "octave": 0, "underlines": 2, "lyrics": ["们"]}
          ]
        },
        {
          "barLeft": "", "barRight": "||",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["高"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["举"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["祢"]},
            {"pitch": "3", "octave": 1, "underlines": 1, "lyrics": ["圣"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["名，"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["直"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["到"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["永"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["远。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    }
  ]
}

# HYMN 504
h504 = {
  "id": "504",
  "number": 504,
  "title": "神啊我的心切慕祢",
  "subtitle": "圣洁的追求 · 又名《如鹿切慕溪水》",
  "category": "圣洁追求",
  "key": "1=D",
  "timeSignature": "4/4",
  "author": "词/曲：Martin Nystrom (1984) · 诗篇42:1",
  "background": "享誉全球的传世灵修圣乐，中文常译《如鹿切慕溪水》。取意诗篇第四十二篇第一节“神啊，我的心切慕祢，如鹿切慕溪水”，以清纯婉转、如清泉流淌般的曲调抒发向着神纯粹专一的渴慕与全人奉献。",
  "youtubeId": "W97r_50446",
  "audioUrl": "https://play.izanm.org/song/p/50446.mp3",
  "audioSourceUrl": "https://www.zanmei.ai/song/50446.html",
  "audioPlayerUrl": "https://www.zanmei.ai/player/zan.html",
  "audioBackupUrl": "https://play.j53.net/song/p/50446.mp3",
  "audioLocalUrl": "hymns/audio/50446.mp3",
  "videoSearch": "如鹿切慕溪水 神啊我的心切慕你 Martin Nystrom",
  "textScore": {
    "keySignature": "1=D",
    "timeSignature": "4/4",
    "tempo": "安详渴望地",
    "rawText": "504  神啊我的心切慕祢  1=D 4/4  圣洁的追求\n\n3  5  5  3 2 | 1· 2  4  3 2 1 | 6  6  5· 4 | 5 - - - |\n神 啊，我 的心 切 慕 祢，如     鹿 切 慕 溪 水，\n\n3  5  5  3 2 | 1· 2  4  3 2 1 | 1· 3  2· 1 | 1 - - - |\n唯 有 祢 是我 心 所 爱，我渴   慕 来 敬 拜 祢。\n\n1̇  1̇  1̇  1̇ 7 | 6  6  5· 1 | 6  6  6  6 5 | 4  4  3 - |\n祢 是 我 的力 量 盾 牌，我 灵 单 单 降    服 于 祢，\n\n3  5  5  3 2 | 1· 2  4  3 2 1 | 1· 3  2· 1 | 1 - - - ||\n唯 有 祢 是我 心 所 爱，我渴   慕 来 敬 拜 祢。"
  },
  "lyrics": [
    {
      "section": "",
      "lines": [
        "神啊，我的心切慕祢，如鹿切慕溪水，",
        "唯有祢是我心所爱，我渴慕来敬拜祢。"
      ]
    },
    {
      "section": "",
      "lines": [
        "祢是我的力量盾牌，我灵单单降服于祢，",
        "唯有祢是我心所爱，我渴慕来敬拜祢。"
      ]
    }
  ],
  "jianpuStaves": [
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["神"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["啊，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["我"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["的"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["心"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["切"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["慕"]},
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["祢，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["如"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["鹿"]},
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["切"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["慕"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["溪"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["水，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["唯"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["有"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["是"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["心"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["所"]},
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["爱，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["渴"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["慕"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["来"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["敬"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["拜"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["祢"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["是"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["我"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["的"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["力"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["量"]},
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["盾"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["牌，"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["灵"]},
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["单"]},
            {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["单"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["降"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["服"]},
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["于"]},
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["祢，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["唯"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["有"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["是"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["心"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["所"]},
            {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["爱，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["渴"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["慕"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["来"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["敬"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["拜"]}
          ]
        },
        {
          "barLeft": "", "barRight": "||",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    }
  ]
}

# HYMN 531
h531 = {
  "id": "531",
  "number": 531,
  "title": "有福的确据",
  "subtitle": "相信与进入 · Blessed Assurance",
  "category": "相信与进入",
  "key": "1=D",
  "timeSignature": "9/8",
  "author": "词：Fanny Crosby (1873) · 曲：Phoebe Knapp",
  "background": "十九世纪盲人女诗人芬尼·克罗斯比最广为人知的巅峰力作。以坚定、明亮而饱含天国喜乐的9/8拍摇曳节拍，宣告在基督救恩里的无上确据与荣耀盼望，数百年间激励无数圣徒。",
  "youtubeId": "W97r_50473",
  "audioUrl": "https://play.izanm.org/song/p/50473.mp3",
  "audioSourceUrl": "https://www.zanmei.ai/song/50473.html",
  "audioPlayerUrl": "https://www.zanmei.ai/player/zan.html",
  "audioBackupUrl": "https://play.j53.net/song/p/50473.mp3",
  "audioLocalUrl": "hymns/audio/50473.mp3",
  "videoSearch": "有福的确据 Blessed Assurance 芬尼克罗斯比",
  "textScore": {
    "keySignature": "1=D",
    "timeSignature": "9/8",
    "tempo": "欢欣笃定地",
    "rawText": "531  有福的确据  1=D 9/8  相信与进入\n\n   3 2 1 | 5· 5·  4 5 6 | 5· 5· 5 3 5 | 1̇· 7· 6 5 #4 | 5· 5·\n1. 有福的   确 据，耶 稣属 我，何 等的   荣 耀 向我显   明，\n2. 完全顺   服 主，我 灵欢 喜，天 堂的   荣 耀 显于我   心，\n3. 完全献   与 主，万 事安 宁，荣 耀的   圣 灵 充满我   心，\n\n   3 2 1 | 5· 5·  4 5 6 | 5· 5· 1 2 3 | 4· 2· 1 2 7̣ | 1· 1·\n1. 被救主   赎 回 为 神后 嗣，藉 宝 血   洗 罪，圣灵重  生。\n2. 仿佛有   天 使 由 天降 临，报 明 主   慈 爱，并主怜  悯。\n3. 时刻仰   望 主，儆 醒等 候，不 住 地   祈 祷，到主再  临。\n\n(副歌)\n   5 5 5 | 1̇· 5·  6 6 6 | 5· 5· 5 5 5 | 6· 1̇· 7 7 6 | 7· 7·\n   这是我   信 息，是 我诗 歌，赞 美我   救 主，心里欢  畅；\n\n   7 1̇ 2̇ | 1̇· 5·  6 5 6 | 5· 5· 1 2 3 | 4· 2· 1· 2 7̣ | 1· 1· ||\n   这是我   信 息，是 我诗 歌，赞 美我   救 主，昼夜不   分。"
  },
  "lyrics": [
    {
      "section": "",
      "lines": [
        "1. 有福的确据，耶稣属我，何等的荣耀向我显明，",
        "被救主赎回为神后嗣，藉宝血洗罪，圣灵重生。"
      ]
    },
    {
      "section": "",
      "lines": [
        "2. 完全顺服主，我灵欢喜，天堂的荣耀显于我心，",
        "仿佛有天使由天降临，报明主慈爱，并主怜悯。"
      ]
    },
    {
      "section": "",
      "lines": [
        "3. 完全献与主，万事安宁，荣耀的圣灵充满我心，",
        "时刻仰望主，儆醒等候，不住地祈祷，到主再临。"
      ]
    },
    {
      "section": "",
      "lines": [
        "这是我信息，是我诗歌，赞美我救主，心里欢畅；",
        "这是我信息，是我诗歌，赞美我救主，昼夜不分。"
      ]
    }
  ],
  "jianpuStaves": [
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["1. 有", "2. 完", "3. 完"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["福", "全", "全"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["的", "顺", "献"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["确", "服", "与"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["据，", "主，", "主，"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["耶", "我", "万"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["稣", "灵", "事"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["属", "欢", "安"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["我，", "喜，", "宁，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["", "", ""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["何", "天", "荣"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["等", "堂", "耀"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["的", "的", "的"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["荣", "荣", "圣"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["耀", "耀", "灵"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["向", "显", "充"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "于", "满"]},
            {"pitch": "#4", "octave": 0, "underlines": 1, "lyrics": ["显", "我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["明，", "心，", "心，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurEnd": True, "lyrics": ["", "", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["1. 被", "2. 仿", "3. 时"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["救", "佛", "刻"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["主", "有", "仰"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["赎", "天", "望"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["回", "使", "主，"]},
            {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["为", "由", "儆"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["神", "天", "醒"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["后", "降", "等"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["嗣，", "临，", "候，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["", "", ""]},
            {"pitch": "1", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["藉", "报", "不"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["宝", "明", "住"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["血", "主", "地"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["洗", "慈", "祈"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["罪，", "爱，", "祷，"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["圣", "并", "到"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["灵", "主", "主"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["重", "怜", "再"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["生。", "悯。", "临。"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "slurEnd": True, "lyrics": ["", "", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["这", "这", "这"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["是", "是", "是"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["信", "信", "信"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["息，", "息，", "息，"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["是", "是", "是"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "我"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["诗", "诗", "诗"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["歌，", "歌，", "歌，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["", "", ""]},
            {"pitch": "5", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["赞", "赞", "赞"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["美", "美", "美"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["救", "救", "救"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["主，", "主，", "主，"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["心", "心", "心"]},
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["里", "里", "里"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["欢", "欢", "欢"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["畅；", "畅；", "畅；"]},
            {"pitch": "7", "octave": 0, "underlines": 0, "dotted": True, "slurEnd": True, "lyrics": ["", "", ""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["这", "这", "这"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["是", "是", "是"]},
            {"pitch": "2", "octave": 1, "underlines": 1, "lyrics": ["我", "我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["信", "信", "信"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["息，", "息，", "息，"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["是", "是", "是"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "我"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["诗", "诗", "诗"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["歌，", "歌，", "歌，"]},
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["", "", ""]},
            {"pitch": "1", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["赞", "赞", "赞"]},
            {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["美", "美", "美"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "我"]}
          ]
        },
        {
          "barLeft": "", "barRight": "||",
          "units": [
            {"pitch": "4", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["救", "救", "救"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["主，", "主，", "主，"]},
            {"pitch": "1", "octave": 0, "underlines": 1, "dotted": True, "lyrics": ["昼", "昼", "昼"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "lyrics": ["夜", "夜", "夜"]},
            {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["不", "不", "不"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["分。", "分。", "分。"]},
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "slurEnd": True, "lyrics": ["", "", ""]}
          ]
        }
      ]
    }
  ]
}

# HYMN 565
h565 = {
  "id": "565",
  "number": 565,
  "title": "我的神我要敬拜祢",
  "subtitle": "完全的满足 · 诗篇16:11",
  "category": "完全的满足",
  "key": "1=C",
  "timeSignature": "4/4",
  "author": "华人经典敬拜赞美诗歌 · 诗篇16:11",
  "background": "真挚甘甜的灵修敬拜短歌。以极其温润而倾心吐意的旋律，向至高造物主献上深情的爱与感恩。字字句句化用大卫诗篇“祢是我心灵的满足，祢是我唯一的喜乐”，深得数代信徒热爱。",
  "youtubeId": "W97r_50507",
  "audioUrl": "https://play.izanm.org/song/p/50507.mp3",
  "audioSourceUrl": "https://www.zanmei.ai/song/50507.html",
  "audioPlayerUrl": "https://www.zanmei.ai/player/zan.html",
  "audioBackupUrl": "https://play.j53.net/song/p/50507.mp3",
  "audioLocalUrl": "hymns/audio/50507.mp3",
  "videoSearch": "我的神我要敬拜祢 祢是我心灵的满足 赞美诗",
  "textScore": {
    "keySignature": "1=C",
    "timeSignature": "4/4",
    "tempo": "深情甘甜地",
    "rawText": "565  我的神我要敬拜祢  1=C 4/4  完全的满足\n\n3 5 | 5· 3 2 3 2 1 | 1 - - 3 5 | 6· 1̇ 1̇ 6 1̇ | 5 - -\n我的  神，我要敬拜 祢，    我的  心 深深地爱 祢。\n\n3 5 | 6· 3 2 3 2 1 | 1· 6̣ 6̣ 6 6 | 5· 3 2 3 2 1 | 1 - -\n在祢  宝座前，我思想 祢恩典， 我的  神，我要敬拜 祢。\n\n3 5 | 1̇· 1̇ 1̇ 3 6 | 5· 3 5 3 5 | 1̇· 1̇ 1̇ 6 3 | 5 - -\n祢是  我心灵的满 足，      祢是  我唯一的喜 乐。\n\n3 5 | 6· 3 2 3 2 1 | 1· 6̣ 6̣ 6 6 | 5· 3 2 3 2 1 | 1 - - ||\n在祢  宝座前，我思想 祢恩典， 我的  神，我要敬拜 祢。"
  },
  "lyrics": [
    {
      "section": "",
      "lines": [
        "我的神，我要敬拜祢，我的心深深地爱祢。",
        "在祢宝座前，我思想祢恩典，我的神，我要敬拜祢。"
      ]
    },
    {
      "section": "",
      "lines": [
        "祢是我心灵的满足，祢是我唯一的喜乐。",
        "在祢宝座前，我思想祢恩典，我的神，我要敬拜祢。"
      ]
    }
  ],
  "jianpuStaves": [
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["的"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["神，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["要"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurStart": True, "lyrics": ["拜"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["祢，"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["的"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["心"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["深"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["深"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["地"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["爱"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["在"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["祢"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["宝"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["座"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["前，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurStart": True, "lyrics": ["思"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": ["想"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["祢"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["恩"]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["典，"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["的"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["神，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["要"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurStart": True, "lyrics": ["拜"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["祢"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["是"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["我"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["心"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["灵"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["的"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["满"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "slurStart": True, "lyrics": ["足，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": [""]},
            {"pitch": "5", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["祢"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["是"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 1, "underlines": 0, "dotted": True, "lyrics": ["我"]},
            {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["唯"]},
            {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["一"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["的"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["喜"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["乐。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    },
    {
      "measures": [
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["在"]},
            {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["祢"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "6", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["宝"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["座"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["前，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurStart": True, "lyrics": ["思"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": ["想"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["祢"]},
            {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["恩"]},
            {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["典，"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["的"]}
          ]
        },
        {
          "barLeft": "", "barRight": "|",
          "units": [
            {"pitch": "5", "octave": 0, "underlines": 0, "dotted": True, "lyrics": ["神，"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我"]},
            {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["要"]},
            {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["敬"]},
            {"pitch": "2", "octave": 0, "underlines": 2, "slurStart": True, "lyrics": ["拜"]},
            {"pitch": "1", "octave": 0, "underlines": 2, "slurEnd": True, "lyrics": [""]}
          ]
        },
        {
          "barLeft": "", "barRight": "||",
          "units": [
            {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["祢。"]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
            {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
          ]
        }
      ]
    }
  ]
}

# The complete list of 9 hymns ordered by number
complete_hymns = [h360, h371, h422, h447, h471, h476, h504, h531, h565]
print(f"Total hymns: {len(complete_hymns)}")

# Apply mobile-adapted lyrics & ensure title 耶稣爱你
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'scratch'))
from apply_hymns_mobile_lyrics_upgrade import NEW_LYRICS_CONFIG
for idx, conf in NEW_LYRICS_CONFIG.items():
    h = complete_hymns[idx]
    h['lyrics'] = conf['sections']
    if 'title' in conf:
        h['title'] = conf['title']
    if 'audioSourceUrl' in conf:
        h['audioSourceUrl'] = conf['audioSourceUrl']
    if 'audioPlayerUrl' in conf:
        h['audioPlayerUrl'] = conf['audioPlayerUrl']
    if 'audioUrl' in conf:
        h['audioUrl'] = conf['audioUrl']
    if 'videoSearch' in conf:
        h['videoSearch'] = conf['videoSearch']
    if 'textScore_rawText' in conf and 'textScore' in h:
        h['textScore']['rawText'] = conf['textScore_rawText']
    if 'textScore_sections' in conf and 'textScore' in h:
        h['textScore']['sections'] = conf['textScore_sections']

# Write to hymns/hymns_data.js
output_js = f"// 华人经典传唱诗歌典藏数据库\n// 包含乐谱结构化数据与完整歌词，支持圣经式极简视读\nconst HYMNS_DATABASE = {json.dumps(complete_hymns, ensure_ascii=False, indent=2)};\n"
with open('hymns/hymns_data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)
print("Updated hymns/hymns_data.js")

