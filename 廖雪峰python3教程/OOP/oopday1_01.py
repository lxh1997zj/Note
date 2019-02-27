# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

lisa = Student('Lisa',99)
jack = Student('Jack',89)
bart = Student('Bart',59)
print('%s: %s' % (lisa.name,lisa.get_grade()))
print('%s: %s' % (jack.name,jack.get_grade()))
print('%s: %s' % (bart.name,bart.get_grade()))
print(lisa.name,lisa.get_grade())
print(jack.name,jack.get_grade())
print(bart.name,bart.get_grade())
'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
'''