from bs4 import BeautifulSoup
from utils import filex, jsonx

CLASS_NAME_CONTENT = 'section-inner sectionLayout--insetColumn'
UNICODE_REPLACES = [
    ['\u2019', '\''],
    ['\u201c', '"'],
    ['\u201d', '"'],
    ['\u2026', '...'],
]


def _clean(str):
    str = str.strip()
    for [before, after] in UNICODE_REPLACES:
        str = str.replace(before, after)
    return str


def medium_html_to_docjson(html_file, docjson_file):
    html = filex.read(html_file)
    html = html.replace('<br>', '\n')
    soup = BeautifulSoup(html, 'html.parser')

    docjson = []

    first_title = True
    sections = soup.find_all('div', class_=CLASS_NAME_CONTENT)
    for section in sections:
        for child in section.find_all():
            text = _clean(child.text)
            if child.name == 'h3':
                if first_title:
                    docjson.append(dict(tag='title', text=text))
                    first_title = False
                else:
                    docjson.append(dict(tag='h1', text=text))
            elif child.name == 'h4':
                docjson.append(dict(tag='h2', text=text))
            elif child.name == 'p':
                docjson.append(dict(tag='p', text=text))
            elif child.name == 'blockquote':
                docjson.append(dict(tag='blockquote', text=text))
            elif child.name == 'li':
                docjson.append(dict(tag='li', text=text))
            elif child.name == 'pre':
                docjson.append(dict(tag='pre', text=text))
            elif child.name == 'img':
                src = child['src']
                docjson.append(dict(tag='img', src=src))
            elif child.name == 'figcaption':
                docjson.append(dict(tag='figcaption', text=f'{text}'))

        docjson.append(dict(tag='ellipsis'))

    child = soup.find('time')
    if child:
        text = _clean(child.text)
        docjson.append(dict(tag='time', text=text))

    jsonx.write(docjson_file, docjson)
    print(f'Wrote {docjson_file}')
