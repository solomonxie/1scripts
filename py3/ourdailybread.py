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
    - [ ] Scrap odb.org and download today's content
    - [ ] Scrap the bible verses cited in the content from Biblegateway.com
    - [ ] Organize contents to form a Markdown file
    - [ ] Save file and store at a folder for `crontab`
"""

import requests
import re
from bs4 import BeautifulSoup

def main():
    url = 'https://odb.org'
    r = requests.get(url)
    print(r.content)
    

if __name__ == "__main__":
    main()
