# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

def make_counter():
	count = 0
	def counter():
		nonlocal count
		count += 1
		return count
	return counter
def make_counter_test():
	mc = make_counter()
	print(mc())
	print(mc())
	print(mc())
make_counter_test()
