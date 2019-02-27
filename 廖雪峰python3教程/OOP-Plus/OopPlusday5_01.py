# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from enum import Enum,unique
# Gender = Enum('Gender',('Male','Female')) # 方法二
@unique
class Gender(Enum):
	Male = 0
	Female = 1
class Student(object):
	def __init__(self,name,gender):
		self.name = name
		if not isinstance(gender,Gender):
			raise TypeError('gender must be in Gender !')
		self.gender = gender
# 测试
bart = Student('Bart',Gender.Male)
print(bart.name,bart.gender)
if bart.gender == Gender.Male:
	print('测试通过!')
else:
	print('测试失败!')

