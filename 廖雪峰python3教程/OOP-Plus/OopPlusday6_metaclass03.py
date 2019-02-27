# !/usr/bin/env python3
# -*- coding:utf-8 -*-
print('-----'*10)
class UpperAttrMetaclass(type):
	print('1============')
	def __new__(cls,name,bases,dct):
		print('2==========')
		attrs = ((name,value) for name,value in dct.items() if not name.startswith('__'))
		uppercase_attr = dict((name.upper(),value) for name,value in attrs)
		return type.__new__(cls,name,bases,uppercase_attr)
class Foo(metaclass = UpperAttrMetaclass):
	print('3========')
	bar = 'bip'
f = Foo()
print('-'*100)
print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))
print(dir(f))
