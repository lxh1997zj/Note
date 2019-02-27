# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Inch(float):
	'Convert from inch to meter'
	def __new__(cls,arg=0.0):
		return float.__new__(cls,arg*0.0254)
print(Inch(12))