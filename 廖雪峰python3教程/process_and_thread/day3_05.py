# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

local_school = threading.local()

class myClass(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def process_student():
    std = local_school.student
    print('hello %s in (%s)' % (std,threading.current_thread().name))

def process_student_class():
    myclass = local_school.myclass
    print('my name is %s age %d in (%s)' % (myclass.name,myclass.age,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

def process_thread_class(my):
    local_school.myclass = my
    process_student_class()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
cs3 = myClass('Jack',23)
t3 = threading.Thread(target=process_thread_class,args=(cs3,),name='Thread-C')
cs4 = myClass('Tom',18)
t4 = threading.Thread(target=process_thread_class,args=(cs4,),name='Thread-D')
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print('All thread ended.')
