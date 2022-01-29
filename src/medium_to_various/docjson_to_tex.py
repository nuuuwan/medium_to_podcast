from utils import filex


def docjson_to_text(docjson_file, tex_file):
    tex_content = '''
\\documentclass{article}

\\begin{document}
First document. This is a simple example, with no
extra parameters or packages included.
\\end{document}
    '''
    filex.write(tex_file, tex_content)
    print(f'Wrote {tex_file}')


if __name__ == '__main__':
    docjson_file = None
    tex_file = '/tmp/medium-merged.tex'
    docjson_to_text(docjson_file, tex_file)
