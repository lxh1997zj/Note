# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

local = threading.local()
class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def getinfo():
    stu = local.student
    print('this is %s,%d,%d in %s' % (stu.name,stu.age,stu.score,threading.current_thread().name))

def setinfo(name,age,score):
    local.student = Student(name,age,score)
    getinfo()

t1 = threading.Thread(target=setinfo,args=('Alice',25,88),name='Thread-1')
t2 = threading.Thread(target=setinfo,args=('Bob',27,90),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
print('print complete...')

