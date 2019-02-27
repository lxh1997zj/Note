# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value : self.append(value)
		return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
	pass
L = MyList()
print(L)
L.add(1)
print(L)
print('------------------------------')
L2 = list()
print(L2)
# L2.add(1)
# print(L2)

'''
__new__()方法接收到的参数依次是：
1.当前准备创建的类的对象；
2.类的名字；
3.类继承的父类集合；
4.类的方法集合。
'''