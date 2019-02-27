# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 声明全局变量，如果在局部要对全局变量修改，需要在局部也要先声明该全局变量：

gcount = 0
def global_test():
	global gcount
	gcount += 1
	print(gcount)
global_test()