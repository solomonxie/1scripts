# coding:utf-8


import os
from bs4 import BeautifulSoup

def main():
    folder = '/Volumes/SD/Downloads/New/One-to-One-Conversations-backup/htm'

    #import pdb;pdb.set_trace()
    for root, subdir, files in os.walk(folder):
        for filename in files:
            print(filename)
            if os.path.splitext(filename)[1] != '.htm':
                continue
            path = os.path.join(root, filename)
            with open(path, 'r+') as f:
                html = f.read()

            soup = BeautifulSoup(html, 'html5lib')

            title = soup.find('title')
            title.string = os.path.splitext(filename)[0]
            print(title.string)

            with open(path, 'w') as f:
                f.write(soup.prettify())
        


if __name__ == "__main__":
    main()
