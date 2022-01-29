from docx import Document
from utils import jsonx


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
            p = document.add_paragraph(text)
            p.add_run('italic.').italic = True
        elif tag == 'blockquote':
            document.add_paragraph(text, style='Intense Quote')

        elif tag == 'li':
            document.add_paragraph(text, style='List Bullet')
        elif tag == 'pre':
            document.add_paragraph(text)
        elif tag == 'img':
            d['src']
            # document.add_picture(src)

        elif tag == 'time':
            text_time = f'Colombo, {text}'
            p = document.add_paragraph(text_time)
            p.add_run('italic.').italic = True

    document.save(docx_file)
    print(f'Wrote {docx_file}')
