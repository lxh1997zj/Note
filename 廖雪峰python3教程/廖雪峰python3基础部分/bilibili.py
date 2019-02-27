# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class Bilibili(object):
    def __init__(self,L,n):
        self.n = n
        self.L = L
    def listsort(self):
        if len(str(self.L)) < 3:
            print(ValueError)
        else:
            for i in list(str(self.L)):
                a = list(str(self.L)).index(i)
                L1 = list(str(self.L)).pop(a)
            for j in L1:
                b = list(L1).index(j)
                L2 = list(L1).pop(b)
            for k in L2:
                if i + j + k == self.n:
                    return True
        return False
lisa = Bilibili(12345,10)
print(lisa.listsort())
