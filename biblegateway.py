#Python3
# -*- coding: utf-8 -*-

"""
File: biblegateway.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    Scrap bible scriptures from searching-result page on Bibilegateway.com
"""


import requests
from bs4 import BeautifulSoup


class BibleGateway:

    """Docstring for BibleGateway:. """

    def __init__(self, url):
        self.url = url 
        self.quotes = []

        self.fetch()

    def fetch(self):
        """TODO: Docstring for fetch.
        :returns: TODO
        """
        with open('./dataset/biblegateway.html', 'r') as f:
            soup = BeautifulSoup(f.read(), 'html5lib')

        for tag in soup.select('div[class*=result-text-style-normal]'):
            # Bolding all Chapter numbers
            for c in tag.select('span[class=chapternum]'):
                num = c.string
                c.string = '**%s**' %(num.strip())
            # Change all Verse numbers to superscript
            for v in tag.find_all('sup', attrs={'class': 'versenum'}):
                num = v.get_text()
                v.string = self.superscript(num.strip())

            print(tag.get_text())


    def superscript(self, content):
        """TODO: Change all verse numbers to Superscripts
        :content: String.
        :returns: String. A superscript number 
        """
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        supers = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

        for n in numbers:
            content = content.replace(n, supers[int(n)])

        return content

