from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches, Pt, RGBColor
from utils import jsonx

from medium_to_various.remote_file_utils import get_local_file

DEFAULT_IMAGE_WIDTH = 3
DEFAULT_FONT_NAME = 'Georgia'
ALIGN_CENTER = 1


def _build_styles(document):
    style = document.styles['Normal']
    style.font.size = Pt(10)
    style.font.name = DEFAULT_FONT_NAME

    style = document.styles['Quote']
    style.font.color.rgb = RGBColor(128, 0, 0)
    style.font.name = DEFAULT_FONT_NAME
    style.paragraph_format.left_indent = Inches(0.5)

    style = document.styles.add_style('New Heading 0', WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(20)
    style.font.name = DEFAULT_FONT_NAME
    style.paragraph_format.alignment = ALIGN_CENTER

    style = document.styles.add_style('New Heading 1', WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(15)
    style.font.name = DEFAULT_FONT_NAME
    style.paragraph_format.alignment = ALIGN_CENTER

    style = document.styles.add_style('New Heading 2', WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(12)
    style.font.name = DEFAULT_FONT_NAME
    style.paragraph_format.alignment = ALIGN_CENTER

    style = document.styles.add_style('New Heading 3', WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(10)
    style.font.name = DEFAULT_FONT_NAME
    style.paragraph_format.alignment = ALIGN_CENTER


def docjson_to_docx(docjson_file, docx_file):
    docjson = jsonx.read(docjson_file)
    document = Document()
    _build_styles(document)
    for d in docjson:
        tag, text = d['tag'], d.get('text')
        if tag == 'title':
            document.add_paragraph(text, style='New Heading 0')
        elif tag == 'h1':
            document.add_paragraph(text, style='New Heading 1')
        elif tag == 'h2':
            document.add_paragraph(text, style='New Heading 2')
        elif tag == 'h3':
            document.add_paragraph(text, style='New Heading 3')

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
