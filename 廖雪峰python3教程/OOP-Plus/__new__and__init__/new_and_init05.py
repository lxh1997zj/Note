# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'come from : http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example'
class Metaclass(type):
	def __new__(meta,name,bases,dct):
		print('-----------------------------------')
		print('Allocating memory for class',name)
		print(meta)
		print(bases)
		print(dct)
		return super(Metaclass,meta).__new__(meta,name,bases,dct)
	def __init__(cls,name,bases,dct):
		print('-----------------------------------')
		print('Initializing class',name)
		print(cls)
		print(bases)
		print(dct)
		super(Metaclass,cls).__init__(name,bases,dct)
class Myclass(object,metaclass=Metaclass):	
	def foo(self,param):
		# print(param)
		return param  # 原文为print(param),但会因为没有return语句返回None,所以改成return,就只返回helllo.
p = Myclass()
print(p.foo('hello'))

'''
结果:
-----------------------------------
Allocating memory for class Myclass
<class '__main__.Metaclass'>
(<class 'object'>,)
{'__module__': '__main__', '__qualname__': 'Myclass', 'foo': <function Myclass.foo at 0x000002206CC23510>}
-----------------------------------
Initializing class Myclass
<class '__main__.Myclass'>
(<class 'object'>,)
{'__module__': '__main__', '__qualname__': 'Myclass', 'foo': <function Myclass.foo at 0x000002206CC23510>}
hello
'''