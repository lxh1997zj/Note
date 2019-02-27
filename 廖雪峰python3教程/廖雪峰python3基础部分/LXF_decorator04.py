# -*- coding:utf-8 -*-
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call %s():'%func.__name__)
		func(*args,**kw)
		print('end call %s():'%func.__name__)
		return func(*args,**kw)  
	return wrapper
# 测试
@log
def now():
	print('2018-10-5')
now()
print(now.__name__)