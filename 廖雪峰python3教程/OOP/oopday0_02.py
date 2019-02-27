# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Person(object):
# 这里就是初始化你将要创建的实例的属性
	def __init__(self,hight,weight,age):
		self.hight = hight
		self.weight = weight
		self.age = age
# 定义你将要创建的实例所有用的技能
	def paoniu(self):
		print('你拥有的技能')
	def eat(self):
		print('you can eat')
# 开始创建实例
zhangsan = Person(170,50,29)
lisi = Person(175,100,30)
# 你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()
'''
上帝

class 类 (人)
instance 实例 (你,我,他)
你会有些属性(身高,年龄,体重)
你会有些技能(吃饭,泡妞)

__init__ 方法的主要作用,就是初始化你的属性,
这些属性,在上帝初始化你的时候就要赋予给你,
比如zhangsan = Person(170,29,50)这时上帝就把你创造出来了，
也就是实例化了你，然后，你到底有哪些技能呢，
这就看有没有在类里面定义了，如果有定义泡妞的技能，
那么你就可以调用泡妞的技能来泡妞，大致就是这样吧，看看上面的例子就更清楚了
'''