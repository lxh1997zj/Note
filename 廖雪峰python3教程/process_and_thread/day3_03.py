# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'错误程序！'
import threading

local_num = threading.local()

def change_it(n):
    local_num.balance = local_num.balance + n
    local_num.balance = local_num.balance - n
    if local_num.balance != 0:
        print(local_num.balance)

def run_thread(n):
    local_num.balance = 0
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(local_num.balance)
