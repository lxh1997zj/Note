# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Foo(object):
	price = 50
	def how_much_of_book(self,n):
		print(self)
		return self.price * n
foo = Foo()
print(foo.how_much_of_book(8))
print(dir(Foo))