# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 参考链接 url = 'https://kevinguo.me/2018/01/19/python-topological-sorting/'
class A(object):
	def foo(self):
		print('A foo')
	def bar(self):
		print('A bar')

class B(object):
	def foo(self):
		print('A foo')
	def bar(self):
		print('B bar')

class C1(A,B):
	pass

class C2(A,B):
	pass

class D(C1,C2):
	pass

if __name__ == '__main__':
	print(D.__mro__)   # __mro__:解析方法调用的顺序
	d = D()
	d.foo()
	d.bar()
'''
找到入度为0的点，只有一个D，把D拿出来，把D相关的边剪掉
现在有两个入度为0的点(C1,C2)，取最左原则，拿C1，剪掉C1相关的边，这时候的排序是{D,C1}
现在我们看，入度为0的点(C2),拿C2,剪掉C2相关的边，这时候排序是{D,C1,C2}
接着看，入度为0的点(A,B),取最左原则，拿A，剪掉A相关的边，这时候的排序是{D,C1,C2,A}
继续，入度哦为0的点只有B，拿B，剪掉B相关的边，最后只剩下object
所以最后的排序是{D,C1,C2,A,B,object}
我们执行上面的代码，发现print(D.__mro__)的结果也正是这样，而这也就是多重继承所使用的C3算法啦

最后的最后，python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
'''