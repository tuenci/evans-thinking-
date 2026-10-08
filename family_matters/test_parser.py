import re

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
        html = ['<div class="table-responsive"><table class="styled-table">']
        # header
        headers = [c.strip() for c in rows[0].split('|')[1:-1]]
        html.append('<thead><tr>' + ''.join(f'<th>{inline_format(h)}</th>' for h in headers) + '</tr></thead>')
        html.append('<tbody>')
        for r in rows[2:]: # skip separator
            cols = [c.strip() for c in r.split('|')[1:-1]]
            html.append('<tr>' + ''.join(f'<td>{inline_format(c)}</td>' for c in cols) + '</tr>')
        html.append('</tbody></table></div>')
        return '\n'.join(html)

    def inline_format(text):
        # bold italic
        text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        # bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        # italic
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text

    for line in lines:
        raw = line.strip()
        
        # skip page markers
        if raw.startswith('<!-- Page'):
            continue
        # skip horizontal rules
        if raw in ['---', '***', '___']:
            output.extend(close_blocks())
            output.append('<hr class="content-divider">')
            continue
            
        if not raw:
            output.extend(close_blocks())
            continue
            
        # check table
        if raw.startswith('|') and raw.endswith('|'):
            if not in_table:
                output.extend(close_blocks())
                in_table = True
                table_rows = []
            table_rows.append(raw)
            continue
        elif in_table:
            output.extend(close_blocks())
            
        # check blockquote
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

        # check headings
        if raw.startswith('#'):
            output.extend(close_blocks())
            m = re.match(r'^(#{1,6})\s+(.*)$', raw)
            if m:
                level = len(m.group(1))
                h_text = inline_format(m.group(2))
                if level == 1:
                    # Level 1 is usually chapter title, ignore or make h2
                    continue
                elif level == 2 or level == 3:
                    output.append(f'<h3 class="{subheading_cls}">{h_text}</h3>')
                else:
                    output.append(f'<h4 class="{minorheading_cls}">{h_text}</h4>')
                continue
                
        # check unordered list
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

        # check ordered list
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
            
        # Regular paragraph
        output.append(f'<p>{inline_format(raw)}</p>')
        
    output.extend(close_blocks())
    return '\n'.join(output)

sample_md = """
### 测试标题
这是一个段落，带有**粗体**与*斜体*。

> 这是引言名言
> 第二行

- 列表项一
- 列表项二

1. 第一项
2. 第二项

| 列一 | 列二 |
| --- | --- |
| 内容A | 内容B |
"""

print(markdown_to_html(sample_md, 'zh'))
