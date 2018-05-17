# coding:utf-8
'''
# ==== This project should be running in a python3 enviroment, preferred in Virtualenv. ====
#
# Author: Solomon Xie
# Email: solomonxiewise@gmail.com
# Project: Join Short Essays to One Document
# Description: Join tons of short essays I wrote long ago to one document
'''

from os import path
from os import walk
import sys
import time
import re

def main():
    """
    I'm just gonna finish everything in this func
    """
    base_folder = '/Volumes/SD/Downloads/text'
    archive_folder = '/Volumes/SD/Downloads/text-archive'

    ## Walk through the folder
    for root, subdir, files in walk(base_folder, topdown=True):
        if len(files) < 1: continue

        joint_name = path.basename(path.realpath(root)) + '.md'
        joint_path = path.join(archive_folder, joint_name)

        for name in files:
            txt_path = path.join(root, name)
            txt = smart_reading(txt_path)
            content = '# '+ name +'\n'+ txt + '\n\n'
            with open(joint_path, 'a') as f_out:
                f_out.write(content)



def smart_reading(path):
    """
    Try different encodings
    """
    charsets = ['utf-8', 'gbk','UTF-16LE']

    for enc in charsets:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            print('Failed loading with encoding [%s] for %s.'%(enc, path))
            continue

    return 'n/a'


if __name__ == "__main__":
    main()
