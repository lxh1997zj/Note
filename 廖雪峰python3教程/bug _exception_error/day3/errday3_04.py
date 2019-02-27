# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'程序还有bug!'
# 装饰器实现检查分数,url = 'https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/0015398566405381a4542a4747d4e39acb64a8ce720d154000'

import unittest
def checkinput(func):
    def wrapper(*args,**kwargs):
            try:
                for cscore in kwargs.values():
                    if cscore<0 or cscore>100:
                        raise ValueError
                    else:
                        return func(args,**kwargs)
            except ValueError as e:
                print('score should be 0-100')
    return wrapper

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    @checkinput
    def get_grade(self):
    	if self.score >= 80:
    		return 'A'
    	elif self.score >= 60:
    		return 'B'
    	else:
    	    return 'C'



class TestStudent(unittest.TestCase):

	def test_80_to_100(self):
		s1 = Student('Bart',80)
		s2 = Student('Lisa',100)
		self.assertEqual(s1.get_grade(),'A')
		self.assertEqual(s2.get_grade(),'A')

	def test_60_to_80(self):
		s1 = Student('Bart',60)
		s2 = Student('Lisa',79)
		self.assertEqual(s1.get_grade(),'B')
		self.assertEqual(s2.get_grade(),'B')
	def test_0_to_60(self):
		s1 = Student('Bart',0)
		s2 = Student('Lisa',59)
		self.assertEqual(s1.get_grade(),'C')
		self.assertEqual(s2.get_grade(),'C')

	def test_invalid(self):
		s1 = Student('Bart',-1)
		s2 = Student('Lisa',101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()

if __name__ == '__main__':
	unittest.main()
