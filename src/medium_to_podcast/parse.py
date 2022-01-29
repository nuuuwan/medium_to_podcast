"""Parse Medium Posts as HTML."""
import os
import math

from bs4 import BeautifulSoup
from utils import filex

DIR_MEDIUM = '/Users/nuwan.senaratna/Not.Dropbox/_CODING/data/medium'
DIR_MEDIUM_POSTS = os.path.join(DIR_MEDIUM, 'posts')
DIR_MEDIUM_POSTS_MD = os.path.join(DIR_MEDIUM, 'posts-md')
ARTICLES_PER_BOOK = 50

CLASS_NAME_CONTENT = 'section-inner sectionLayout--insetColumn'
UNICODE_REPLACES = [
    ['\u2019', '\''],
    ['\u201c', '"'],
    ['\u201d', '"'],
    ['\u2026', '...'],
]

def get_html_files():
    html_files = []
    for file in os.listdir(DIR_MEDIUM_POSTS):
        if file[-5:] == '.html':
            html_files.append(file)
    html_files = sorted(html_files)
    return html_files



def _clean(str):
    str = str.strip()
    for [before, after] in UNICODE_REPLACES:
        str = str.replace(before, after)
    return str




def html_to_md(html_file_only, i):
    """Parse."""
    html_file = os.path.join(DIR_MEDIUM_POSTS, html_file_only)
    html = filex.read(html_file)
    soup = BeautifulSoup(html, 'html.parser')

    lines = []

    content = soup.find('div', class_=CLASS_NAME_CONTENT)
    first_title = True
    for child in content.find_all():
        text = _clean(child.text)
        if child.name == 'h3':
            if first_title:
                lines.append(f'# {text}')
                first_title = False
            else:
                lines.append(f'## {text}')
        elif child.name == 'h4':
            lines.append(f'### {text}')
        elif child.name == 'p':
            lines.append(f'{text}')
        elif child.name == 'blockquote':
            lines.append(f'>>> {text}')
        elif child.name == 'li':
            lines.append(f'* {text}')
        elif child.name == 'pre':
            lines.append(f'```\n{text}\n```')
        elif child.name == 'img':
            src = child['src']
            lines.append(f'![Image]({src})')

    child = soup.find('time')
    if child:
        text = _clean(child.text)
        i1 = i + 1
        lines = [f'#### Article {i1} · {text}'] + lines

        content = '\n\n'.join(lines)
        md_file = os.path.join(DIR_MEDIUM_POSTS_MD, html_file_only[:-5] + '.md')
        filex.write(md_file, content)
        print(f'Saved {md_file}')

        return lines
    return []

def htmls_to_md(html_files):
    n_articles = len(html_files)
    n_books = math.ceil(n_articles / ARTICLES_PER_BOOK)

    for i_book in range(0, n_books):
        all_lines = []
        i_book1 = i_book  + 1

        all_lines.append(f'# Book {i_book1}')
        min_i_article = i_book * ARTICLES_PER_BOOK + 1
        max_i_article = min((i_book + 1) * ARTICLES_PER_BOOK, n_articles)
        all_lines.append(f'#### Articles {min_i_article} to {max_i_article}')

        for i in range(0,ARTICLES_PER_BOOK):
            i_article = i_book * ARTICLES_PER_BOOK + i
            if i_article >= n_articles:
                break
            all_lines += html_to_md(html_files[i_article], i_article)

        content = '\n\n'.join(all_lines)
        md_file = os.path.join(DIR_MEDIUM_POSTS_MD, f'nuwans-medium-book-{min_i_article:03}-{max_i_article:03}.md')
        filex.write(md_file, content)
        print(f'Saved {md_file}')




if __name__ == '__main__':
    html_files = get_html_files()
    htmls_to_md(html_files)
