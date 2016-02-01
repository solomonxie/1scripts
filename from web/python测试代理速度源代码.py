#!/usr/bin/env python
#coding:utf-8

"""Get proxies from urls, and test their speed"""
import urllib, re, time, threading

urls = ["http://proxy.ipcn.org/proxylist.html",
        "http://info.hustonline.net/index/proxyshow.aspx"
        ]       #where to get proxies
urls_proxy = {}     #proxy used to connect urls
proxy_pattern = re.compile(r"""\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,}""")
test_url = "http://www.python.org/"
test_pattern = re.compile(r"""xs4all""")
time_out = 30.0     #max waiting time to test proxies
output_file = "Proxies.txt"

class TestTime(threading.Thread):
    """test a proxy's speed in new thread by recording its connect time"""
    def __init__(self, proxy):
        threading.Thread.__init__(self)
        self.proxy = proxy
        self.time = None
        self.stat = proxy + " time out!"
    def run(self):
        start = time.time()
        try:
            f = urllib.urlopen(test_url, proxies = {"http":"http://"+self.proxy})
        except:
            self.stat = self.proxy+" fails!"
        else:
            data = f.read()
            f.close()
            end = time.time()
            if test_pattern.search(data): #if data is matched
                self.time = end-start
                self.stat = self.proxy+" time: "+str(self.time)
            else:
                self.stat = self.proxy+" not matched!"

def totest(proxy, result):
    """test a proxy's speed in time_out seconds"""
    test = TestTime(proxy)
    test.setDaemon(True)
    print "testing "+proxy
    test.start()
    test.join(time_out)     #wait time_out seconds for testing
    print test.stat
    if test.time:
        result.append((test.time, proxy))

if __name__ == "__main__":
    #get old proxies in output_file
    try:
        f = open(output_file)
    except:
        allproxies = set()
    else:
        allproxies = set([x[:-1] for x in f.readlines()])
        f.close()   

    #get else proxies from urls
    for url in urls:
        print "getting proxy from "+url
        try:
            f = urllib.urlopen(url, proxies=urls_proxy)
        except:
            print url+" can not open!\n"
        else:
            data = f.read()
            f.close()
            allproxies.update(proxy_pattern.findall(data))
            print url+" finished!"

    #test all proxies' speed
    result = []
    for proxy in allproxies:
        #new thread to test every proxy
        t = threading.Thread(target=totest, args=(proxy, result))
        t.setDaemon(True)
        t.start()

    #show all proxies' speed
    time.sleep(time_out+5.0)
    result.sort()
    for i in xrange(len(result)):
        print str(i+1)+"\t"+result[i][1]+"   \t:\t"+str(result[i][0])

    #output needed proxies
    num = min(abs(int(raw_input("\nHow many proxies to output: "))), len(result))
    try:
        f = open(output_file, "w")
    except:
        print "Can not open output file!"
    else:
        f.writelines([x[1]+"\n" for x in result[:num]])
        f.close()
        print str(num)+" proxies are output."