# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

local_student = threading.local()

class Student():
    def __init__(self,id,name,sex):
        self._id = id
        self._name = name
        self._sex = sex
    def stu_to_str(self):
        return 'studentId:' + self._id + ',studentName:' + self._name + ',studentSex:' + self._sex

def set_student(id,name,sex):
    local_student.stu = Student(id,name,sex)

def get_studet(id,name,sex):
    set_student(id,name,sex)
    stu = local_student.stu
    print('hello,%s (in %s)' % (stu.stu_to_str(),threading.current_thread().name))

t1 = threading.Thread(target=get_studet,args=('1608411002','xiaoli','male'),name='Thread-1')
t2 = threading.Thread(target=get_studet,args=('1609411020','xiaoming','female'),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
print('completed')
