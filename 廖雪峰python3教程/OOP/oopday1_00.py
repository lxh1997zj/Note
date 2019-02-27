# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的.
class Student(object):  # 类名通常要大写!

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self,a): # 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入。
		print('%s: %s %s' % (self.name,self.score,a))


bart = Student('Bart Simpson',59)
bart.print_score('真辣鸡啊!')