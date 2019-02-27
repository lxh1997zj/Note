# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'FIFO'
# 具体可以思路参考url="https://blog.csdn.net/lilong117194/article/details/76252057"

from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpdateOrderedDict, self).__init__()
        # super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0  # 检查要添加的key是否在self中
        print('self1:',self)
        print('len(self):',len(self))
        # 如果dict容量已满
        if len(self) - containsKey >= self._capacity:
            print('%s(len(self)) - %s(containskey) >= %s(self._capacity)' % (len(self),containsKey,self._capacity))
            # 则删除最先添加的key
            last = self.popitem(last=False) # last=true用LIFO,last=false采用FIFO,help(OrderedDict.popitem)原文: Pairs are returned in LIFO order if last is true or FIFO order if false.
            print('remove:',last)
            print('self2:',self)
        # 检查dict里是否已经存在要增加的(key,value)中的key
        if containsKey:
            # 删除原来的key
            del self[key]
            print('set:',(key,value))
            print('self3:',self)
        # 如果dict中没有要添加的key
        else:
            print('add:',(key,value))
            print('self4:',self)
        OrderedDict.__setitem__(self,key,value)
        print('self5:',self)

# 测试
l = LastUpdateOrderedDict(2)
l['a'] = 1
print('.....................')
l['b'] = 2
print('.....................')
l['c'] = 3
print('.....................')
l['b'] = 6
print('.....................')
print(l)
