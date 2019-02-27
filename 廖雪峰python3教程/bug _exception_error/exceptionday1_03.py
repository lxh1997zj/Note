# !/usr/bin/env python3
# -*- coding:utf-8 -*-

def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise

bar()

'''
try:
	10/0
except ZeroDivisionError:
	raise ValueError('input error!')
# During handling of the above exception, another exception occurred:
# 在处理上述异常期间，发生了另一个异常：
'''