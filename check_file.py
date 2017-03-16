# Description	: Check a file exists and that we can read the file
# 注释版本 2017-03-16 wangschang
# 使用方法 python3 check_file.py 文件名称
from __future__ import print_function
import sys		# 导入模块
import os		# 导入注释

#定义提示信息
def usage():
    print('读取文件内容')
    print('[+]Usage: python check_file.py <filename1> [filename2] ... [filenameN]')
    exit(0)

#读取文件内容
def readfile(filename):
    with open(filename,'r') as f:
        line = f.read()
    print(line)

#定义主函数
def main():
    if len(sys.argv)>=2:
        filenames = sys.argv[1:]
        #判断是否是文件
        for filename in filenames:
            if not os.path.isfile(filename):
                print('[-] file name '+ filename + ' does not exist')
                filenames.remove(filename)
                continue
            # 判断是否可读
            if not os.access(filename,os.R_OK):
                print('[-] file name ' + filename + ' can not access')
                filenames.remove(filename)
                continue
        #读取文件内容
        for filename in filenames:
            readfile(filename)
    else:
        usage()
#执行主函数
if __name__ == '__main__':
    main()
