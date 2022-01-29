import os

from medium_to_various.docjson_to_md import docjson_to_md
from medium_to_various.medium_html_to_docjson import medium_html_to_docjson

DIR_MEDIUM = '/Users/nuwan.senaratna/Not.Dropbox/_CODING/data/medium'
DIR_MEDIUM_POSTS = os.path.join(DIR_MEDIUM, 'posts')
DIR_MEDIUM_POSTS_MD = os.path.join(DIR_MEDIUM, 'posts-md')


def get_html_files():
    html_files = []
    for file_only in os.listdir(DIR_MEDIUM_POSTS):
        if file_only[-5:] == '.html':
            file = os.path.join(DIR_MEDIUM_POSTS, file_only)
            html_files.append(file)
    html_files = sorted(html_files)
    return html_files


if __name__ == '__main__':
    html_files = get_html_files()
    n_html_files = len(html_files)
    print(f'Found {n_html_files} html files')

    import random

    html_file = random.choice(html_files)
    print(f'Random html file: "{html_file}"')

    docjson_file = '/tmp/medium.doc.json'
    medium_html_to_docjson(html_file, docjson_file)

    md_file = '/tmp/medium.md'
    docjson_to_md(docjson_file, md_file)
