# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
def findfile(key,path=os.curdir): # os.curdir:当前文件路径，相当于 '.'
	dirlist = [path]
	while len(dirlist):
		for x in os.listdir(dirlist[0]):
			xPath = os.path.join(dirlist[0],x)
			if os.path.isdir(xPath):
				dirlist.append(xPath)
			elif x.find(key) != -1:
				print('Found file at:',xPath)
		dirlist.pop(0)
findfile('IOday')