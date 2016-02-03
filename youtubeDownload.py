# coding:utf-8
import os, sys, re, getopt
import requests # 第三方模块
# os.popen('start chrome http://en.savefrom.net/#url=https:/www.youtube.com/watch?v=b5NmtmNwMgU')

def main():
    opts, args = getopt.getopt(sys.argv[1:], 'v:l:', ['video=','list='])
    vUrl = ''
    playlist = ''
    for o,a in opts:
        if   o == '-v' or o == '--video': vUrl = a
        elif o == '-l' or o == '--list': playlist = a
    # 测试用
    # vUrl = 'https://www.youtube.com/watch?v=HMqgVXSvwGo&index=1&list=PLNCVk_zarBEsIqlQBcYVIpuBlyY2hy0Z0'
    # playlist = r"D:\TDownload\fireball playlist - YouTube.html"
    if not vUrl and not playlist: return 'No parameter found.'
    # 如果是视频网址
    if vUrl:
        # os.popen('start chrome http://en.savefrom.net/#url=%s'%vUrl)
        yid = ''.join( re.findall('watch\?v=([^&=]+)', vUrl) )
        urls = [
            'start chrome http://en.savefrom.net/#url=https:/www.youtube.com/watch?v=%s'%yid,
            'start chrome http://savemedia.com/watch?v=%s'%yid
        ]
        for i in urls: os.popen(i)
    # 如果是列表
    if playlist:
        print 'Parsing %s'%playlist
        html = ''
        # 判断是列表网址或是本地网页文件地址
        if 'http' in playlist[0:5]: 
            hd = {'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))'}
            html = requests.get(playlist, headers=hd, timeout=5).text
        else: 
            with open(playlist, 'r') as f: html = f.read()
        resu = re.findall('watch\?v=([^&=]+)', html)
        # 利用集合去除重复项
        saveFrom = set([ 'start chrome http://en.savefrom.net/#url=https:/www.youtube.com/watch?v=%s'%i for i in resu ])
        saveMedia = set([ 'start chrome http://savemedia.com/watch?v=%s'%i for i in resu ])
        for i in saveFrom: os.popen(i)
        for i in saveMedia: os.popen(i)

if __name__ == '__main__':
    print main()