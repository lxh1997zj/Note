# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Foo(object):
	def __new__(cls,*agrs,**kwds):
		inst = object.__new__(cls,*agrs,**kwds)
		print(inst)
		return inst
	def __init__(self,price=50):
		self.price = price
	def how_much_of_book(self,n):
		print(self)
		return self.price * n
foo = Foo()
print(foo.how_much_of_book(8))
# <__main__.Foo object at 0x0000019DCAB85F60>
# <__main__.Foo object at 0x0000019DCAB85F60>
# 400