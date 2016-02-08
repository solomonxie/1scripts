# coding:utf-8
import os, sys, re, getopt
import requests # 第三方模块

def main():
    opts, args = getopt.getopt(sys.argv[1:], 'v:l:b', ['video=','list=', 'browse', 'svm', 'svf'])
    urls = []
    vUrl = playlist = folder = ''
    browse, svf, svm = False, False, True
    for o,a in opts:
        if   o == '-v' or o == '--video': vUrl = a
        elif o == '-l' or o == '--list': playlist = a
        elif o == '-b' or o == '--browse': browse = True
        elif o == '--svf': svf = True
        elif o == '--svm': svm = True
    # 测试用
    # vUrl = 'https://www.youtube.com/watch?v=HMqgVXSvwGo&index=1&list=PLNCVk_zarBEsIqlQBcYVIpuBlyY2hy0Z0'
    # playlist = r"D:\TDownload\youtu.html" # 测试用
    if not vUrl and not playlist: return 'No parameter found.'
    if 'youtube.com/playlist?list=' in vUrl: playlist, vUrl = vUrl, ''
    # 如果是视频网址
    if vUrl:
        # os.popen('start chrome http://en.savefrom.net/#url=%s'%vUrl)
        yid = ''.join( re.findall('watch\?v=([^&="]+)', vUrl) )
        if len(yid) < 1: return
        urls = [
            'http://en.savefrom.net/#url=https:/www.youtube.com/watch?v=%s'%yid,
            'http://savemedia.com/watch?v=%s'%yid
        ]
        if browse:
            for i in urls: os.popen('start chrome %s'%i)
        else: genHTML(urls)
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
        if len(resu) < 1: return
        if   svf: urls = set([ 'http://en.savefrom.net/#url=https:/www.youtube.com/watch?v=%s'%i for i in resu ])
        elif svm: urls = set([ 'http://savemedia.com/watch?v=%s'%i for i in resu ])
        if browse:
            for i in urls: os.popen('start chrome %s'%i)
        else: genHTML(urls)

def genHTML(urls):
    html = ''
    i = 1
    for u in urls: 
        html += '<p>%d.<a href="%s">%s</a></p>'%(i,u, u)
        i += 1
    path = os.environ['TEMP'] + '\playlist.html'
    with open(path, 'w') as f: f.write(html)
    os.popen(path)

if __name__ == '__main__':
    print main()