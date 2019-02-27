# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 这样写的话可以实现FIFO,但是加入重复的key会覆盖而不是在末尾加上,所以会改变dict的顺序

from collections import OrderedDict

class fifo_dict(OrderedDict):
    def __init__(self, capacity):
        super(fifo_dict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        if key not in self and len(self) >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)

        super(fifo_dict, self).__setitem__(key, value)

# 测试
l = fifo_dict(2)
l['a'] = 1
print('.....................')
l['b'] = 2
print('.....................')
l['c'] = 3
print('.....................')
l['b'] = 6
print('.....................')
print(l)