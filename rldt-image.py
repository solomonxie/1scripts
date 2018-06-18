#Python3
# -*- coding: utf-8 -*-

"""
File: imgstore.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    This is a script for orginizing images from the RLDT system.
TODO:
    - [ ] Read CSV file and Match, rename to jpg file.
    - [ ] Create folders according to the PID.
    - [ ] Create a JSON file for each folder includes the info of PID, NAME, PictureName
"""


import os
import json


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    csv = '/Volumes/SD/Workspace/RLDT/data/img-list.csv'
    srcfolder = '/Volumes/SD/Workspace/RLDT/data/RAW'
    newfolder = '/Volumes/SD/Workspace/RLDT/data/RAW2'

    f = open(csv, 'r')
    for i, line in enumerate(f):
        if i == 0: continue
        #if i == 3: break
        img = RLDTImage(line)
        img.move(srcfolder, newfolder)
        with open(newfolder+'/'+ img.pid +'/info.json', 'w') as f:
            f.write('{"imgid":"%s", "pid":"%s", "pname":"%s", "filename":"%s"}' % (\
                    img.imgid, img.pid, img.pname, img.imgname))
            print('Created info file.')
    f.close()




class RLDTImage:

    """Docstring for RLDTImage. """

    def __init__(self, data):
        """TODO: to be defined1. """
        self.data = data
        self.imgid = ''
        self.imgname = ''
        self.pid = ''
        self.pname = ''
        self.filename = ''
        self.src = ''
        self.target = ''
        self.newfolder = ''

        self.readinfo()

    def readinfo(self):
        """TODO: Docstring for distribute.
        :data: String, one line of image information: [ID PID PName PictureName FileType]
        :returns: TODO
        """
        info = self.data.split(',')
        #print(info)

        self.imgid = info[0]
        self.imgname = info[3] +'.'+ info[4].strip()
        self.pid = info[1]
        self.pname = info[2]
        self.filename = info[0] +'.'+ info[4].strip()

        #print(self.filename)

    def move(self, srcfolder, newfolder):
        """TODO: Docstring for move.
        :srcfolder: String, the source folder stores all images
        :newfolder: String, the new folder path where the image gonna store
        :returns: TODO
        """
        print('Now start to move the image [%s] for [%s]' %(self.filename, self.pname))

        self.src = srcfolder +'/'+ self.imgid
        self.newfolder = newfolder +'/'+ self.pid
        self.target = self.newfolder +'/'+ self.filename
        # find the file
        if os.path.exists(self.src) is False:
            print('The file %s does not exists.' % self.src)
            return
        # create folder
        with os.popen('mkdir -p %s' % self.newfolder) as p:
            print(p.read())
            print('Created folder %s' % self.newfolder)

        # move or copy file to the new folder
        with os.popen('cp %s %s' % (self.src, self.target)) as p:
            print(p.read())
            print('OK.\nLocated at: %s' % self.target)


        



if __name__ == "__main__":
    main()
