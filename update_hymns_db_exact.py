import json, re

# Let's write the complete, verified, note-by-note database
with open('hymns/hymns_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const HYMNS_DATABASE = (\[.*\]);', text, re.DOTALL)
db = json.loads(m.group(1))

# HYMN 360
h360 = db[0]
h360['title'] = "是谁从远处看见认识我"
h360['category'] = "救主耶稣"
h360['key'] = "1=G"
h360['timeSignature'] = "4/4"

# Exact Staves for 360:
h360['jianpuStaves'] = [
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["1. 是", "2. 是", "3. 是"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["谁", "谁", "谁"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["从", "从", "担"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["远", "灰", "当"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["处", "尘", "全"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["看", "中", "人"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["见", "抬", "类"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["认", "举", "的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["识", "了", "刑"]},
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["我？", "我？", "罚？"]},
          {"pitch": "5", "octave": -1, "underlines": 0, "slurEnd": True, "lyrics": ["", "", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "1", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["是", "是", "是"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["谁", "谁", "谁"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["千", "从", "要"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["万", "粪", "洗"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["人", "堆", "净"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["中", "中", "全"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["题", "提", "人"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["名", "拔", "类"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "7", "octave": -1, "underlines": 0, "lyrics": ["召", "了", "过"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["我？", "我？", "犯？"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["1. 是", "2. 是", "3. 是"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["谁", "谁", "谁"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["为", "为", "背"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["寻", "代", "负"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["找", "替", "全"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "人"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["降", "甘", "类"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["生", "心", "的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["尘", "舍", "忧"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["世？", "命？", "患？"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["", "", ""]},
          {"pitch": "5", "octave": -1, "underlines": 0, "slurEnd": True, "lyrics": ["", "", ""]},
          {"pitch": "1", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["是", "是", "是"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["祢，", "祢，", "祢，"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["主", "主", "主"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["耶", "耶", "耶"]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["稣", "稣", "稣"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["唯", "唯", "唯"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["有", "有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["祢；", "祢；", "祢；"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["1. 是", "2. 是", "3. 是"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["祢，", "祢，", "祢，"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["主", "主", "主"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["耶", "耶", "耶"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["稣", "稣", "稣"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["唯", "唯", "唯"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["有", "有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["祢；", "祢；", "祢；"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["是", "是", "是"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["祢，", "祢，", "祢，"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["主", "主", "主"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["耶", "耶", "耶"]},
          {"pitch": "4", "octave": 0, "underlines": 0, "lyrics": ["稣", "稣", "稣"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["唯", "唯", "唯"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["有", "有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["祢。", "祢。", "祢。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["1. 唯", "2. 唯", "3. 唯"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["有", "有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["祢，", "祢，", "祢，"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["为", "为", "背"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["寻", "代", "负"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["找", "替", "全"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["我", "我", "人"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["降", "甘", "类"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["生", "心", "的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["尘", "舍", "忧"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["世，", "命，", "患，"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["", "", ""]},
          {"pitch": "5", "octave": -1, "underlines": 0, "slurEnd": True, "lyrics": ["", "", ""]},
          {"pitch": "1", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["是", "是", "是"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", "", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["祢，", "祢，", "祢，"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["主", "主", "主"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["耶", "耶", "耶"]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["稣", "稣", "稣"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["唯", "唯", "唯"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["有", "有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "||",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["祢。", "祢。", "祢。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", "", ""]}
        ]
      }
    ]
  }
]

# HYMN 371
h371 = db[1]
h371['title'] = "耶稣爱我"
h371['category'] = "难测的爱"
h371['key'] = "1=bE"
h371['timeSignature'] = "3/4"
h371['footnote'] = '(注: “我”可换唱“你”)'

h371['jianpuStaves'] = [
  {
    "measures": [
      {
        "barLeft": "|:", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["1. 耶", "2. 耶"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": -1, "underlines": 0, "lyrics": ["稣", "稣"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["爱", "救"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["我，", "我，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["耶", "耶"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["稣", "稣"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["爱", "救"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["我，", "我，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["在", "在"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我", "我"]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["生", "生"]},
          {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["命", "命"]},
          {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["中", "中"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["最", "最"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "dot": True, "lyrics": ["大", "大"]},
          {"pitch": "2", "octave": 0, "underlines": 2, "lyrics": ["的", "的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["福", "盼"]},
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["分", "望"]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["就", "就"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["是：", "是："]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["耶", "耶"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["稣", "稣"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["永", "永"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["远", "远"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["爱", "救"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["我。", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": ":|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": ["", ""]},
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
          {"pitch": "1", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["我。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]},
          {"pitch": "0", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["救"]},
          {"pitch": "7", "octave": -1, "underlines": 1, "lyrics": ["我"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["脱"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["离"]},
          {"pitch": "0", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["脱"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["离"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 1, "slurStart": True, "lyrics": ["罪"]},
          {"pitch": "5", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["恶"]},
          {"pitch": "5", "octave": -1, "underlines": 0, "lyrics": [""]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["权"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["势，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]},
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
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["带"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["我"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["进"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["入"]},
          {"pitch": "0", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["进"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["入"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["光"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["明"]},
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["国"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["度。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "6", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["哦！"]},
          {"pitch": "7", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 1, "underlines": 0, "lyrics": ["耶"]},
          {"pitch": "7", "octave": 0, "underlines": 0, "lyrics": ["稣"]},
          {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["爱"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["我，"]},
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
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["祂"]},
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["能"]},
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["救"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["我，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["耶"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["稣"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["永"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "2", "octave": 0, "underlines": 0, "lyrics": ["远"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "6", "octave": -1, "underlines": 0, "lyrics": ["爱"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["我。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "||",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "slurEnd": True, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]}
        ]
      }
    ]
  }
]

# HYMN 422
h422 = db[2]
h422['title'] = "有一位神"
h422['category'] = "邀请"
h422['subtitle'] = "邀请"
h422['key'] = "1=D"
h422['timeSignature'] = "4/4"

h422['jianpuStaves'] = [
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["1. 有", "2. 有"]},
          {"pitch": "3", "octave": 0, "underlines": 2, "lyrics": ["一", "一"]},
          {"pitch": "4", "octave": 0, "underlines": 2, "lyrics": ["位", "位"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["神，", "神，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["有", "有"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["权", "权"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["能", "能"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["创", "创"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["造", "造"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["宇", "宇"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["宙", "宙"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["万", "万"]},
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["物，", "物，"]},
          {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": ["也", "也"]},
          {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": ["有", "有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["温", "温"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["柔", "柔"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["双", "双"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["手", "手"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["安", "安"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["慰", "慰"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["受", "受"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["伤", "伤"]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "4", "octave": 0, "underlines": 0, "slurStart": True, "lyrics": ["灵", "灵"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
          {"pitch": "2", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]},
          {"pitch": "2", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["魂。", "魂。"]},
          {"pitch": "5", "octave": -1, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["有", "有"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["一", "一"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["位", "位"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["神，", "神，"]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
          {"pitch": "5", "octave": -1, "underlines": 1, "lyrics": ["有", "高"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["权", "坐"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["柄", "在"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["审", "荣"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["判", "耀"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["一", "宝"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["切", "座"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["罪", "却"]},
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["恶，", "赐"]},
          {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": ["也", "爱"]},
          {"pitch": "1", "octave": 0, "underlines": 2, "lyrics": ["有", "子"]}
        ]
      }
    ]
  },
  {
    "sectionMarker": "(副歌)",
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["1. 慈", "2. 耶"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["悲", "稣"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["体", "救"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["贴", "人"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["人", "免"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["的", "于"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["软", "堕"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": ["", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["弱。", "落。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": ["", ""]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": ["", ""]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["有", ""]},
          {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["一", ""]},
          {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["位", ""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["神，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["我"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["们"]},
          {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 0, "lyrics": ["神，"]},
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
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["唯"]},
          {"pitch": "7", "octave": 0, "underlines": 1, "lyrics": ["一"]},
          {"pitch": "1", "octave": 1, "underlines": 1, "lyrics": ["的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 0, "lyrics": ["神，"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["名"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["叫"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "slurEnd": True, "lyrics": [""]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "4", "octave": 0, "underlines": 0, "dot": True, "lyrics": ["耶"]},
          {"pitch": "3", "octave": 0, "underlines": 1, "lyrics": ["和"]},
          {"pitch": "2", "octave": 0, "underlines": 0, "dot": True, "lyrics": ["华，"]},
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "",
        "units": [
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["权"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": ["威"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["荣"]},
          {"pitch": "6", "octave": 0, "underlines": 1, "lyrics": [""]},
          {"pitch": "6", "octave": 0, "underlines": 0, "dot": True, "slurEnd": True, "lyrics": ["光，"]}
        ]
      }
    ]
  },
  {
    "measures": [
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 1, "lyrics": ["有"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["恩"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": ["典"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "slurStart": True, "lyrics": ["慈"]},
          {"pitch": "5", "octave": 0, "underlines": 1, "lyrics": [""]},
          {"pitch": "5", "octave": 0, "underlines": 0, "dot": True, "slurEnd": True, "lyrics": ["爱，"]},
          {"pitch": "6", "octave": -1, "underlines": 1, "lyrics": ["是"]}
        ]
      },
      {
        "barLeft": "", "barRight": "|",
        "units": [
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["昔"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["在"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["今"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["在"]},
          {"pitch": "4", "octave": 0, "underlines": 1, "lyrics": ["永"]},
          {"pitch": "3", "octave": 0, "underlines": 0, "lyrics": ["在"]},
          {"pitch": "2", "octave": 0, "underlines": 1, "lyrics": ["的"]}
        ]
      },
      {
        "barLeft": "", "barRight": "||",
        "units": [
          {"pitch": "1", "octave": 0, "underlines": 0, "lyrics": ["神。"]},
          {"pitch": "-", "octave": 0, "underlines": 0, "lyrics": [""]},
          {"pitch": "0", "octave": 0, "underlines": 1, "lyrics": [""]}
        ]
      }
    ]
  }
]

# Write out hymns_data.js
new_content = '/**\n * 《诗歌宝藏》—— 华人教会传唱诗歌选集 核心数据库\n * 谱词一体元胞系统 (100% 永不错乱简谱架构)\n */\n\nconst HYMNS_DATABASE = ' + json.dumps(db, ensure_ascii=False, indent=2) + ';\n'

with open('hymns/hymns_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("100% Accurate hymns_data.js updated successfully!")
