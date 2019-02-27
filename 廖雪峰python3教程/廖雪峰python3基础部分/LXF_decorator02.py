# -*- coding:utf-8 -*-
# 同时支持有参数和无参数的装饰器
import functools
def log(text):
	if isinstance(text,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():'%(text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decorator
	else:
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('call %s():'%text.__name__)
			return text(*args,**kw)
		return wrapper
# 测试
@log('真香啊')	
def now():
	print('2018-10-5')
now()
print(now.__name__)
@log
def now():
	print('2018-10-5')
now()
print(now.__name__)