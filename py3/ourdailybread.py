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

import json
import requests
from bs4 import BeautifulSoup

def main():
    odb = OurDailyBread()
    odb.save('./dataset/odb.md')
    odb.sendmail('/Volumes/SD/Workspace/etc/email.json', ['solomonxie@outlook.com'])
    

class OurDailyBread:
    """
    A class for an article from today's odb.org content.  
    """

    def __init__(self):
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
        self.markdown = ''
        self.html = ''

        self.fetch()

    def fetch(self):
        """TODO: fetch contents from odb.org
        :returns: Nothing. But composes markdown value of this instance.
        """
        print('Fetching Our daily bread...')
        #r = requests.get(self.url)
        #soup = BeautifulSoup(r.content, 'html5lib')
        print('OK.')

        with open('./dataset/odb.org.html', 'r') as f:
            soup = BeautifulSoup(f.read(), 'html5lib')

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
        
        # convert markdown to html format
        #self.html = ''
        with open('./dataset/out.html', 'r') as f:
            self.html = f.read()

        
    def fetch_bible(self, tag):
        """TODO: Fetch scriptures from Biblegateway.com
        :tag: ElementTag instance of BeautifulSoup, as the target tag includes scriptures
        :type: returns string
        :returns: Scripture content
        """

        links = tag.find_all('a')
        content = 'Read: [%s](%s) | Bible in a Year: [%s](%s)'\
                %(links[0].get_text(), links[0]['href'], links[1].get_text(), links[1]['href'])

        #bible = BibleGateway(links[0]['href'])

        return content


    def save(self, path):
        """TODO: Docstring for save.
        :returns: TODO
        """
        with open(path, 'w') as f:
            f.write(self.markdown)
        print('Saved markdown file.')

    
    def sendmail(self, path, recipients):
        """TODO: Docstring for sendmail.
        :path: String, A local JSON file including mail server info 
        :recipients: List, email recipients list
        :returns: None.
        """
        # create email instance
        mail = Email(path)
        # make Email body
        subject = self.title
        content = self.html
        # send mail
        mail.send(subject, content, recipients)



import smtplib
from email.mime.text import MIMEText
class Email:

    """Docstring for Email. """

    def __init__(self, path):
        with open(path, 'r') as f:
            self.cfg = json.loads(f.read())
        self.server = self.cfg['senders'][1]

    def send(self, subject, content, recipients):

        """TODO: Docstring for send.
        :subject: String, title for email
        :content: String, HTML formated content
        :recipients: List, email addresses.
        :returns: None.
        """
        # Settings of sender's server
        host = self.server['host']
        sender = self.server['email']
        user = self.server['user']
        password = self.server['password']
        to = recipient[0]

        # Login the sender's server
        print('Logging with server...')
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(host, 25)
        smtpObj.login(user, password)
        print('Login successful.')

        # Content of email
        #subject = 'Python send html email test55'
        with open('./dataset/out.html', 'r') as f:
            content = f.read()
        
        # Settings of the email string
        email = MIMEText(content,'html','utf-8')
        email['Subject'] = subject
        email['From'] = sender
        email['To'] = to
        msg = email.as_string()
        print('Sending email: [%s] from [%s] to [%s]'%(subject, self.sendfrom, to))
        
        # Send email
        smtpObj.sendmail(sender, to, msg) 
        smtpObj.quit() 
        print('OK.')


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



if __name__ == "__main__":
    main()
