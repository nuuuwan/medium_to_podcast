import os

from medium_to_various.docjson_to_docx import docjson_to_docx
from medium_to_various.docjson_to_md import docjson_to_md
from medium_to_various.docjson_utils import docjson_merge
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

    random.shuffle(html_files)
    SAMPLE_SIZE = 10
    sample_html_files = html_files[:SAMPLE_SIZE]
    # sample_html_files = list(
    #     map(
    #         lambda file_only: os.path.join(DIR_MEDIUM_POSTS, file_only),
    #         [
    #             '2021-07-13_'
    #             + 'Drawing-Dorling-Cartograms-of-Sri-Lanka-a22a8886d057.html'
    #         ],
    #     )
    # )

    docjson_files = []
    for i, html_file in enumerate(sample_html_files):
        file_base = f'/tmp/medium-{i}'
        docjson_file = f'{file_base}.doc.json'
        medium_html_to_docjson(html_file, docjson_file)
        docjson_files.append(docjson_file)

    merged_docjson_file = '/tmp/medium-merged.doc.json'
    docjson_merge(docjson_files, merged_docjson_file)

    merged_md_file = '/tmp/medium-merged.md'
    docjson_to_md(merged_docjson_file, merged_md_file)

    merged_docx_file = '/tmp/medium-merged.docx'
    docjson_to_docx(merged_docjson_file, merged_docx_file)
