# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下(在Unix，Windows中有效)。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
followlinks -- 设置为 true，则通过软链接访问目录.
该方法没有返回值。

# 举例:
import os
for root,dirs,files in os.walk('.',topdown=True):  # topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
    for name in files:
        print(os.path.join(root,name))
        # print(type(name))  # <class 'str'>
    for name in dirs:
        print(os.path.join(root,name))
        # print(type(name))  # <class 'str'>
'''

import os
# 可选参数目录dir为当前目录,必要参数findstr 为要查找的指定字符串
def FindFile(findstr='',dirpath='.'):
# 创建一个最后文件路径和目录路径的列表
	file_paths = []
	# dir_paths = []  # 没必要!
#使用walk方法,os.walk是个生成器
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
# root 所指的是当前正在遍历的这个文件夹的本身的地址(包含子目录)
# dirs 是一个 list ，内容是该文件夹中所有的目录的名字(包括子目录)
# files 同样是 list , 内容是该文件夹中所有的文件(包括子目录)
	for root,dirs,files in os.walk(dirpath):
		for filename in files:
			if findstr in filename:
				file_paths.append(os.path.join(root,filename))
	return file_paths

print(FindFile('IOday'))
