# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 在函数 add_b 内 global 定义的变量 b，只能在 函数 do_global 内引用， 如果要在 do_global 内修改，必须在 do_global 函数里面声明 global  b ，表明是修改外面的 全局变量 b ：

def add_b():
	global b
	b = 42
	def do_global():
		global b
		b = b + 10
		print(b)
	do_global()
	print(b)
add_b()
print(b)