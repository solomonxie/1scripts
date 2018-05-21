# ---coding:utf-8---

# ==== This project should be running in a python3 enviroment, preferred in Virtualenv. ====
#
# Author: Solomon Xie
# Email: solomonxiewise@gmail.com
# Project: Blog archive data cleaner
# Description: Extract blog & tweeter data from multiple type of data structures in different files
#

import re
import os
import time
from bs4 import BeautifulSoup

def main():
    diandian_blog_xml('/Volumes/SD/Downloads/Text-extract/diandian-1.xml')
    diandian_blog_xml('/Volumes/SD/Downloads/Text-extract/diandian-2.xml')

def diandian_blog_xml(src):
    folder = '/Volumes/SD/Downloads/blog-archives/diandian/'
    with open(src, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    posts = soup.select('posts > post')

    print('%d posts have found.'%len(posts))

    for p in posts:
        tm = int(p.createtime.get_text())/1000
        ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tm))
        if p.title is not None:
            title = p.title.get_text() or ctime
        else:
            title = ctime
        tag = p.find('text') or p.find('desc')
        text = tag.get_text()

        soup = BeautifulSoup(text, 'html5lib')
        tags = soup.find_all('p')
        text_filtered = '\n'.join([t.get_text() for t in tags])
        #print(text_filtered)

        content = '# %s \n@ %s \n%s' %(title, ctime, text_filtered)
        print(title, ctime)
        with open(folder+'%s.MD'%title, 'w') as f:
            f.write(content)

    return

def renren_tweets():
    return

def qzone_tweets():
    return

def sina_weibo_2011():
    return


def sina_weibo_2012():
    return

def sina_weibo_2013():
    return

def memes_2008():
    return

def memes_2011():
    return

if __name__ == "__main__":
    main()
