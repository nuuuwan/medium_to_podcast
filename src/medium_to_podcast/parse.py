"""Parse Medium Posts as HTML."""
import os
import json

from bs4 import BeautifulSoup

from utils import www

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


def parse(html_url):
    """Parse."""
    html = www.read(html_url)
    soup = BeautifulSoup(html, 'html.parser')

    data = {'paragraphs': []}

    content = soup.find('div', class_=CLASS_NAME_CONTENT)

    for child in content.find_all():
        text = _clean(child.text)
        if child.name == 'h3':
            data['title'] = text
        elif child.name == 'h4':
            data['subtitle'] = text
        elif child.name == 'p':
            data['paragraphs'].append(text)

    return data
