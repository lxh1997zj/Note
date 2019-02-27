# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'程序还有bug!'
# 用装饰器实现参数检查,url = 'https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/0015408618648318b3c85972ad149dc8854c4525b082f94000'


import functools, unittest

def check_score(func):
    @functools.wraps(func)
    def wrapper(args,*kw):

    # print(args[0].score)
       
        if not 0 <= args[0].get_score() <= 100:
            raise ValueError('Except 0 <= score <= 100')
        return func(*args, **kwargs)
    # return 'Check over'
    return wrapper

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

   

    def __getitem__(self,n):
        return self.score

    @check_score
    def get_grade(self):
        if self.score < 60:
            return 'C'
        elif self.score < 80:
            return 'B'
        else:
            return 'A'

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


