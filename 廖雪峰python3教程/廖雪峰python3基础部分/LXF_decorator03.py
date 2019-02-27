# -*- coding:utf-8 -*-
import functools
def log(*nub):  # 可变参数即可满足
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'%(nub,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
# 测试
@log('真香啊')
def now():
	print('2018-10-5')
now()
