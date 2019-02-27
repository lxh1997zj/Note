# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Foo(object):
	price = 50
	def __new__(cls,*agrs,**kwds):
		inst = object.__new__(cls,*agrs,**kwds)
		print(inst)
		return inst
	def how_much_of_book(self,n):
		print(self)
		return self.price * n
foo = Foo()
print(foo.how_much_of_book(8))
# <__main__.Foo object at 0x000001B7FF855F98>
# <__main__.Foo object at 0x000001B7FF855F98>
# 400