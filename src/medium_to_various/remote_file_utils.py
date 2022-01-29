import os

from PIL import Image
from utils import hashx, www

DIR_REMOTE_FILES = '/Users/nuwan.senaratna/Not.Dropbox/_CODING/remote_files'


def _convert_if_needed(local_file):
    file_without_ext, ext = os.path.splitext(local_file)
    if ext in ['.jpeg', '.jpg']:
        new_local_file = f'{file_without_ext}.png'
        if not os.path.exists(new_local_file):
            img = Image.open(local_file)
            img.save(new_local_file)
            print(f'Converted {local_file} -> {new_local_file}')
        return new_local_file
    return local_file


def _get_local_file_only(url):
    h = hashx.md5(url)
    ext = url.split('.')[-1]
    if len(ext) > 5:
        ext = 'png'
    local_file = os.path.join(DIR_REMOTE_FILES, f'{h}.{ext}')
    return local_file


def _download_if_not_exists(local_file, url):
    if not os.path.exists(local_file):
        www.download_binary(url, local_file)
        print(f'Downloaded "{url}" -> "{local_file}"')


def get_local_file(url):
    print(url)
    local_file = _get_local_file_only(url)
    _download_if_not_exists(local_file, url)
    local_file = _convert_if_needed(local_file)
    return local_file


if __name__ == '__main__':
    urls = [
        os.path.join(
            'https://cdn-images-1.medium.com',
            'max/800/1*pWm5OyLUt8QLXO0T6XBGWA.jpeg',
        ),
        os.path.join(
            'https://cdn-images-1.medium.com',
            'max/800/1*bxuYPpmd284j1zIYxgiMtQ.png',
        ),
    ]
    for url in urls:
        print(get_local_file(url))
