# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'__iter__():让一个class用于for循环,并有类似迭代的特点'
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1 # 初始化两个计数器a,b
	def __iter__(self):
		return self         # 实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 100000:  # 退出循环的条件
			raise StopIteration()
		return self.a        # 返回下一个值
# 测试
for n in Fib():
	print(n)