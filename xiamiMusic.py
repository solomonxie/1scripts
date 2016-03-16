# coding:utf-8

from bs4 import BeautifulSoup
from threading import Thread
import requests
import os, re, time, zipfile

def main():
    Xiami()

class Xiami():
    def __init__(self):
        self.folder = '%s\\xiami(%s)\\'%(os.getcwd(), time.strftime('%Y-%m-%d'))
        if not os.path.exists(self.folder): os.mkdir(self.folder)
        self.online = True
        self.collections = []
        self.singers = []
        self.songs = []
        self.albums = []
        self.hd = {
            'GET': '/space/collect/u/38443336?spm=a1z1s.6626009.229054153.5.pMbJFI HTTP/1.1',
            'Host': 'www.xiami.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6',
            # 'Cookie': 'ahtena_is_show=true; _unsign_token=415346aa41365b54a4d644f5daf45878; isg=E96080E9F3B2CB801ACE950734B83C8D; member_auth=0jubE9oY7jhjgKiRG400ISUc6OHRGDKDwolV3bUpvgUgLYddZNLwkauSSg9M2yOQrmHLngtIVYaWmmmKgW14STtdkvQN7vt6Ww; user=38443336%22%E4%BA%86%E4%B8%8D%E8%B5%B7%E7%9A%84%E8%B0%A2%E6%BD%87%E4%B9%8B%22images%2Favatar_new%2F768%2F384433361403690171_1.jpg%222%229910%22%3Ca+href%3D%27%2Fwebsitehelp%23help9_3%27+%3Esi%3C%2Fa%3E%220%2218%2240690%22ad7c136564%221454537674; _xiamitoken=4eb85b123b73ab72d365718cf994700a; CNZZDATA2629111=cnzz_eid%3D1584693888-1452403648-%26ntime%3D1454534600; CNZZDATA921634=cnzz_eid%3D449687629-1452404398-%26ntime%3D1454536422; l=Ag4O1IwTf7zNOctQWUF8M4fY3u7Qj9KJ'
            'Cookie': 'join_from=0T2dTo8YuGA12%2F%2FB; _unsign_token=4c94c6939d3709e3efe1ed97941b7752; user_from=4; member_auth=0jubE9oY7jhjgKiRG400ISUc6OHRGDKDwolV3bUpvgUgLYddZNLwkauSSg9M2yOQrmHLngtIVYaWmmmKgW14STtdkvQN7vt6Ww; user=38443336%22%E4%BA%86%E4%B8%8D%E8%B5%B7%E7%9A%84%E8%B0%A2%E6%BD%87%E4%B9%8B%22images%2Favatar_new%2F768%2F384433361403690171_1.jpg%220%2210493%22%3Ca+href%3D%27%2Fwebsitehelp%23help9_3%27+%3EDo%E2%80%A2%3C%2Fa%3E%220%2218%2241544%22ad7c136564%221457026571; t_sign_auth=43; ahtena_is_show=true; _xiamitoken=8e991ab5d94baea81fa1a0ccac0aa42a; CNZZDATA921634=cnzz_eid%3D944355475-1457022685-http%253A%252F%252Fcn.bing.com%252F%26ntime%3D1457022685; CNZZDATA2629111=cnzz_eid%3D1456048952-1457021881-http%253A%252F%252Fcn.bing.com%252F%26ntime%3D1457021881; l=Ara231kEW7Zkcz3PqHEE0RIuhua4rPoR'
        }
        # === 初始化时则立即读取所有信息 ===
        # 1.获取所有自建精选集并保存列表>>>>
        self.loadCollections()
        print 'Finished loading all %d collections.'%len(self.collections)
        with open(self.folder+r'\collections.html', 'w') as f:
            f.write( '\n'.join(self.collections).encode('utf-8') )
        # 2.获取所有关注歌手并保存为列表>>>>
        self.loadSingers()
        print 'Finished loading all %d singerd singers.'%len(self.singers)
        with open(self.folder+r'\singers.html', 'w') as f:
            f.write('<hr>'.join(self.singers).encode('utf-8'))
        # 3.获取所有收藏的歌曲并保存为列表>>>>
        self.loadLikedSongs()
        print 'Finished loading all %d songs.'%len(self.songs)
        with open(self.folder+r'\songs.html', 'w') as f:
            f.write('<br>'.join(self.songs).encode('utf-8'))
        # 4.获取所有收藏的专辑并保存为列表>>>>
        self.loadAlbums()
        print 'Finished loading all %d albums.'%len(self.albums)
        with open(self.folder+r'\albums.html', 'w') as f:
            f.write('<br>'.join(self.albums).encode('utf-8'))
        # ==== 打包文件 =====
        self.archive()

    def loadCollections(self, url='', pn=1):
        if not url: url = 'http://www.xiami.com/space/collect?u=38443336&order=1&p=1'
        print url
        r_session = requests.session()
        html = u'%s'%requests.get(url, headers=self.hd, timeout=5).text
        soup = BeautifulSoup(html, 'html5lib')
        npage = u''.join( re.findall('class="p_redirect_l" href="([^"]+)"', html) )
        if npage: self.loadCollections(url='http://www.xiami.com' + npage, pn=pn+1)
        # 先完成列表页面的读取 再逐次深入读取每个项的页面
        ids = set( u''.join(re.findall('<a href="\D+(\d+)"', unicode(i))) for i in soup.select('div.detail') )
        titles = set( i.get_text(strip=True) for i in soup.select('div.detail strong') )
        # for i in ids: self.__eachCollection(aid=i) # 单进程
        multiThread(func=self.__eachCollection, prams=ids) # 多线程

    def __eachCollection(self, aid, pn=1):
        url = 'http://www.xiami.com/collect/%s'%aid
        print url
        r_session = requests.session()
        html = requests.get(url, headers=self.hd, timeout=5).text
        soup = BeautifulSoup(html, 'html5lib')
        abTitle = u''.join(re.findall('<title>\s*([^_]+)\s*_[^<>]+</title>', html))
        # update = u''.join(re.findall('</span>\s*(\d{4}-\d{2}-\d{2})', html))
        songs = [unicode(i) for i in soup.select('span.song_name')]
        content = '<h1>%s</h1><hr>\n%s'%(abTitle, u'\n<br>\n'.join(songs))
        print '%d songs found in collection [%s].'%(len(songs), abTitle)
        self.collections.append(content)

    def loadSingers(self, pn=1):
        url = 'http://www.xiami.com/relation/following-artist/page/%d'%pn
        print url
        r_session = requests.session()
        html = u'%s'%requests.get(url, headers=self.hd, timeout=5).text
        resu = [unicode(i.get_text(strip=True)) for i in BeautifulSoup(html, 'html5lib').select('a.name')]
        if len(resu) < 1: return
        self.singers += resu
        print 'loaded %d singers.'%len(resu)
        # === (这里开始只有在第一页时运行会被调用) ===
        if pn == 1: # 计算总页码 并从第2页开始使用多线程
            n = int( '\n'.join(re.findall('<span>\([^\d]+\d+[^\d]+(\d+)[^\d]+\)</span>', html)) )
            per = len(resu)
            tp = n/per if n%per == 0 else n/per+1
            print 'Total: %d singers, %d pages.'%(n, tp)
            t = 10 # 控制线程数 同一时间运行不要超过10个线程
            for i in range(0, tp, t):
                multiThread(func=self.loadSingers, prams=range(i+2,i+t+2) if tp-i>10 else range(i+2,tp+1))

    def loadLikedSongs(self, pn=1):
        url = 'http://www.xiami.com/space/lib-song/u/38443336/page/%d'%pn
        print url
        r_session = requests.session()
        html = u'%s'%requests.get(url, headers=self.hd, timeout=5).text
        # with open(self.folder+r'\songs-1.html', 'r') as f: html = f.read() # 调试用
        resu = [unicode(i.get_text(strip=True)) for i in BeautifulSoup(html, 'html5lib').select('td.song_name')]
        if len(resu) < 1: return
        self.songs += resu
        print 'loaded %d liked songs.'%len(resu)
        # === (这里开始只有在第一页时运行会被调用) ===
        if pn == 1: # 计算总页码 并从第2页开始使用多线程
            n = int( '\n'.join(re.findall('<span>\([^\d]+\d+[^\d]+(\d+)[^\d]+\)</span>', html)) )
            per = len(resu)
            tp = n/per if n%per == 0 else n/per+1
            print 'Total: %d songs, %d pages.'%(n, tp)
            t = 10 # 控制线程数 同一时间运行不要超过10个线程
            for i in range(0, tp, t):
                multiThread(func=self.loadLikedSongs, prams=range(i+2,i+t+2) if tp-i>10 else range(i+2,tp+1))

    def loadAlbums(self, pn=1):
        url = 'http://www.xiami.com/space/lib-album/u/38443336/page/%d'%pn
        print url
        r_session = requests.session()
        html = u'%s'%requests.get(url, headers=self.hd, timeout=5).text
        # with open(self.folder+r'\albums-1.html', 'r') as f: html = f.read() # 调试用
        resu = ['--'.join(re.findall('title="([^"]+)"',unicode(i))) for i in BeautifulSoup(html, 'html5lib').select('div.detail div.name')]
        if len(resu) < 1: return
        self.albums += resu
        print 'loaded %d albums.'%len(resu)
        # === (这里开始只有在第一页时运行会被调用) ===
        if pn == 1: # 计算总页码 并从第2页开始使用多线程
            n = int( '\n'.join(re.findall('<span>\([^\d]+\d+[^\d]+(\d+)[^\d]+\)</span>', html)) )
            per = len(resu)
            tp = n/per if n%per == 0 else n/per+1
            print 'Total: %d albums, %d pages.'%(n, tp)
            t = 10 # 控制线程数 同一时间运行不要超过10个线程
            for i in range(0, tp, t):
                multiThread(func=self.loadAlbums, prams=range(i+2,i+t+2) if tp-i>10 else range(i+2,tp+1))

    def archive(self, dele=True):
        files = os.listdir(self.folder) # listdir()在接收unicode参数时会返回unicode格式的文件目录
        folder = [fo for fo in self.folder.split('\\') if fo][-1]
        zipname = folder + '.zip' # 以文件夹名称为zip文件名
        print '%d files to be compressed.' % len(files), files
        z = zipfile.ZipFile(zipname, 'w')
        for f in files:
            z.write(self.folder+f, folder+'\\'+f)
        z.close()
        if dele: __import__('shutil').rmtree(self.folder) # 完成后删除原文件夹

def multiThread(func, prams):
    threadList = []
    for p in prams:
        t = Thread(target=func, args=(p,))
        t.start()
        threadList.append(t)
    print '\n-----Processing with %d threads.-----\n'%len(threadList)
    for sub in threadList:
        sub.join()


if __name__ == '__main__':
    main()
    