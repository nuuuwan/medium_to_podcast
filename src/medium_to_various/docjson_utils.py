from utils import jsonx


def docjson_merge(docjson_files, merged_docjson_file):
    all_docjson = []
    for docjson_file in docjson_files:
        docjson = jsonx.read(docjson_file)
        all_docjson += docjson

    jsonx.write(merged_docjson_file, all_docjson)
    print(f'Wrote {merged_docjson_file}')
