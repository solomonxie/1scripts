# coding:utf-8
'''
  # Title   : computerLocations
  # Author  : Solomon Xie
  # Utility : 
  # Require : Python 2.x, Windows 7
  # Anlysis : 
  # Method  : 
  # Notes   : 
'''
import os, sys, re, getopt

def main():
    parseInstruction()

def parseInstruction(ins=""):
    print sites(eg='fo:recent', key='hello')

def sites(eg="", key="", gp=""):
    engines = []
    # --圣经搜索--
    engines.append(["BibleGateway", "https://www.biblegateway.com/quicksearch/?quicksearch="+key, "Bible"]) #Bible Gateway
    engines.append(["BibleOnline", "http://www.chinesebibleonline.com/search?key="+key, "Bible"]) #中文圣经在线
    engines.append(["LzzBible", "http://cn.bing.com/search?q=site:www.cclw.net/Bible/LzzBible/ "+key, "Bible"]) #吕振中版圣经
    engines.append(["Hymns", "http://cn.bing.com/search?q=site:zanmeishi.com/ "+key, "Bible"]) #赞美诗网
    # --本地文件夹--
    engines.append(["fo", "D:\\TDownload\\"])
    engines.append(["fo:C", "C:\\"])
    engines.append(["fo:D", "D:\\"])
    engines.append(["fo:Recent", "C:\\Users\\Administrator\\Recent\\"]) #最近使用文件
    engines.append(["fo:Doc", "D:\\Documents\\"])
    engines.append(["fo:Down", "D:\\TDownload\\"])
    engines.append(["fo:Soft", "D:\\TDownload\\Softwares\\Developer\\"])
    engines.append(["fo:Work", "D:\\Workspace\\"])
    engines.append(["fo:Web", "D:\\Workspace\\Websites\\"])
    engines.append(["fo:My", "D:\\Solomon Xie\\"])
    engines.append(["fo:Pic", "D:\\Pictures\\"])
    engines.append(["fo:Wa", "D:\\Documents\\_WEB_ARTICLES\\"])
    engines.append(["fo:History", "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Recent"])
    engines.append(["fo:Tech", "D:\\Documents\\_TECH_ARTICLES\\"])
    engines.append(["fo:Net", "D:\\Documents\\_TECH_ARTICLES\\Network\\"])
    engines.append(["fo:Proxy", "D:\\Documents\\_TECH_ARTICLES\\Network\\Proxies\\"])
    engines.append(["fo:Py", "D:\\Documents\\_TECH_ARTICLES\\Python\\"])
    engines.append(["fo:Spider", "D:\\Documents\\_TECH_ARTICLES\\Crawler\\"])
    engines.append(["fo:Dev", "D:\\Documents\\_TECH_ARTICLES\\Developer\\"])
    engines.append(["fo:IDE", "D:\\Documents\\_TECH_ARTICLES\\IDE\\"])
    engines.append(["fo:Shell", "D:\\Documents\\_TECH_ARTICLES\\Shell\\"])
    engines.append(["fo:Site", "D:\\Documents\\_TECH_ARTICLES\\Website\\"])
    # --本地文件/服务/设置--
    engines.append(["help", "D:\\Documents\\_TECH_ARTICLES\\Developer\\AutoHotkey\\AutoHotkey.chm"])
    engines.append(["sys", "Control System"]) #系统设置
    engines.append(["sys:CptMan", "compmgmt.msc"]) #计算机管理
    engines.append(["sys:RemoteDesk", "mstsc"]) #远程桌面
    engines.append(["sys:Reg", "Regedit"]) #注册表
    engines.append(["sys:GPO", "GPedit.msc"]) #组策略
    engines.append(["sys:Services", "Services.msc"]) #服务
    engines.append(["sys:event", "GPedit.msc"]) #事件查看器
    engines.append(["onepass", "D:\\Solomon Xie\\GateToSolomonXieMC@2.docx"])
    engines.append(["setProxy", "D:\\Solomon Xie\\Workspace\\setRegProxy.py"]) #Python设置代理脚本，接收命令行参数
    engines.append(["sys:install", "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl,,1"]) #安装/卸载软件
    # --常用软件--
    engines.append(["Vim", "Vim"]) #VIM
    engines.append(["cmd", "D:\\TDownload\\Softwares\\Developer\\cmder\\Cmder.exe "+key]) #cmd的增强版工具
    engines.append(["Down", "C:\\Program Files\\Thunder Network\\Thunder\\Program\\Thunder.exe "+key]) #迅雷下载
    engines.append(["Rec", "C:\\Program Files\\Blueberry Software\\BB FlashBack Pro 5\\FlashBack Recorder.exe"]) #屏幕录像
    engines.append(["QQ", "C:\\Program Files\\Tencent\\QQ\\Bin\\QQScLauncher.exe"])
    engines.append(["QQPlayer", "C:\\Program Files\\Tencent\\QQPlayer\\QQPlayer.exe"])
    engines.append(["BaiduYun", "C:\\Users\\Administrator\\AppData\\Roaming\\Baidu\\BaiduYunGuanjia\\BaiduYunGuanjia.exe"])
    engines.append(["Wechat", "C:\\Program Files\\Tencent\\WeChat\\WeChat.exe"])
    engines.append(["Word", "WinWord"])
    engines.append(["Excel", "Excel"])
    engines.append(["PPT", "PowerPnt"])
    engines.append(["Access", "MsAccess"])
    engines.append(["Calcu", "C:\\Windows\\system32\\calc.exe"]) #计算器
    engines.append(["Draw", "C:\\Windows\\system32\\mspaint.exe"]) #画图
    engines.append(["IE", "C:\\Program Files\\Internet Explorer\\iexplore.exe "+key])
    engines.append(["Chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe "+key])
    engines.append(["ff", "C:\\Program Files\\Mozilla Firefox\\firefox.exe "+key])
    engines.append(["3L", "C:\\Users\\Administrator\\AppData\\Local\\360Chrome\\Chrome\\Application\\360chrome.exe "+key]) #360极速浏览器
    engines.append(["Calc", "C:\\Windows\\system32\\calc.exe"]) #计算器
    engines.append(["PicMan", "Ois"]) #Ms Office Picture Manager 自带图片管理工具
    engines.append(["Publisher", "MSPUB"]) #Ms Office Publisher
    engines.append(["Xampp", "C:\\xampp\\xampp-control.exe"]) #XAMPP服务器
    engines.append(["Graphviz", "C:\\Program Files\\Graphviz2.38\\bin\\gvedit.exe"])
    engines.append(["Sublime", "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"]) #Sublime Text
    engines.append(["Foxit", "C:\\Program Files\\Foxit Software\\Foxit Reader\\FoxitReader.exe"]) #Foxit浏览器
    engines.append(["FTP", "C:\\Program Files\\FileZilla FTP Client\\filezilla.exe"]) #FTP上传工具
    engines.append(["Wireshark", "C:\\Program Files\\Wireshark\\Wireshark-gtk.exe"]) #Wireshark
    engines.append(["Xiami", "C:\\Program Files\\Xiami\\XMusic\\XMusic.exe"]) #虾米音乐
    engines.append(["VBox", "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"]) #VirtualBox虚拟机
    # --命令行操作--
    engines.append(["ieSettings", "rundll32.exe shell32.dll, Control_RunDLL inetcpl.cpl, ,4L"]) #设置代理
    # -- 邮箱及云盘 --
    engines.append(["QQmail", "http://mail.qq.com"]) #
    engines.append(["163", "http://mail.163.com/"]) #
    engines.append(["Outlook", "http://outlook.com"]) #
    engines.append(["Gmail", "http://mail.google.com"]) #
    # --主流搜索--
    engines.append(["Bing", "http://cn.bing.com/?q="+key]) #必应搜索
    engines.append(["Baidu", "https://www.baidu.com/s?wd="+key]) #百度搜索
    engines.append(["Google", "https://www.google.com/#newwindow=1&q="+key]) #谷歌搜索
    engines.append(["D", "http://cn.bing.com/dict/?q="+key]) #必应词典
    engines.append(["Wiki", "https://en.wikipedia.org/w/index.php?search="+key]) #维基百科
    engines.append(["Baike", "http://baike.baidu.com/search?word="+key]) #百度百科
    engines.append(["Douban", "http://www.douban.com/search?source=suggest&q="+key]) #豆瓣
    engines.append(["dm", "http://movie.douban.com/subject_search?search_text="+key]) #豆瓣电影
    engines.append(["Zhihu", "https://www.zhihu.com/search?type=question&q="+key]) #知乎
    engines.append(["Taobao", "https://s.taobao.com/search?q="+key]) #淘宝
    engines.append(["DouLie", "https://cse.google.com/cse/home?q="+key+"&cx=004798099194550741737:qvcmshog6v4"])
    engines.append(["QRcode", "https://chart.googleapis.com/chart?cht=qr&chs=500x500&choe=UTF-8&chld=L|4&chl="+key])
    engines.append(["Phone", "http://ip.cn/db.php?num="]) #电话号码查询
    engines.append(["allitebooks", "http://www.allitebooks.com/?s="+key]) #全部免费IT电子书
    # --技术文章--
    engines.append(["JianShu", "http://www.jianshu.com/search?q="+key, "Tech"]) #简书
    engines.append(["Weixin", "http://weixin.sogou.com/weixin?type=2&query="+key, "Tech"]) #微信文章搜索
    engines.append(["sef", "http://segmentfault.com/search?q="+key, "Tech"]) #segmentfault
    engines.append(["sof", "http://cn.bing.com/?q=site:stackoverflow.com+"+key, "Tech"]) #Stackoverflow
    engines.append(["jikett", "http://geek.csdn.net/search/"+key, "Tech"]) #极客头条
    engines.append(["otf", "http://outofmemory.cn/search?q="+key, "Tech"]) #内存溢出
    engines.append(["TouTiao", "http://toutiao.io/search?q="+key, "Tech"]) #开发者头条
    engines.append(["CSDN", "http://so.csdn.net/so/search/s.do?t=blog&q="+key, "Tech"]) #csdn
    engines.append(["xtjj", "http://cn.bing.com/?q=site:gold.xitu.io+"+key, "Tech"]) #稀土掘金
    engines.append(["cnHackerNews", "http://cn.bing.com/?q=site:news.dbanotes.net+"+key, "Tech"]) #中国版HackerNews
    engines.append(["V2EX", "http://cn.bing.com/?q=site:v2ex.com/t+"+key, "Tech"]) #V2EX
    engines.append(["RunOob", "http://www.runoob.com/?s="+key, "Tech"]) #菜鸟教程
    engines.append(["4byte", "http://www.4byte.cn/q?wd="+key, "Tech"]) #字节技术
    engines.append(["Gbtags", "http://www.gbtags.com/gb/search.htm?source=gbtags&s="+key, "Tech"]) #极客标签
    # --在线视频--
    engines.append(["tudou", "http://www.soku.com/t/nisearch/"+key, "Video"]) #土豆网/优酷网
    engines.append(["youtube", "https://www.youtube.com/results?search_query="+key, "Video"]) # Youtube
    engines.append(["letv", "http://so.letv.com/s?wd="+key, "Video"]) #乐视网
    engines.append(["iqi", "http://so.iqiyi.com/so/q_"+key, "Video"]) #爱奇艺
    engines.append(["Vimeo", "https://vimeo.com/search?q="+key, "Video"]) #
    # --资源下载--
    engines.append(["pan", "http://cn.bing.com/?q=site:pan.baidu.com+"+key, "BT"]) #百度网盘
    engines.append(["pdf", "https://www.google.com/#newwindow=1&q=type:pdf+"+key]) #pdf下载
    engines.append(["btdigg", "https://btdigg.org/search?info_hash=&q="+key, "BT"])
    engines.append(["cilibaba", "http://www.cilibaba.com/search/"+key, "BT"])
    engines.append(["piratebay", "http://thepiratebay.cd/search/"+key, "BT"])
    engines.append(["zhaobt", "http://www.zhaobt.net/"+key+"-first-asc-1.html?f=h", "BT"])
    engines.append(["okbt", "http://www.okbt.net/search/"+key, "BT"])
    engines.append(["bthand", "http://www.bthand.com/search/"+key+".html", "BT"])
    engines.append(["yunpansoso", "http://www.yunpansoso.com/search.html?keyword="+key, "BT"])
    engines.append(["btmeiju", "http://www.btmeiju.com/ustv_search.htm?title="+key, "BT"]) #BT美剧
    engines.append(["bttiantang", "http://www.bttiantang.com/s.php?q="+key, "BT"]) #BT天堂
    # --资源解析--
    engines.append(["flvcd", "http://www.flvcd.com/parse.php?format=&kw="+key, "getvideo"]) #硕鼠视频解析
    engines.append(["saveFrom", "http://sfrom.net/"+key,"getvideo"]) #国外网站视频解析
    engines.append(["saveMedia", "http://savemedia.com/watch?v="+key, "getvideo"]) #国外网站视频解析
    # --在线课程--
    engines.append(["jikexy", "http://search.jikexueyuan.com/course/?q="+key, "cnCourse"]) #极客学院搜索
    engines.append(["guoke", "http://mooc.guokr.com/search/?wd="+key, "cnCourse"]) #果壳MOOC：各平台综合搜索
    engines.append(["Gkk", "http://c.open.163.com/search/search.htm?query="+key, "cnCourse"]) #网易公开课
    engines.append(["Ykt", "http://study.163.com/search.htm?p="+key, "cnCourse"]) #网易云课堂
    engines.append(["yunlu", "http://yun.lu/student/course/list/0?q="+key, "cnCourse"]) #云路课堂
    engines.append(["Chuanke", "http://www.chuanke.com/course/_"+key+"_____.html", "cnCourse"])
    engines.append(["Udemy", "https://www.udemy.com/courses/search/?price=price-free&q="+key, "enCourse"])
    engines.append(["Coursera", "https://www.coursera.org/courses?query="+key, "enCourse"])
    engines.append(["CodeAcademy", "http://cn.bing.com/search?q=site:codeacademy.com+"+key, "enCourse"])
    engines.append(["Lynda", "http://www.lynda.com/search?q="+key, "enCourse"])
    engines.append(["Courses.com", "http://www.courses.com/s?q="+key, "enCourse"])
    engines.append(["Alison", "https://alison.com/search/result/?q="+key, "enCourse"])
    # --代理服务器--
    engines.append(["myip", "http://ip.cn/"]) #查询本机的公网IP
    engines.append(["duotai", "https://duotai.org/login"]) #多态网ZPN（全平台提供PAC自动配置代理的脚本）
    engines.append(["kjson", "https://www.kjson.com/proxy/", "ips"]) 
    engines.append(["ip1", "http://proxy.ipcn.org/proxylist.html", "ips"]) 
    engines.append(["ip2", "http://proxy.goubanjia.com/free/", "ips"]) 
    engines.append(["ip3", "http://www.kuaidaili.com/", "ips"])
    engines.append(["ip4", "http://www.xicidaili.com/", "ips"]) 
    engines.append(["ip5", "http://proxylist.hidemyass.com/", "ips"])
    engines.append(["ip6", "https://nordvpn.com/free-proxy-list/", "ips"])
    engines.append(["ip7", "https://incloak.com/proxy-list/", "ips"])
    engines.append(["ip8", "http://ip.izmoney.com/", "ips"])
    engines.append(["ip9", "http://ip.qiaodm.com/", "ips"])

    # if gp = "" :
    #     loop % engines.MaxIndex()
    #         if engines[A_Index][1] = eg :
    #             return engines[A_Index][2]
    # else
    #     retu := []
    #     loop % engines.MaxIndex()
    #         if (engines[A_Index][3] = gp)
    #             retu.append(engines[A_Index][2])
    #     return retu
    retu = []
    if gp == '':
        for lo in engines:
            if lo[0].lower() == eg.lower():
                retu.append(lo[1])
    else:
        for lo in engines:
            if len(lo) < 3: continue
            if lo[2].lower() == gp.lower():
                retu.append(lo[1])
    return retu


if __name__ == '__main__':
    main()