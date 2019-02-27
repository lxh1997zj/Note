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
		print('B foo')
	def bar(self):
		print('B bar')

class C1(A):
	def bar(self):
		print('C1-bar')

class C2(B):
	def bar(self):
		print('C2-bar')

class D(C1,C2):
	pass

if __name__ == '__main__':
	print(D.__mro__)  # __mro__:解析方法调用的顺序
	d = D()
	d.foo()
	d.bar()
'''
找到入度为0的顶点，只有一个D，拿D，剪掉D相关的边
得到两个入度为0的顶点(C1,C2),根据最左原则，拿C1，剪掉C1相关的边，这时候序列为{D,C1}
接着看，入度为0的顶点有两个(A,C1),根据最左原则，拿A，剪掉A相关的边，这时候序列为{D,C1,A}
接着看，入度为0的顶点为C2,拿C2，剪掉C2相关的边，这时候序列为{D,C1,A,C2}
继续，入度为0的顶点为B，拿B，剪掉B相关的边，最后还有一个object
所以最后的序列为{D,C1,A,C2,B,object}
最后，我们执行上面的代码，发现print(D.__mro__)的结果正如上面所计算的结果

最后的最后，python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
'''