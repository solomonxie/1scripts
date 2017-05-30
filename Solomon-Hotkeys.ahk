/*
	=== 笔记 ===
	^  -----> Ctrl
	+  -----> Shift
	!  -----> Alt
	#  -----> Win
	- Pause/ScrollLock/PrintScreen等特殊键，不能配合ctrl/shift或组合使用，目前好像只能配合Alt使用
	- if else语法"博大精深"，带不带()括号，决定了表达式的写法！简单说if (var = "text")，或者 if %var% = text 这样的
	  或者 #if 又大有不同
	- 变量赋值语句也博大精深！如果涉及到字符串与变量连接那就深了去了：
	  var="456"的话 s = "123%var%"或s := "123"var这样才行
	- #IfWinActive 这个东西完成后呢，下面不能再全局注册键盘了。。。所以尽量把这种语句放在源码最下面
*/

; === 全局键盘设定 ===
Global(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
;--- 键盘重新映射 ---
Pause::Suspend ;暂停/开启脚本
!Pause::Reload  ;重新加载本AHK脚本文件
; PrintScreen::Send ^+{Esc} ;任务管理器
PrintScreen:: RunOrAct("ahk_class PuTTY", "Putty")
Insert::Return
!Insert::Insert ;Alt+Insert 代表原Insert键
ScrollLock::MultiTask()
!ScrollLock::ScrollLock
; --- 快捷启动 ---
F1::  RunOrAct("ahk_exe chrome.exe", "Chrome")
; F3::  RunOrAct("ahk_exe WINWORD.EXE", "Word")
<<<<<<< HEAD
F4::  Run % Sites("Sublime") ;RunOrAct("ahk_class PX_WINDOW_CLASS", "Sublime")
=======
F4::  Run % Sites("Subl") ;RunOrAct("ahk_class PX_WINDOW_CLASS", "Sublime")
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
; F9::  RunOrAct("ahk_exe filezilla.exe", "FTP")
F10::  RunOrAct("ahk_exe filezilla.exe", "FTP")
; !F2:: RunOrAct("ahk_class CabinetWClass", "fo:down")
^!W:: Send !{F4} ;关闭当前程序
^!T:: RunOrAct("ahk_exe ConEmu.exe", "cmd" )

RunOrAct(app, eg) {
	IfWinExist % app
		IfWinNotActive % app
			WinActivate  % app
		else
			WinMinimize % app
	else
		RunWait % Sites(eg)
		WinActivate  % app
	Return
}

Orientation(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
; === 基本方向操作 ===
!Space::Send {Click}
!Up::   Send {WheelUp}    ;鼠标上滚
!Down:: Send {WheelDown}  ;鼠标下滚
!Left:: Send {WheelLeft}  ;鼠标左滚
!Right::Send {WheelRight} ;鼠标右滚
!9::Send {WheelUp}        ;鼠标上滚
!0::Send {WheelDown}      ;鼠标下滚
!U::Send {WheelLeft}      ;鼠标左滚
!O::Send {WheelRight}     ;鼠标右滚
![:: Send ^{PgUp} ;向左切换标签
!]:: Send ^{PgDn}  ;向右切换标签
; !I:: MouseMove, 0, -200 , 1, R
; !K:: MouseMove, 0,  200 , 1, R
; !J:: MouseMove, -200, 0 , 1, R
; !L:: MouseMove, 200,  0 , 1, R
!I::MouseClickDrag, L, 0, 0, 0, -10, 1, R
!K::MouseClickDrag, L, 0, 0, 0,  10, 1, R
!J::MouseClickDrag, L, 0, 0, -10, 0, 1, R
!L::MouseClickDrag, L, 0, 0,  10, 0, 1, R

Snippet(){
	;(代码糖，用来在Ctrl+R快速跳转)
} 
; -- 个人信息Snippet快捷键 (Chrome Only) -->
::@sol::solomonxie@foxmail.com

MultiTask(){
	; --- 获取指令及关键词 ---
	InputBox, fullCommand, (Command Line Interface), Please give me a command:, , 600, 130 ;获取搜索引擎的指定
	if (fullcommand = "")
		Return
	; -- 解析命令行 ---
	split  := " " 
	StringGetPos , posi, fullCommand, %split%
	if (posi > 0) {
		StringMid, eg, fullCommand, 0 , posi ;
		StringMid, key, fullCommand, posi+2 , StrLen(fullCommand)
	}
	else {
		eg := fullCommand
		key := ""
	}
	; ---开始搜索---
	if      (eg = "" and fullcommand != "")
		Run % Sites("Bing", key)
	else if (eg = "Proxy"){
		if (key = "")
			Run % Sites("ieSettings")
		else if (key = "Off")
			Run % Sites("setProxy") " --off "
		else if (key = "On")
			Run % Sites("setProxy") " -p "
		else
			Run % Sites("setProxy") " -p """ key """"  ;想在字符串里引用双引号 同时又加上变量 只能这样用
	}
	else if (eg = "Pac" and key != "") {
		if (key = "Off")
			Run % Sites("setProxy") " --off "
		else if (key = "1")
			Run % Sites("setProxy") " --pac """ Sites("PAC1") """"
		else if (key = "2")
			Run % Sites("setProxy") " --pac """ Sites("PAC2") """"
		else if (key = "ON")
			Run % Sites("setProxy") " --pac """ Sites("PAC2") """"
		else
			Run % Sites("setProxy") " --pac """ key """"
	}
	else if (eg = "Mirror") {
		Run % Sites("Mirror") " -p " key ;用的时候路径必须带引号！
	}
	else if (eg="Bible" or eg="BT" or eg="Video" or eg="cnCourse" or eg="enCourse" or eg="IT" or eg="ips" or eg="getvideo" or eg="wp" or eg="itBlog") {
		resu := Sites("", key, eg)
		loop % resu.MaxIndex() 
			Run % resu[A_Index]
	}
	else if (eg="Down:Youtube") {
		Run % Sites("Down:Youtube") " --video """ key """"
	}
	else if (eg="Down:YoutubeList") {
		filePath := A_Temp "\youtube-playlist.html"
		file := FileOpen(filePath, "w")
		file.Write(Clipboard)
		file.Close()
		Run % Sites("Down:Youtube") " --list """ filePath """"
	}
	else {
		Run % Sites(eg, key)
	}
	Return
}


^!F12:: ;试验专用键 Ctrl+Alt+F12
{
	RunOrAct("ahk_exe ConEmu.exe", "cmd" )
}

; --- 制作搜索引擎链表 ---
Sites(eg="", key="", gp="") {
	engines := []
	; --圣经搜索--
	engines.insert(["BibleGateway", "https://www.biblegateway.com/quicksearch/?quicksearch=" key, "Bible"]) ;Bible Gateway
	engines.insert(["BibleOnline", "http://www.chinesebibleonline.com/search?key=" key, "Bible"]) ;中文圣经在线
	engines.insert(["LzzBible", "http://cn.bing.com/search?q=site:www.cclw.net/Bible/LzzBible/ " key, "Bible"]) ;吕振中版圣经
	engines.insert(["Hymns", "http://cn.bing.com/search?q=site:zanmeishi.com/ " key, "Bible"]) ;赞美诗网
	; --本地文件夹--
	engines.insert(["fo", "D:\TDownload\"])
	engines.insert(["fo:C", "C:\"])
	engines.insert(["fo:D", "D:\"])
	engines.insert(["fo:Run", A_WorkingDir]) ;获取当前脚本所在的目录
	engines.insert(["fo:Recent", "C:\Users\" A_UserName "\Recent\"]) ;最近使用文件
	engines.insert(["fo:Doc", A_MyDocuments])
	engines.insert(["fo:Down", "D:\TDownload\"])
	engines.insert(["fo:Soft", "D:\TDownload\Softwares\Developer\"])
	engines.insert(["fo:Work", "D:\Workspace\"])
	engines.insert(["fo:Web", "D:\Workspace\Websites\"])
	engines.insert(["fo:My", "D:\Solomon Xie\"])
<<<<<<< HEAD
	engines.insert(["fo:MyWork", "D:\Solomon Xie\Workspace\"])
	engines.insert(["fo:Gist", "D:\Solomon Xie\Workspace\Gists"])
=======
	engines.insert(["fo:Gists", "D:\Workspace\Gists"])
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
	engines.insert(["fo:Pic", "D:\Pictures\"])
	engines.insert(["fo:Wa", "D:\Documents\_WEB_ARTICLES\"])
	engines.insert(["fo:History", "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent"])
	engines.insert(["fo:Tech", "D:\Documents\_TECH_ARTICLES\"])
	engines.insert(["fo:Net", "D:\Documents\_TECH_ARTICLES\Network\"])
	engines.insert(["fo:Proxy", "D:\Documents\_TECH_ARTICLES\Network\Proxies\"])
	engines.insert(["fo:Py", "D:\Documents\_TECH_ARTICLES\Python\"])
	engines.insert(["fo:Spider", "D:\Documents\_TECH_ARTICLES\Crawler\"])
	engines.insert(["fo:Dev", "D:\Documents\_TECH_ARTICLES\Developer\"])
	engines.insert(["fo:IDE", "D:\Documents\_TECH_ARTICLES\IDE\"])
	engines.insert(["fo:Shell", "D:\Documents\_TECH_ARTICLES\Shell\"])
	engines.insert(["fo:Site", "D:\Documents\_TECH_ARTICLES\Website\"])
	; --本地文件/服务/设置--
	engines.insert(["help:AHK", "D:\Documents\_TECH_ARTICLES\Developer\AutoHotkey\AutoHotkey.chm"])
	engines.insert(["help:EC2", "http://aws.amazon.com/cn/documentation/ec2/?nc1=h_ls"])
	engines.insert(["help:Aliyun", "https://help.aliyun.com"])
	engines.insert(["sys", "Control System"]) ;系统设置
	engines.insert(["sys:CptMan", "compmgmt.msc"]) ;计算机管理
	engines.insert(["sys:RemoteDesk", "mstsc"]) ;远程桌面
	engines.insert(["sys:Reg", "Regedit"]) ;注册表
	engines.insert(["sys:GPO", "GPedit.msc"]) ;组策略
	engines.insert(["sys:Services", "Services.msc"]) ;服务
	engines.insert(["sys:event", "GPedit.msc"]) ;事件查看器
	engines.insert(["sys:hosts", "C:\Windows\System32\drivers\etc\hosts"]) ;事件查看器
	engines.insert(["This", "C:\Program Files\Sublime Text 3\sublime_text.exe """ A_ScriptFullPath """ "]) ;编辑本脚本
	engines.insert(["Gate", "D:\Solomon Xie\GateToSolomonXieMC@2.zip"])
<<<<<<< HEAD
	engines.insert(["setProxy", "D:\Solomon Xie\Workspace\Gists\getProxy.py"]) ;Python设置代理脚本，接收命令行参数
	engines.insert(["Mirror", "D:\Solomon Xie\Workspace\Gists\miniDiskMirror.py"]) ;Python设置任意文件夹镜像
=======
	engines.insert(["setProxy", "D:\Workspace\Gists\getProxy.py"]) ;Python设置代理脚本，接收命令行参数
	engines.insert(["Mirror", "D:\Workspace\Gists\miniDiskMirror.py"]) ;Python设置任意文件夹镜像
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
	engines.insert(["sys:install", "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl,,1"]) ;安装/卸载软件
	engines.insert(["ieSettings", "rundll32.exe shell32.dll, Control_RunDLL inetcpl.cpl, ,4L"]) ;设置代理
	; --常用软件--
	engines.insert(["Vim", "Vim"]) ;VIM
	engines.insert(["Putty", "D:\Workspace\bin\Putty\putty.exe"]) ;SSH连接
	engines.insert(["ShadowSocks", "D:\Workspace\bin\Shadowsocks\Shadowsocks.exe"])
	engines.insert(["ss", "D:\Workspace\bin\Shadowsocks\Shadowsocks.exe"])
	engines.insert(["sqlite", "D:\Workspace\bin\sqlitebrowser\sqlitebrowser.exe " key])
	engines.insert(["Lantern", "C:\Users\Administrator\AppData\Roaming\Lantern\lantern.exe"]) ;蓝灯翻墙
<<<<<<< HEAD
	engines.insert(["Ubuntu", "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe --comment Xunbuntu 32bit --startvm 2ac730ae-3424-4eea-b849-18fe5430e317"]) ;SSH连接
=======
	engines.insert(["Lubuntu", "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe --comment Lubuntu --startvm 689b1ec3-b2ea-4e39-9c40-04bdfa465ecf"]) ;SSH连接
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
	engines.insert(["MD", "https://stackedit.io/editor"]) ;Markdown编辑器
	engines.insert(["MD2", "http://www.jianshu.com/writer#/"]) ;Markdown编辑器 简书
	engines.insert(["MD3", "C:\Program Files\Google\Chrome\Application\chrome.exe  --profile-directory=Default --app-id=kidnkfckhbdkfgbicccmdggmpgogehop"]) ;Markdown编辑器 马克飞象
	engines.insert(["cmd", "D:\Workspace\bin\cmder\Cmder.exe " key]) ;cmd的增强版工具
	engines.insert(["Xunlei", "C:\Program Files\Thunder Network\Thunder\Program\Thunder.exe " key]) ;迅雷下载
	engines.insert(["Rec", "C:\Program Files\Blueberry Software\BB FlashBack Pro 5\FlashBack Recorder.exe"]) ;屏幕录像
	engines.insert(["QQ", "C:\Program Files\Tencent\QQ\Bin\QQScLauncher.exe"])
	engines.insert(["QQPlayer", "C:\Program Files\Tencent\QQPlayer\QQPlayer.exe"])
	engines.insert(["BaiduYun", "C:\Users\Administrator\AppData\Roaming\Baidu\BaiduYunGuanjia\BaiduYunGuanjia.exe"])
	engines.insert(["bdy", "C:\Users\Administrator\AppData\Roaming\Baidu\BaiduYunGuanjia\BaiduYunGuanjia.exe"])
	engines.insert(["Wechat", "C:\Program Files\Tencent\WeChat\WeChat.exe"])
	engines.insert(["FastCopy", "D:\Workspace\bin\FastCopy\FastCopy.exe"])
	engines.insert(["Word", "WinWord"])
	engines.insert(["Excel", "Excel"])
	engines.insert(["PPT", "PowerPnt"])
	engines.insert(["Access", "MsAccess"])
	engines.insert(["Jisuan", "C:\Windows\system32\calc.exe"]) ;计算器
	engines.insert(["Draw", "C:\Windows\system32\mspaint.exe"]) ;画图
	engines.insert(["IE", "C:\Program Files\Internet Explorer\iexplore.exe " key])
	engines.insert(["Chrome", "C:\Program Files\Google\Chrome\Application\chrome.exe " key])
	engines.insert(["ChromeApp", "C:\Program Files\Google\Chrome\Application\chrome.exe --show-app-list"])
	engines.insert(["ff", "C:\Program Files\Mozilla Firefox\firefox.exe " key])
	engines.insert(["3L", "C:\Users\Administrator\AppData\Local\360Chrome\Chrome\Application\360chrome.exe " key]) ;360极速浏览器
	engines.insert(["Calc", "C:\Windows\system32\calc.exe"]) ;计算器
	engines.insert(["PicMan", "Ois"]) ;Ms Office Picture Manager 自带图片管理工具
	engines.insert(["Publisher", "MSPUB"]) ;Ms Office Publisher
	engines.insert(["Xampp", "C:\xampp\xampp-control.exe"]) ;XAMPP服务器
	engines.insert(["Graphviz", "C:\Program Files\Graphviz2.38\bin\gvedit.exe"])
<<<<<<< HEAD
	engines.insert(["Sublime", "C:\Program Files\Sublime Text 3\sublime_text.exe"]) ;Sublime Text
=======
	engines.insert(["Subl", "C:\Program Files\Sublime Text 3\sublime_text.exe"]) ;Sublime Text
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
	engines.insert(["Foxit", "C:\Program Files\Foxit Software\Foxit Reader\FoxitReader.exe"]) ;Foxit浏览器
	engines.insert(["FTP", "C:\Program Files\FileZilla FTP Client\filezilla.exe"]) ;FTP上传工具
	engines.insert(["Wireshark", "C:\Program Files\Wireshark\Wireshark-gtk.exe"]) ;Wireshark
	engines.insert(["Xiami", "C:\Program Files\Xiami\XMusic\XMusic.exe"]) ;虾米音乐
	engines.insert(["VBox", "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"]) ;VirtualBox虚拟机
	engines.insert(["PAC1", "http://xduotai.com/xTsikkFkv.pac"]) ;PAC 自动配置代理脚本
	engines.insert(["PAC2", "https://pac.itzmx.com/abc.pac"]) ;PAC 自动配置代理脚本
	; --主流网站--
	engines.insert(["QQmail", "http://mail.qq.com"]) ;
	engines.insert(["163", "http://mail.163.com/"]) ;
	engines.insert(["Outlook", "http://outlook.com"]) ;
	engines.insert(["Gmail", "http://mail.google.com"]) ;
	engines.insert(["Yun", "http://pan.baidu.com"]) ;百度云盘网页版
	engines.insert(["Linkedin", "https://www.linkedin.com/"])
	; --技术控制站--
	engines.insert(["Aws", "https://aws.amazon.com/"]) ;
	engines.insert(["Admin:Aws", "https://console.aws.amazon.com/console/home"]) ;
	engines.insert(["Admin:Aliyun", "https://ecs.console.aliyun.com"]) ;
	engines.insert(["Admin:Do", "https://cloud.digitalocean.com/droplets"]) ; DigitalOcean
	; --主流搜索--
	engines.insert(["Bing", "http://cn.bing.com/?q=" key]) ;必应搜索
	engines.insert(["Baidu", "https://www.baidu.com/s?wd=" key]) ;百度搜索
	engines.insert(["Google", "https://www.google.com/#newwindow=1&q=" key]) ;谷歌搜索
	engines.insert(["B", "http://cn.bing.com/?q=" key]) ;必应搜索
	engines.insert(["G", "https://www.google.com/#newwindow=1&q=" key]) ;谷歌搜索
	engines.insert(["D", "http://cn.bing.com/dict/?q=" key]) ;必应词典
	engines.insert(["Dict", "http://cn.bing.com/dict/?q=" key]) ;必应词典
	engines.insert(["Wiki", "https://en.wikipedia.org/w/index.php?search=" key]) ;维基百科
	engines.insert(["Baike", "http://baike.baidu.com/search?word=" key]) ;百度百科
	engines.insert(["Douban", "http://www.douban.com/search?source=suggest&q=" key]) ;豆瓣
	engines.insert(["dm", "http://movie.douban.com/subject_search?search_text=" key]) ;豆瓣电影
	engines.insert(["Zhihu", "https://www.zhihu.com/search?type=question&q=" key]) ;知乎
	engines.insert(["Taobao", "https://s.taobao.com/search?q=" key]) ;淘宝
	engines.insert(["DouLie", "https://cse.google.com/cse/home?q=" key "&cx=004798099194550741737:qvcmshog6v4"])
	engines.insert(["QRcode", "https://chart.googleapis.com/chart?cht=qr&chs=500x500&choe=UTF-8&chld=L|4&chl=" key])
	engines.insert(["Phone", "http://ip.cn/db.php?num="]) ;电话号码查询
	engines.insert(["allitebooks", "http://www.allitebooks.com/?s=" key]) ;全部免费IT电子书
	engines.insert(["app", "http://www.yiyeso.com/s/" key]) ;iOS应用搜索
	; --在线视频--
	engines.insert(["tudou", "http://www.soku.com/t/nisearch/" key, "Video"]) ;土豆网/优酷网
	engines.insert(["youtube", "https://www.youtube.com/results?search_query=" key, "Video"]) ; Youtube
	engines.insert(["YoutubeList", "https://www.youtube.com/results?sp=EgIQAw%253D%253D&q=" key, "Video"]) ; Youtube
	engines.insert(["letv", "http://so.letv.com/s?wd=" key, "Video"]) ;乐视网
	engines.insert(["iqi", "http://so.iqiyi.com/so/q_" key, "Video"]) ;爱奇艺
	engines.insert(["Vimeo", "https://vimeo.com/search?q=" key, "Video"]) ;
	; --资源下载--
	engines.insert(["pan", "http://cn.bing.com/?q=site:pan.baidu.com+" key, "BT"]) ;百度网盘
	engines.insert(["pdf", "https://www.google.com/#newwindow=1&q=type:pdf+" key]) ;pdf下载
	engines.insert(["btdigg", "https://btdigg.org/search?info_hash=&q=" key, "BT"])
	engines.insert(["cilibaba", "http://www.cilibaba.com/search/" key, "BT"])
	engines.insert(["piratebay", "http://thepiratebay.cd/search/" key, "BT"])
	engines.insert(["zhaobt", "http://www.zhaobt.net/" key "-first-asc-1.html?f=h", "BT"])
	engines.insert(["okbt", "http://www.okbt.net/search/" key, "BT"])
	engines.insert(["bthand", "http://www.bthand.com/search/" key ".html", "BT"])
	engines.insert(["yunpansoso", "http://www.yunpansoso.com/search.html?keyword=" key, "BT"])
	engines.insert(["btmeiju", "http://www.btmeiju.com/ustv_search.htm?title=" key, "BT"]) ;BT美剧
	engines.insert(["bttiantang", "http://www.bttiantang.com/s.php?q=" key, "BT"]) ;BT天堂
	; --资源解析--
	engines.insert(["Down", "C:\Program Files\Thunder Network\Thunder\Program\Thunder.exe " Clipboard]) ;迅雷下载
<<<<<<< HEAD
	engines.insert(["Down:flvcd", "http://www.flvcd.com/parse.php?format=&kw=" Clipboard, "getvideo"]) ;硕鼠视频解析
	engines.insert(["Down:Youtube", "D:\Solomon Xie\Workspace\Gists\youtubeDownload.py"]) ;Python下载Youtube视频
	engines.insert(["Down:You1", "http://en.savefrom.net/#url=" Clipboard]) ;国外网站视频解析
	engines.insert(["Down:You2", "http://savemedia.com/watch?v=" Clipboard, "getvideo"]) ;国外网站视频解析
=======
	engines.insert(["Down:You1", "http://en.savefrom.net/#url=" Clipboard]) ;国外网站视频解析
	engines.insert(["Down:You2", "http://savemedia.com/watch?v=" Clipboard, "getvideo"]) ;国外网站视频解析
	; engines.insert(["Down:Youtube", "D:\Workspace\Gists\youtubeDownload.py"]) ;Python下载Youtube视频
	engines.insert(["flvcd", "http://www.flvcd.com/parse.php?format=&kw=" Clipboard, "getvideo"]) ;硕鼠视频解析
>>>>>>> 8b89f0bff70abecb288bdfba81f0c11aa5ec6626
	; --在线课程--
	engines.insert(["jikexy", "http://search.jikexueyuan.com/course/?q=" key, "cnCourse"]) ;极客学院搜索
	engines.insert(["guoke", "http://mooc.guokr.com/search/?wd=" key, "cnCourse"]) ;果壳MOOC：各平台综合搜索
	engines.insert(["Gkk", "http://c.open.163.com/search/search.htm?query=" key, "cnCourse"]) ;网易公开课
	engines.insert(["Ykt", "http://study.163.com/search.htm?p=" key, "cnCourse"]) ;网易云课堂
	engines.insert(["yunlu", "http://yun.lu/student/course/list/0?q=" key, "cnCourse"]) ;云路课堂
	engines.insert(["Chuanke", "http://www.chuanke.com/course/_" key "_____.html", "cnCourse"])
	engines.insert(["Udemy", "https://www.udemy.com/courses/search/?price=price-free&q=" key, "enCourse"])
	engines.insert(["Coursera", "https://www.coursera.org/courses?query=" key, "enCourse"])
	engines.insert(["CodeAcademy", "http://cn.bing.com/search?q=site:codeacademy.com+" key, "enCourse"])
	engines.insert(["Lynda", "http://www.lynda.com/search?q=" key, "enCourse"])
	engines.insert(["Courses.com", "http://www.courses.com/s?q=" key, "enCourse"])
	engines.insert(["Alison", "https://alison.com/search/result/?q=" key, "enCourse"])
	; --代理服务器--
	engines.insert(["myip", "http://ip.cn/"]) ;查询本机的公网IP
	engines.insert(["duotai", "https://duotai.org/login"]) ;多态网ZPN（全平台提供PAC自动配置代理的脚本）
	engines.insert(["kjson", "https://www.kjson.com/proxy/", "ips"]) 
	engines.insert(["ip1", "http://proxy.ipcn.org/proxylist.html", "ips"]) 
	engines.insert(["ip2", "http://proxy.goubanjia.com/free/", "ips"]) 
	engines.insert(["ip3", "http://www.kuaidaili.com/", "ips"])
	engines.insert(["ip4", "http://www.xicidaili.com/", "ips"]) 
	engines.insert(["ip5", "http://proxylist.hidemyass.com/", "ips"])
	engines.insert(["ip6", "https://nordvpn.com/free-proxy-list/", "ips"])
	engines.insert(["ip7", "https://incloak.com/proxy-list/", "ips"])
	engines.insert(["ip8", "http://ip.izmoney.com/", "ips"])
	engines.insert(["ip9", "http://ip.qiaodm.com/", "ips"])
	engines.insert(["ip10", "http://www.mayidaili.com/", "ips"])
	engines.insert(["ip11", "http://www.fengyunip.com/free/foreign-high.html", "ips"])
	; --IT文章搜索--
	engines.insert(["JianShu", "http://www.jianshu.com/search?q=" key, "it"]) ;简书
	engines.insert(["Zhihu", "https://www.zhihu.com/search?type=question&q=" key, "it"]) ;知乎
	engines.insert(["Weixin", "http://weixin.sogou.com/weixin?type=2&query=" key, "it"]) ;微信文章搜索
	engines.insert(["sef", "http://segmentfault.com/search?q=" key, "it"]) ;segmentfault
	engines.insert(["sof", "http://cn.bing.com/?q=site:stackoverflow.com+" key, "it"]) ;Stackoverflow
	engines.insert(["jikett", "http://geek.csdn.net/search/" key, "it"]) ;极客头条
	engines.insert(["otf", "http://outofmemory.cn/search?q=" key, "it"]) ;内存溢出
	engines.insert(["TouTiao", "http://toutiao.io/search?q=" key, "it"]) ;开发者头条
	engines.insert(["CSDN", "http://so.csdn.net/so/search/s.do?t=blog&q=" key, "it"]) ;csdn
	engines.insert(["xtjj", "http://cn.bing.com/?q=site:gold.xitu.io+" key, "it"]) ;稀土掘金
	engines.insert(["cnHackerNews", "http://cn.bing.com/?q=site:news.dbanotes.net+" key, "it"]) ;中国版HackerNews
	engines.insert(["V2EX", "http://cn.bing.com/?q=site:v2ex.com/t+" key, "it"]) ;V2EX
	engines.insert(["RunOob", "http://www.runoob.com/?s=" key, "it"]) ;菜鸟教程
	engines.insert(["4byte", "http://www.4byte.cn/q?wd=" key, "it"]) ;字节技术
	engines.insert(["Gbtags", "http://www.gbtags.com/gb/search.htm?source=gbtags&s=" key, "it"]) ;极客标签
	engines.insert(["GitSearch", "https://github.com/search?q=" key, "it"]) ;Github搜索
	engines.insert(["Github", "https://github.com/"]) ;Github
	; --Wordpress文章搜索--
	engines.insert(["WPseek", "https://wpseek.com/function/" key "/", "wp"])
	engines.insert(["wp1", "http://cn.bing.com/search?q=site:wpdaxue.com " key, "wp"])
	engines.insert(["wp2", "http://cn.bing.com/search?q=site:codex.wordpress.org " key, "wp"])
	engines.insert(["wp3", "http://cn.bing.com/search?q=site:cn.wordpress.org " key, "wp"])
	engines.insert(["wp4", "http://cn.bing.com/search?q=site:wpjam.com " key, "wp"])
	engines.insert(["wp5", "http://cn.bing.com/search?q=site:dglives.com " key, "wp"])
	engines.insert(["wp6", "http://cn.bing.com/search?q=site:themepark.com.cn " key, "wp"])
	engines.insert(["wp7", "http://cn.bing.com/search?q=site:solagirl.net " key, "wp"])
	engines.insert(["wp8", "http://cn.bing.com/search?q=site:wpnoob.cn " key, "wp"])
	engines.insert(["wp9", "http://cn.bing.com/search?q=site:wordpress.stackexchange.com " key, "wp"])
	engines.insert(["wp10", "http://cn.bing.com/search?q=site:2zzt.com " key, "wp"])
	engines.insert(["wp12", "http://cn.bing.com/search?q=site:wpcourse.com " key, "wp"])
	engines.insert(["wp13", "http://cn.bing.com/search?q=site:themelab.com " key, "wp"])
	engines.insert(["wp14", "http://cn.bing.com/search?q=site:qianduanblog.com " key, "wp"])
	engines.insert(["wp15", "http://cn.bing.com/search?q=site:fellowtuts.com " key, "wp"])
	; --IT优秀博客文章搜索--
	engines.insert(["itBlog1", "http://cn.bing.com/search?q=site:leixuesong.cn " key, "itBlog"])
	engines.insert(["itBlog2", "http://cn.bing.com/search?q=site:williamlong.info " key, "itBlog"])
	engines.insert(["itBlog3", "http://cn.bing.com/search?q=site:crifan.com " key, "itBlog"])
	engines.insert(["itBlog4", "http://cn.bing.com/search?q=site:xiaoxia.org " key, "itBlog"])
	engines.insert(["itBlog5", "http://cn.bing.com/search?q=site:cuiqingcai.com " key, "itBlog"])
	engines.insert(["itBlog6", "http://cn.bing.com/search?q=site:blog.csdn.net/wxg694175346/ " key, "itBlog"])
	engines.insert(["itBlog7", "http://cn.bing.com/search?q=site:ruanyifeng.com " key, "itBlog"])
	engines.insert(["itBlog8", "http://cn.bing.com/search?q=site:findingsea.github.io " key, "itBlog"])
	engines.insert(["itBlog9", "http://cn.bing.com/search?q=site:liujiacai.net " key, "itBlog"])
	engines.insert(["itBlog10", "http://cn.bing.com/search?q=site:codemacro.com " key, "itBlog"])
	engines.insert(["itBlog11", "http://cn.bing.com/search?q=site:imcn.me/html/ycategory/applications " key, "itBlog"])
	engines.insert(["itBlog12", "http://cn.bing.com/search?q=site:webres.wang " key, "itBlog"])
	engines.insert(["itBlog13", "http://cn.bing.com/search?q=site:blogdaren.com " key, "itBlog"])
	engines.insert(["itBlog14", "http://cn.bing.com/search?q=site:coolshell.cn " key, "itBlog"])
	engines.insert(["itBlog15", "http://cn.bing.com/search?q=site:cnblogs.com/xing901022/ " key, "itBlog"])
	engines.insert(["itBlog16", "http://cn.bing.com/search?q=site:xlzd.me " key, "itBlog"])
	engines.insert(["itBlog17", "http://cn.bing.com/search?q=site:soulteary.com " key, "itBlog"])
	engines.insert(["itBlog18", "http://cn.bing.com/search?q=site:4byte.cn " key, "itBlog"])

	if (gp = "") {
		loop % engines.MaxIndex()
			if (engines[A_Index][1] = eg)
				return engines[A_Index][2]
	} else {
		retu := []
		loop % engines.MaxIndex()
			if (engines[A_Index][3] = gp)
				retu.insert(engines[A_Index][2])
		return retu
	}
}

SelText() {
	tmp = %ClipboardAll% ; save clipboard
	Clipboard := "" ; clear clipboard
	Send, ^c ; simulate Ctrl+C (=selection in clipboard)
	ClipWait, 0, 1 ; wait until clipboard contains data
	selection = %Clipboard% ; save the content of the clipboard
	Clipboard = %tmp% ; restore old content of the clipboard
	return selection
}

Explorer(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
; === 文件夹 ===
#IfWinActive, ahk_exe Explorer.EXE
{
	; +C::
	Return
}

Foxit(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
; === Foxit阅读器 ===
#IfWinActive, ahk_class classFoxitReader
{
	F12::Send {Alt}R ;打开注释菜单
	Return
}

Chrome(){
	;(代码糖，用来在Ctrl+R快速跳转)
} 
; === Chrome浏览器 ===
#IfWinActive, ahk_exe chrome.exe
{
	^B::Send +^O ;-- 书签管理器 --
	^E::Send !es ;-- 浏览器设置 --
	; ^Y:: Run % Sites("SaveFrom", Clipboard) ; 最近不稳定所以先不设为默认了
	^Y:: Run % Sites("Down:You1", Clipboard) ;必须复制视频的ID来解析
	Insert::Send {AppsKey}P ;-- 打印选中文字 --
	F1:: Run % Sites( "Bing", SelText() ) ;---搜索选中文字---
	Return
}

QQPlayer(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
; === QQ影音播放器 ===
#IfWinActive, ahk_exe QQPlayer.exe
{
	; 
	Return
}

Sublime(){
	;(代码糖，用来在Ctrl+R快速跳转)
}
; === Sublime Text 3 ===
#IfWinActive, ahk_exe sublime_text.exe
{
	F12::^+P  ;Ctrl+Alt+P打开控制面板太麻烦了
	Return
}