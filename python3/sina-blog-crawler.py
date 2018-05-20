# ==== This project should be running in a python3 enviroment, preferred in Virtualenv. ====
#
# Author: Solomon Xie
# Email: solomonxiewise@gmail.com
# Project: Sina Blog Crawler
# Description: scrap my sina blogs and backup
#

import requests
import re
from bs4 import BeautifulSoup

def main():
    return



def fetch_blog_list(page=0):
    """
    Fetch blog list page by page
    """
    url = 'http://blog.sina.com.cn/s/articlelist_1253924794_0_1.html'

    headers = {}

    r = requests.get(url, headers=headers)

    if r.status_code is not 200:
        print('Server dinied. Status:[%s].'%r.status_code)
        return

    html = r.text
    soup = BeautifulSoup(html, 'html5lib')



if __name__ == "__main__":
    main()
