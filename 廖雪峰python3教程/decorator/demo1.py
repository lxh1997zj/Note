# !/usr/bin/env pthon3
# -*- coding:utf-8 -*-
def dec1(func):
	print('1111')
	def one():
		print('2222')
		func()
		print('3333')
	return one

def dec2(func):
	print('aaaa')
	def two():
		print('bbbb')
		func()
		print('cccc')
	return two
@dec1
@dec2
def test():
	print('test test')

test()