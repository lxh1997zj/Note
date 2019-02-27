# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
def deco1(f):
	print('deco1')
	def w():
		print('first start')
		f()
		print('first end')
	return w
def deco2(f):
	print('deco2')
	def w():
		print('second start')
		f()
		time.sleep(1)
		print('second end')
	return w
@deco1
@deco2
def fun():
	print('ding......')
f = fun
f()
'''
deco2
deco1
first start
second start
ding......
second end
first end
'''