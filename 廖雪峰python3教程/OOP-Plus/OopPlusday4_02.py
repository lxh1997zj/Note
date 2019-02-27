# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'__getitem__():让class有类似按下标访问数列和slice(切片)的特性'
'''
self.a, self.b = 0, 1
相当于 
tuple = (0, 1)
self.a = tuple[0]
self.b = tuple[1]
'''
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int): # n是索引
			a,b = 1,1
			for i in range(n):
				a,b =b,a+b
			return a
		if isinstance(n,slice): # n是切片(slice)
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
# 测试
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])
print(f[0:5])
print(f[:10])
print(f[:10:2])
'''
切片的概念：
class slice(stop)
class slice(start,stop[,step])
start--起始位置
stop--结束位置
step--间距

参考-url = 'http://www.runoob.com/python/python-func-slice.html'
'''