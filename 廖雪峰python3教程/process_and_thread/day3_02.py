# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
from threading import local, Thread

localinfo = local()

def printName():
    n = 10
    while n > 0:
        print('thread %s >>> %s >>> %d' % (threading.current_thread().name,localinfo.name,n))
        n -= 1

def run(name):
    localinfo.name = name
    printName()

t1 = Thread(target=run,args=('yangboy',))
t2 = Thread(target=run,args=('hannah',))
t1.start()
t2.start()
t1.join()   # 操作系统会在t1和t2线程间不断切换,输出顺序会乱,建议改成串行
t2.join()
