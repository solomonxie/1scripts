#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MAC ONLY.
This if for convenience of writing markdown notes:
Send screenshots to github and get the raw url, 
then paste in markdown file as a permanent image link.

REQUIREMENT:
    pip install pyobjc
"""

import os
import sys
import json
import base64
import requests

# PyObjc library > Appkit > NSPasteboard (main class for clipboard) and PNG/TIFF file type classes
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypeString


def main():
    """

    """
    print 'Start...'

    import pdb;pdb.set_trace()

    path = get_pasteboard_img()
    bs64 = img_to_bs64(path)
    url  = upload_to_github(path, bs64)

    print 'Uploaded.\nNow copy image url[%s] to clipboard...' % url

    os.system('echo "![Image](%s)" | pbcopy' % url)


def upload_to_github(path, fcontent):
    token = raw_input('Please tell me your authentication token string:')
    filename = os.path.basename(path)

    # upload image data to github
    api = 'https://api.github.com/repos/solomonxie/user_content_media/contents/images/%s' % filename
    headers = {'authorization': 'token %s' % token}
    payload = '{"message": "auto uploaded by python", "content": "%s"}' % fcontent

    print 'Uploading an image onto Github repository...'
    r = requests.request("PUT", url=api, data=payload, headers=headers, timeout=10)

    print 'Response Code: %d' % r.status_code
    print 'Response body:\n%s' % r.content

    if r.status_code is not 201:
        print 'Requesting of uploading failed...'
        return

    # get the raw url of this file
    info = r.json()

    return info['content']['download_url']



def img_to_bs64(path):
    with open(path, 'rb') as f:
        encoded = base64.b64encode(f.read())

    print 'Encoded an image into a base64 string. [%d]' % len(encoded)
    return encoded


def get_pasteboard_img():
    """
    Get image from pasteboard/clipboard and save to file 
    """
    pb = NSPasteboard.generalPasteboard()  # Get data object from clipboard 
    data_type = pb.types()                 # Get type of the data

    # Recognize data type for furher processing 
    if NSPasteboardTypePNG in data_type:         # PNG:
        # Get data content by data type
        data = pb.dataForType_(NSPasteboardTypePNG)
        filename = 'HELLO_PNG.png'
    elif NSPasteboardTypeTIFF in data_type:      # TIFF: most probablly it's tiff
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        filename = 'HELLO_TIFF.tiff'
    elif NSPasteboardTypeString in data_type:    # Text: if it's already a filepath then just return it
        data = str(pb.dataForType_(NSPasteboardTypeString))
        return data if os.path.exists(data) else None
    else: 
        return None

    # Write data to a local file
    filepath = '/Volumes/SD/Downloads/%s' % filename
    success = data.writeToFile_atomically_(filepath, False)

    return filepath if success else None

    ## Process with different types of data 
    #if NSPasteboardTypePNG in data_type:          # PNG file
    #    data = pb.dataForType_(NSPasteboardTypePNG)
    #    filename = 'HELLO_PNG.png'
    #    filepath = '/tmp/%s' % filename
    #    ret = data.writeToFile_atomically_(filepath, False)
    #    if ret: 
    #        return filepath
    #elif NSPasteboardTypeTIFF in data_type:         #TIFF: most probablly it's tiff
    #    data = pb.dataForType_(NSPasteboardTypeTIFF)
    #    filename = 'HELLO_TIFF.tiff'
    #    filepath = '/tmp/%s' % filename
    #    ret = data.writeToFile_atomically_(filepath, False)
    #    if ret:
    #        return filepath
    #elif NSPasteboardTypeString in data_type:
    #    # string todo, recognise url of png & jpg
    #    pass


if __name__ == "__main__":
    main()
