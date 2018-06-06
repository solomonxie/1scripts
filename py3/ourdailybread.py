# -*- coding: utf-8 -*-

"""
File: ourdailybread.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    A simple script to scrap Our Daily Bread article of today,
    and would be used to send email to myself.
Workflow:
    - [x] Scrap odb.org and download today's content
    - [ ] Scrap the bible verses cited in the content from Biblegateway.com
    - [x] Organize contents to form a Markdown file
    - [ ] Save file and store at a folder for `crontab`
"""

import requests
from bs4 import BeautifulSoup

def main():
    md = './dataset/odb.org.html'
    odb = OurDailyBread(md)
    #print(odb.markdown)

    with open(md, 'w') as f:
        f.write(odb.markdown)
    

class OurDailyBread:
    """
    A class for an article from today's odb.org content.  
    """

    def __init__(self, path):
        """TODO: to be defined1. """
        self.url = 'https://odb.org'
        self.path = ''
        self.title = ''
        self.date = ''
        self.thumbnail = ''
        self.scripture = ''
        self.scripture_link = ''
        self.readbible = ''
        self.bible_link = ''
        self.verses = ''
        self.devotion = ''
        self.poem = ''
        self.thought = ''
        self.insight = ''

        self.fetch(path)

    def fetch(self, path):
        """TODO: fetch contents from odb.org
        :path: Devotion page of odb.org
        :returns: Nothing. But composes markdown value of this instance.
        """
        with open(path, 'r') as f:
            soup = BeautifulSoup(f.read(), 'html5lib')
        #r = requests.get(url)
        #soup = BeautifulSoup(r.content)

        # Parse contents
        self.title = soup.find('h2', attrs={'class': 'entry-title'}).get_text()
        self.date = soup.find('a', attrs={'class': 'calendar-toggle'}).get_text()
        self.thumbnail = soup.find('img', attrs={'class': 'post-thumbnail'})['src']
        self.verses = soup.find('div', attrs={'class': 'verse-box'}).get_text()
        self.devotion = soup.find('div', attrs={'class': 'post-content'}).get_text().strip()
        self.poem = soup.find('div', attrs={'class': 'poem-box'}).get_text().strip()
        self.thought = soup.find('div', attrs={'class': 'thought-box'}).get_text().strip()
        self.insight = soup.find('div', attrs={'class': 'insight-box'}).p.get_text().strip()
        self.scripture = self.fetch_bible(soup.find('div', attrs={'class': 'passage-box'}))

        body = '# %s (Our daily bread)\n**%s**\n> Verses: %s\n![thumbnail](%s)\n'\
                +'## Content\n%s\n%s\n%s\n## Scripture\n%s\n## INSIGHT\n> %s'
        self.markdown = body % (self.title, self.date,self.verses,self.thumbnail, \
            self.devotion, self.poem, self.thought, self.scripture, self.insight)

        
    def fetch_bible(self, tag):
        """TODO: Fetch scriptures from Biblegateway.com
        :tag: ElementTag instance of BeautifulSoup, as the target tag includes scriptures
        :type: returns string
        :returns: Scripture content
        """

        links = tag.find_all('a')
        content = 'Read: [%s](%s) | Bible in a Year: [%s](%s)'\
                %(links[0].get_text(), links[0]['href'], links[1].get_text(), links[1]['href'])

        return content

        
if __name__ == "__main__":
    main()
