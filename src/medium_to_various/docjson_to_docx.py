from docx import Document
from docx.shared import Inches
from utils import jsonx

from medium_to_various.remote_file_utils import get_local_file

DEFAULT_IMAGE_WIDTH = 4


def docjson_to_docx(docjson_file, docx_file):
    docjson = jsonx.read(docjson_file)
    document = Document()
    for d in docjson:
        tag, text = d['tag'], d.get('text')
        if tag == 'h1':
            document.add_page_break()
            document.add_heading(text, level=1)
        elif tag == 'h2':
            document.add_heading(text, level=2)
        elif tag == 'h3':
            document.add_heading(text, level=3)
        elif tag == 'h4':
            document.add_heading(text, level=4)
        elif tag == 'p':
            document.add_paragraph(text)
        elif tag == 'em':
            p = document.add_paragraph()
            p.add_run(text).italic = True
        elif tag == 'figcaption':
            document.add_paragraph(text, style='Caption')
        elif tag == 'blockquote':
            document.add_paragraph(text, style='Quote')

        elif tag == 'li':
            document.add_paragraph(text, style='List Bullet')
        elif tag == 'pre':
            document.add_paragraph(text)
        elif tag == 'img':
            url = d['src']
            local_file = get_local_file(url)
            document.add_picture(local_file, width=Inches(DEFAULT_IMAGE_WIDTH))

        elif tag == 'time':
            f'Colombo, {text}'
            p = document.add_paragraph()
            p.add_run(text).italic = True

    document.save(docx_file)
    print(f'Wrote {docx_file}')
