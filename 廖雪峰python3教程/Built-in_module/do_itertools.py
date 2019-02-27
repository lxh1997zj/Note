# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'itertools提供了非常有用的用于操作迭代对象的函数'

import itertools

def pi(N):  # 方法一
    # 计算pi的值
    res = 0
    j = 0
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x : x <= 2 * N - 1, natuals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in ns:
        i = pow(-1, j) * 4 / i
        j += 1
        res = res +i
    # step 4: 求和:
    return res
'''
def pi(N): # 方法二
    res = 0
    j = 1
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x : x <= 2*N-1, natuals)
    for i in ns:
        if j % 2 == 0:
            i = -4 / i 
        else:
            i = 4 / i
        j += 1
        res = res + i
    return res
'''

'''
def pi(N):  # 方法三
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x : x <= 2*N-1, natuals)
    cs =itertools.cycle([4,-4])
    sum=0                       # 可用list()转换为列表
    for d, n in zip(cs, ns):    # zip([iterable, ...]) 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
        sum += d / n
    return sum
'''

'''
def pi(N):   # 方法四
    OddNumber = itertools.count(1, 2)
    OddNumberN = itertools.takewhile(lambda x: x <= 2*N-1, OddNumber)
    p = []
    ItCy = itertools.cycle([4, -4])
    for ONN in OddNumberN:
        p.append(next(ItCy) / ONN)   # next() 返回迭代器的下一个项目
    return sum(p)            # sum(iterable[, start]) 后面的start默认为0,指前面可迭代对象相加完后再加上start
'''

'''
def pi(N):  # 方法五
    odds = itertools.count(start=1, step=2)
    odds_N = list(itertools.takewhile(lambda x: x <= 2 * N - 1, odds))
    odds_N_4 = [pow(-1, i) * 4 / v for i, v in enumerate(odds_N)]    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    return sum(odds_N_4)                                        # enumerate(sequence, [start=0]) start为下标起始位置,用for循环输出后,一般下标在前,对象在后
'''

'''
def pi(N):  # 方法六
    ls = itertools.count(1,2)
    ls_N = list(itertools.takewhile(lambda x : x<=2*N,ls))
    for i in range(N):
        if(i&1):                   # '&'二进制下运算,偶数为0,奇数为1
            ls_N[i] = -4/ls_N[i]
        else:
            ls_N[i] = 4/ls_N[i]
    return sum(ls_N)
'''

''' 
def pi(N):  # 方法六
    return sum(i/j for i, j in zip(itertools.cycle([4, -4]), itertools.takewhile(lambda x: x <= N*2-1, itertools.count(1, 2))))
'''

# 测试
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')