# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
def deco(arg = True):
	if arg:
		def _deco(func):
			def wrapper(*args,**kw):
				startTime = time.time()
				func(*args,**kw)
				endTime = time.time()
				msecs = (endTime - startTime) * 1000
				print('->elapsed time: %f ms' % msecs)
			return wrapper
	else:
		def _deco(func):
			return func
	return _deco
@deco(False)
def myFunc():
	print('start myFunc')
	time.sleep(0.6)
	print('end myFunc')
@deco(True)
def addFunc(a,b):
	print('start addFunc')
	time.sleep(0.6)
	print('result is %d' % (a + b))
	print('end addFunc')
print('myFunc.name is:',myFunc.__name__)
myFunc()
print()
print('addFunc.name is:',addFunc.__name__)
addFunc(3,8)
