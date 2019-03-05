# !/usr/bin/env python3
# -*- coding:utf-8 -*-

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consumer %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)  # 和next(c)类似都是启动生成器，作为预激协程，让协程向前执行到第一个yield表达式，第一次发送必须参数是None，不然没有yiled参数可以给它赋值
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] Producing %s...' % n)
        r = c.send(n)         # 给yield赋值，并返回下一个yield的值
        print('[PRODUCE] Consumer return: %s...' % r)
    c.close()

c = consumer()
produce(c)
