# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Student(object):
	pass
def set_age(self,age):
	self.age = age
from types import MethodType

#给实例增加属性
s1 = Student()
s1.set_age = MethodType(set_age, s1)
s1.set_age(11)
print(s1.age) #11

# 给类增加属性一
Student.set_age = MethodType(set_age,Student)
Student.set_age(22)
print(Student.age)
s2 = Student()
s3 = Student()
s2.set_age(33)
print(s2.age)
s3.set_age(44)
print(s2.age,s3.age) # 为什么是两个44？

# 给类增加属性二
Student.set_age = set_age
Student.set_age(Student,55)
print(Student.age)
s4 = Student()
s5 = Student()
s4.set_age(66)
s5.set_age(77)
print(s4.age,s5.age)
