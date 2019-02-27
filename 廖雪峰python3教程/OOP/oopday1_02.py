# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student():
	name = 'dana'
	age = 18
	def say(self):
		
		self.name = 'aaa'
		self.age = 200
		print('my name is {0}'.format(self.name))
		print('my age is {0}'.format(self.age))
	def sayAgain(s):

		print('my name is {0}'.format(s.name))
		print('my age is {0}'.format(s.age))

yueyue = Student()
yueyue.say()
yueyue.sayAgain()
