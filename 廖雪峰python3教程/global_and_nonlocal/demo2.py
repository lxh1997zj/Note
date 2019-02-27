# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 在局部如果不声明全局变量，并且不修改全局变量。则可以正常使用全局变量：

gcount = 0
def global_test():
	print(gcount)
global_test()