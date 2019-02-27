# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# list.extend(seq)  seq:元素列表

import os
def scanfile(paths,files,lists=None):
	lists = []
	try:
		for i in os.listdir(paths):
			x = os.path.join(paths,i)
			if os.path.isfile(x) and (files in os.path.split(i)[1]):
				print(os.path.join(x.split('\\')[-2],os.path.split(x)[1]))
				lists.append(os.path.join(x.split('\\')[-2],os.path.split(x)[1]))
			elif os.path.isdir(x):
				lists.extend(scanfile(x,files))
	except PermissionError as e:
		return lists
	return lists
if __name__ == '__main__':
	paths ='.'
	files = 'IOday'
	qq = scanfile(paths,files)
	print(qq)
