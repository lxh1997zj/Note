# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# global 定义的变量，表明其作用域在局部以外，即局部函数执行完之后，不销毁 函数内部以global定义的变量：

def add_a():
	global a
	a = 3
add_a()
print(a)