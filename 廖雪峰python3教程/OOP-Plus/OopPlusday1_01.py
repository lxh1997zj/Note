# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# ***1.当子类定义中没有__slots__时，父类的__slots__对子类不起作用。子类实例想加什么属性就加什么属性***
# ***2.当子类定义中有__slots__时，父类的__slots__会对子类起作用。子类会继承父类的__slot__，那么子类实例能加的属性就是父类__slots__和子类本身__slots__规定的属性了。***

# 1.python支持动态给类和实例增加属性和方法；
# 2.python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。
# 3.将方法绑定给类后，类和实例都可以调用和访问属性与方法，这不受__slots__范围限制
# 4.方法没有绑定给类而直接绑定给实例时，需要在__slots__规定范围中加入该方法和方法中的属性
class Student(object):
	__slots__ = ('name','age','set_age','score')
	pass
s = Student()

# 动态给实例增加属性
s.name = 'Michael'
print(s.name)

# 动态给实例增加方法和属性
def set_age(self,age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

# 动态给类增加属性
Student.gender = 'male'
print(Student.gender)
print(s.gender)

# 动态给类增加方法和属性
def set_score(self,score):
	self.score = score
Student.set_score = set_score
s.set_score(66)
print(s.score)
Student.set_score(Student,12)
print(Student.score)