# -*- coding:utf-8 -*-
def normalize(name):
	return name[0].upper() + name[1:].lower()
# 测试
L1 = ['adam','LISA','BarT']
L2 = list(map(normalize,L1))
print(L2)
