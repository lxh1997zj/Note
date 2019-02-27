# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# from url = 'https://www.zhihu.com/question/271643290/answer/525019532'

from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 +0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() -45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)

bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0) # 如果注释掉这一行可以观看绘画过程，不注释直接得到结果
left(90)
pu()
backward(300)
tree(13, 100)
done()