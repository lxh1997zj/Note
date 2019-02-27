# -*- coding:utf-8 -*-
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call')
		func(*args,**kw)
		print('end call')
		
	return wrapper
# 测试
@log
def now():
	print('2018-10-5')
now()