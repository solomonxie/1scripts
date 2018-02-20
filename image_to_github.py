#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This if for convenience of writing markdown notes:
Send screenshots to github and get the raw url, 
then paste in markdown file as a permanent image link.
"""

import os
import sys
import json
import base64
import requests

def main():
    """

    """
    print 'Start...'

    # Convert a image file to base64 string
    if sys.argv[1] is False and os.path.exists(sys.argv[1]) is False:
        print 'No image path found.'
        return

    path = sys.argv[1]

    print 'Loading local image file [%s]...' % path

    with open(path, 'rb') as f:
        pic = f.read()

    bs64 = base64.b64encode(pic)

    print 'Encoded an image into a base64 string. [%d]' % len(bs64)

    # upload image data to github
    filename = os.path.basename(path)
    url = 'https://api.github.com/repos/solomonxie/user_content_media/contents/images/'+filename
    headers = {'authorization': 'token b1ff0434283fb0610392b7071aad02d3736903fb'}
    payload = '{"message": "auto uploaded by python", "content": "%s"}' % bs64

    print 'Uploading an image onto Github repository...'
    r = requests.request("PUT", url, data=payload, headers=headers, timeout=10)

    print 'Response Code: %d' % r.status_code
    print 'Response body:\n%s' % r.content

    if r.status_code is not 201:
        print 'Requesting of uploading failed...'
        return

    
    # get the raw url of this file
    info = r.json()
    raw = info['content']['download_url']

    print 'Uploaded.\nNow copy image url[%s] to clipboard...' % raw

    os.system('echo "![Image](%s)" | pbcopy' % raw)





if __name__ == "__main__":
    main()
