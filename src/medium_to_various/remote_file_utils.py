import os

from utils import hashx, www

DIR_REMOTE_FILES = '/Users/nuwan.senaratna/Not.Dropbox/_CODING/remote_files'


def _get_local_file_only(url):
    h = hashx.md5(url)
    ext = url.split('.')[-1]
    local_file = os.path.join(DIR_REMOTE_FILES, f'{h}.{ext}')
    return local_file


def _download_if_not_exists(local_file, url):
    if not os.path.exists(local_file):
        www.download_binary(url, local_file)
        print(f'Downloaded "{url}" -> "{local_file}"')


def get_local_file(url):
    local_file = _get_local_file_only(url)
    _download_if_not_exists(local_file, url)
    return local_file


if __name__ == '__main__':
    url = (
        'https://cdn-images-1.medium.com/max/800/1*bxuYPpmd284j1zIYxgiMtQ.png'
    )
    print(get_local_file(url))
