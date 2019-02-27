# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'列出当前目录及子目录下的全部文件和目录绝对地址'
'''
os.path.sep:路径分隔符 linux下就用这个了’/’
os.path.altsep: 根目录
os.path.curdir:当前目录
os.path.pardir：父目录
os.path.abspath(path)：绝对路径
os.path.join(): 常用来链接路径
os.path.split(path): 把path分为目录和文件两个部分，以列表返回
'''
import os

def scanDir(path=os.curdir):  # os.curdir:当前目录
	path = os.path.realpath(path)
	filelist = []
	for item in os.listdir(path):
		item = os.path.join(path,item)
        # @todo 查找、过滤等
		if os.path.isdir(item):
		    filelist += scanDir(item)
		else:
			filelist.append(item)
	return filelist
print(scanDir())