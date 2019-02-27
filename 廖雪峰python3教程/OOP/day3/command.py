# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 首先你有一个command.py文件，内容如下，这里我们假若它后面还有100个方法

class MyObject(object):
	def __init__(self):
		self.x = 9
	def add(self):
		return self.x + self.x
	def pow(self):
		return self.x * self.x
	def sub(self):
		return self.x - self.x
	def div(self):
		return self.x / self.x
		