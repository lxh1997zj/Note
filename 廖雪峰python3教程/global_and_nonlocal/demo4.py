# !/usr/bin/env python3
# -*- coding:utf-8 -*-
def scope_test():
	def do_local():
		spam = 'local spam'
	def do_nonlocal():
		nonlocal spam
		spam = 'nonlocal spam'
	def do_global():
		global spam
		spam = 'global spam'
	spam = 'test spam'
	do_local()
	print('After local assignmane:',spam)
	do_nonlocal()
	print('After nonlocal assignmane:',spam)
	do_global()
	print('After global assignmane:',spam)
scope_test()
print('In global scope:',spam)