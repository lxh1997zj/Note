# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 然后我们有一个入口文件 exec.py，要根据用户的输入来执行后端的操作
from command import MyObject
computer = MyObject()
def run():
	inp = input('method>')

	if inp == 'add':
		print(computer.add())
	elif inp == 'sub':
		print(computer.sub())
	elif inp == 'div':
		print(computer.div())
	elif inp == 'pow':
		print(computer.pow())
	else:
		print('404')
if __name__ == '__main__':
	run()