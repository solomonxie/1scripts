# coding:utf-8
'''
	# 快速把指定文件夹(双击文件时则为本文件夹)的所有文件夹及其中所有文件的镜像
	# 而镜像就是：文件夹还是文件夹，文件则只以文件名创建txt文件
	# 这样的备份其实比较划算：什么都可以从网上下载，不用非得源文件保存
	# txt文件不光保留文件名 内容中还可以记录文件属性信息
'''
import os, sys, time, getopt

def main():
	# ====== 获取指定路径 =======
	opts, args = getopt.getopt(sys.argv[1:], 'p:n', ['path=', 'null'])
	path, null = '', False
	for o, a in opts:
		if   o == '-p' or o == '--path': path = a
		elif o == '-n' or o == '--null': null = True
	if not path: path = os.getcwd() # 如果没有指定目录则制作当前目录镜像
	# ====== 制作镜像 ============
	for root, subdir, files in os.walk(path, topdown=True):
		mir = root.replace( path, path+'(Mirror at %s)'%time.strftime('%Y-%m-%d') )
		if not os.path.exists(mir): os.mkdir(mir) # 创建镜像文件夹
		for name in files:
			try:
				# 将详细文件记录在txt文件中
				details  = '' if null else root+'\\'+name + '\n' + str(os.stat(root+'\\'+name))
				with open(mir+'\\'+name+'.txt', 'w') as f:
					f.write(details)
			except Exception as e:
				# 将出错文件记录到txt文件中以供参考
				print e
				with open(path+'\\errors.txt', 'a') as f:
					f.write('\n'+str(e)+'\n')
				continue

if __name__ == '__main__':
	main()