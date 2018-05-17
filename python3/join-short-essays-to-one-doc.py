# coding:utf-8
'''
# ==== This project should be running in a python3 enviroment, preferred in Virtualenv. ====
#
# Author: Solomon Xie
# Email: solomonxiewise@gmail.com
# Project: Join Short Essays to One Document
# Description: Join tons of short essays I wrote long ago to one document
'''

import os
import sys
import time
import re

def main():
    """
    I'm just gonna finish everything in this func
    """
    path = '/Volumes/SD/Downloads/text/'

    ## Walk through the folder
    for root, subdir, files in os.walk(path, topdown=True):
        for name in files:
            print(name)


if __name__ == "__main__":
    main()
