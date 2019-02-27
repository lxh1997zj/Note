# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from enum import Enum,unique
@unique
class Gender(Enum):
	Male = 0
	Female = 1
class Student(object):
	def __init__(self,name,gender):
		self.name = name
		if type(gender) == Gender:
			self.gender = gender
		else:
			raise ValueError('gender type error')
	def __str__(self):
		return '学生的姓名为:%s,性别为:%s' % (self.name,self.gender)
	__repr__ = __str__
if __name__ == '__main__':
	print(Student('Michael',Gender.Male))
	print(Student('Lily',Gender.Female))
