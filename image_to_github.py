#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This if for convenience of writing markdown notes:
Send screenshots to github and get the raw url, 
then paste in markdown file as a permanent image link.
"""

import os
import sys
import base64
import requests

def main():
    """

    """

    # Convert a image file to base64 string
    if sys.argv[1] is False and os.path.exists(sys.argv[1]) is False:
        print 'No image path found.'
        return

    path = sys.argv[1]

    with open(path, 'rb') as f:
        pic = f.read()

    bs64 = base64.b64encode(pic)

    # upload image data to github
    filename = os.path.basename(path)
    url = 'https://api.github.com/repos/solomonxie/user_content_media/contents/images/'+filename
    headers = {'authorization': 'token 4f3659f0d896c1f80204548db238bb45b6b806a4'}
    payload = '{"message": "auto uploaded by python", "content": "%s"}' % bs64
    r = requests.request("PUT", url, data=payload, headers=headers)

    print r.status_code
    print r.content
    




if __name__ == "__main__":
    main()
