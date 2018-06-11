#Python2
# coding:utf-8

import os
import time
import requests
from urlparse import urlparse
from bs4 import BeautifulSoup

def main():
    book = Book('http://khnovel.com/243262-the-complete-robot.html')
    #print book.book_url
    book.fetch()

class Book:
    def __init__(self, url):
        self.book_url = url
        self.title = ''
        self.info = ''
        self.intro = ''
        link = urlparse(url)
        self.host = link.scheme + '://' + link.netloc

    def fetch(self):
        print self.book_url

        r = requests.get(self.book_url, timeout=5)
        html = r.content

        # get book's basic info
        soup = BeautifulSoup(html, 'html5lib')
        tag = soup.find('div', attrs={'class':'detail-top'})
        self.title = tag.h2.get_text().encode('utf-8')
        self.info = '\n'.join([p.get_text() for p in tag.find_all('p')]).encode('utf-8')
        self.intro = soup.find('div', attrs={'class':'detail-desc'}).get_text().encode('utf-8')

        # for markdown file
        file_name = './test/'+ self.title +'.md'
        file_content = '# '+ self.title +'\n'+ self.info +'\n'+ self.intro +'\n\n'

        # get chatper links
        results = soup.select('#ztitle > li > a')
        for item in results:
            chap = Chapter(self.host+item['href'])
            file_content += '## ' + chap.title + '\n' + chap.content + '\n\n'
            time.sleep(1)

        # to markdown file
        with open(file_name, 'w') as f:
            f.write(file_content)


class Chapter:
    def __init__(self,url):
        self.chapter_url = url
        self.title = ''
        self.content = ''
        self.next_url = ''
        
        # initiate fetching online
        self.fetch()

    def fetch(self):
        print self.chapter_url
        
        r = requests.get(self.chapter_url, timeout=5)
        html = r.content

        soup = BeautifulSoup(html, 'html5lib')
        self.title = soup.find('div', attrs={'id':'play-wrap'}).h3.get_text().encode('utf-8')
        self.content = soup.find('div', attrs={'class':'contents-comic'}).p.get_text().encode('utf-8')



if __name__ == "__main__":
    main()
