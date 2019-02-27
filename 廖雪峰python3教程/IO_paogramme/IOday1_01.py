# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'test 文件的读写！'

# 参考url = 'https://blog.csdn.net/u011242657/article/details/64437612'
# fpath = r'E:\Python代码练习\廖雪峰python3教程\IO_paogramme\2.txt'
# fpath = 'E:\\Python代码练习\\廖雪峰python3教程\\IO_paogramme\\2.txt'

fpath = 'E:/Python代码练习/廖雪峰python3教程/IO_paogramme/2.txt'

with open(fpath,'r') as f:
	s = f.read()
	print(s)
