# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re  # 正则表达式
# url = 'http://www.runoob.com/python3/python3-reg-expressions.html'

def findfile(filePath,keyvalue):
	fs = os.listdir(filePath)
	for f in fs:
		fullpath = os.path.join(filePath,f)
		if os.path.isfile(fullpath):
			if re.search(keyvalue,f):  # 正则表达式
				print(fullpath)
		elif os.path.isdir(fullpath):
			findfile(fullpath,keyvalue)
findfile('.','IOday')