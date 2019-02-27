# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 问题来源 url = 'https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/0015211025952478c78b30b055d42728c9083ed02ce1481000'
# 参考url = 'http://blog.51cto.com/wangwei007/1104940'
import os,sys,pdb
l = []
def findFile(filename,dir='.'):
	for d in os.listdir(dir):
		subDir = os.path.join(os.path.abspath(dir),d)
		if os.path.isdir(d):
			findFile(filename,subDir)
		elif filename in d:
			l.append(subDir)
findFile('logging')
print(l)