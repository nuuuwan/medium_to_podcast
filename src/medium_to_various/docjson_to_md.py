from utils import filex, jsonx


def docjson_to_md(docjson_file, md_file):
    """Parse."""
    docjson = jsonx.read(docjson_file)

    md_lines = []
    for d in docjson:
        tag, text = d['tag'], d.get('text')
        if tag == 'h1':
            md_lines.append(f'# {text}')
        elif tag == 'h2':
            md_lines.append(f'## {text}')
        elif tag == 'h3':
            md_lines.append(f'### {text}')
        elif tag == 'h4':
            md_lines.append(f'#### {text}')
        elif tag == 'p':
            md_lines.append(f'{text}')
        elif tag == 'blockquote':
            md_lines.append(f'>>> {text}')
        elif tag == 'li':
            md_lines.append(f'* {text}')
        elif tag == 'pre':
            md_lines.append(f'```\n{text}\n```')
        elif tag == 'img':
            src = d['src']
            md_lines.append(f'![Image]({src})')
        elif tag == 'time':
            md_lines = [f'#### {text}'] + md_lines

    content = '\n\n'.join(md_lines)
    filex.write(md_file, content)
    print(f'Wrote {md_file}')
