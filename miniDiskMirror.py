# coding:utf-8
'''
    # 快速把指定文件夹(双击文件时则为本文件夹)的所有文件夹及其中所有文件的镜像
    # 而镜像就是：文件夹还是文件夹，文件则只以文件名创建txt文件
    # 这样的备份其实比较划算：什么都可以从网上下载，不用非得源文件保存
    # txt文件不光保留文件名 内容中还可以记录文件属性信息
'''
import os, sys, time, getopt, zipfile

def main():
    # ====== 获取指定路径 =======
    opts, args = getopt.getopt(sys.argv[1:], 'p:n', ['path=', 'null'])
    path, null = '', False
    for o, a in opts:
        if   o == '-p' or o == '--path': path = a
        elif o == '-n' or o == '--null': null = True
    if not path: path = os.getcwd() # 如果没有指定目录则制作当前目录镜像
    # ====== 制作镜像 ============
    fos = [fo for fo in path.split('\\') if fo]
    zipname = '\\'.join(fos[0:-1]) +'\\'+ fos[-1] + '.zip'
    print zipname
    zp = zipfile.ZipFile(zipname, 'w')
    # return
    for root, subdir, files in os.walk(path, topdown=True):
        mir = root.replace( path, path+'(Mirror at %s)'%time.strftime('%Y-%m-%d') )
        if not os.path.exists(mir): os.mkdir(mir) # 创建镜像文件夹
        for name in files:
            try:
                # 将详细文件记录在txt文件中
                details  = '' if null else root+'\\'+name + '\n' + str(os.stat(root+'\\'+name))
                with open(mir+'\\'+name+'.txt', 'w') as f:
                    f.write(details)
                # zp.write(mir.replace(root, '')+'\\'+name+'.txt')
            except Exception as e:
                # 将出错文件记录到txt文件中以供参考
                print e
                with open(path+'\\errors.txt', 'a') as f:
                    f.write('\n'+str(e)+'\n')
                continue
    zp.close()

def archive(folder, dele=True):
    files = os.listdir(folder) # listdir()在接收unicode参数时会返回unicode格式的文件目录
    folder = [fo for fo in folder.split('\\') if fo][-1]
    zipname = folder + '.zip' # 以文件夹名称为zip文件名
    print '%d files to be compressed.' % len(files), files
    z = zipfile.ZipFile(zipname, 'w')
    for f in files:
        z.write(folder+f, folder+'\\'+f)
    z.close()
    if dele: __import__('shutil').rmtree(folder) # 完成后删除原文件夹

if __name__ == '__main__':
    main()