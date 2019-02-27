# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径.'
# url1 = 'http://www.runoob.com/python3/python3-os-path.html'
# url2 = 'http://www.runoob.com/python3/python3-string-find.html'

# 导入os模块
import os
# 定义查找指定文件名的函数：第一参数是要查找的指定文件名，第二个参数是查找的路径，默认参数是当前目录
def findfile(path,s):
    # 遍历当前目录里面的所有文件和文件夹
	for x in os.listdir(path):
	    # 获取每个文件和文件夹的路径 
		xpath = os.path.join(path,x)
		# 判断是文件还是文件夹（目录）
		if os.path.isdir(xpath):
			# 如果是文件夹（目录），则继续查找（这里使用了递归！不过递归有个缺点，如果目录深度太大，容易造成内存溢出）
			findfile(xpath,s)
		elif x.find(s) != (-1):   # str.find(str, beg=0, end=len(string)):如果包含子字符串返回开始的索引值，否则返回-1
		    # 如果是文件，并且包含指定文件名，则打印其文件相对路径
			# print('文件名：%s' % os.path.basename(xpath))
			
			# print('%s' % os.path.basename(xpath))    # 文件名称
			print('%s' % os.path.relpath(xpath))       # 相对路径

# 使用函数
findfile('E:\\Python代码练习\\廖雪峰python3教程','IOday')
