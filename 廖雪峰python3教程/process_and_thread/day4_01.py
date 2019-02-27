# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

l = threading.Lock()

def show(num):
    print(threading.current_thread().getName(),num)

def thread_cal():
    local_num = 0
    for _ in range(1000):
        l.acquire()
        local_num += 1
        l.release()
    show(local_num)

threads = []
for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()
for i in range(10):
    threads[i].join()




