# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    t = b*b-4*a*c
    if t > 0:
        x1 = (-b + math.sqrt(t))/(2*a)
        x2 = (-b - math.sqrt(t))/(2*a)
        return x1,x2
    elif t == 0:
        x = -b/(2*a)
        return x
    else:
        return

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
