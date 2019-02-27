# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 1.python支持动态给类和实例增加属性和方法；
# 2.python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。
# 3.将方法绑定给类后，类和实例都可以调用和访问属性与方法，这不受__slots__范围限制
# 4.方法没有绑定给类而直接绑定给实例时，需要在__slots__规定范围中加入该方法和方法中的属性
class Student(object):
	__slots__ = ('name','age','set_age') # 用slots限制类的实例的属性
	pass
s = Student()

# 动态给实例增加属性
s.name = 'Michael'
print(s.name)

# 动态给类增加属性不受性质
Student.gender = 'male'
print(Student.gender)
print(s.gender)

# 动态给类增加方法和属性
def set_score(self,score): # 如果在__slots__中没有属性score将报lotsAttributeError: 'Student' object has no attribute 'score'
	self.score = score
Student.set_score = set_score # 给类绑定方法和属性不受限制，可以不在__slots__中加set_score和score
Student.set_score(Student,66) # 类调用set_acore方法给自己绑定属性score为66
print(Student.score)
print(s.score) # 实例可以调用类属性scored但是不能用s.set_score(89)来中心赋值
# 不能用s.set_score(89)是因为实例里面没有定义score，但可以动态加入类Student的属性score，虽然实例没有score属性，但Student有就可以直接拿来，所以print(s.score)不会报错
# __slots__中没有score

# 动态给实例增加方法和属性
def set_age(self,age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s) # 直接给实例绑定方法由于类中没有该方法，必须在__slots__中添加set_age, age才可以
s.set_age(25)
print(s.age)

# 动态给类增加方法和属性
Student.set_age = set_age # 给类绑定方法和属性不受限制，可以不在__slots__中加set_score和score
s.set_age(26)      # 但是由于Student类没有调用set_age方法，所以类中没有age的值。实例调用该方法赋值就必须在__slots__中加上age属性了
p = Student()
p.set_age(789)
print(s.age)
print(p.age)


