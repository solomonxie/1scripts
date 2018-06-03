# -*- coding: utf-8 -*-
# Python3

"""
File: backup-markdown-blog-images.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: Search all images linked in github issues or comments, download to local folder for backing up
"""

import os
import re


def main():
    filename = './dataset/img_url_matching.md'
    urls = match_img_urls(filename)
    print(urls)

    # export urls to a .txt file for downloading
    with open('/tmp/urls.txt', 'w') as f:
        f.write('\n'.join(urls))

    # Download all images from the url list
    os.system('wget --random-wait -nc --limit-rate 300k -i /tmp/urls.txt -P dataset/imgs')


def match_img_urls(filename=None):
    """
    :desc: Docstring for match_img_urls.
    :returns: [] list. a list of url strings
    :matching: ![image](https://user-images.githubusercontent.com/14041622/40187586-70e7343c-5a2a-11e8-83ab-e36804921b73.png)
    :cmd: $ wget --random-wait -nc --limit-rate 300k -i List.txt ./folder/
    """
    if os.path.exists(filename) is False:
        return []

    with open(filename, 'r') as f:
        content = f.read()

    # RegExp for matching image urls
    pattern = re.compile(r'\!\[.+\]\((.+)\)')
    urls = pattern.findall(content)

    return urls


if __name__ == "__main__":
    main()
