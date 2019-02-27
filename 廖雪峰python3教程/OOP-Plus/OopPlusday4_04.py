# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'__call__():直接对实例进行调用,思考题为__getattr__()和__call__()的结合使用'
# method one
class Chain1(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,attr):
		return Chain1('%s/%s' % (self._path,attr))
	def __str__(self):
		return self._path
	__call__ = __getattr__
	__repr__ = __str__
print(Chain1().status.user.timeline.list1)
print(Chain1().users('michael').repos)
print(Chain1().users.repos)

# method two
class Chain2(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,attr):
		if attr == 'users':
			return lambda x: Chain2('%s/%s/%s' % (self._path,attr,x))
		else:
			return Chain2('%s/%s' % (self._path,attr))
	def __str__(self):
		return self._path
print(Chain2().status.user.timeline.list2)
print(Chain2().users('Lisa').repos)

# method three
class Chain3(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        if type(path) != str:
            raise TypeError('path must be str')
        return Chain3('%s/%s' % (self._path, path))
    __call__ = __getattr__
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain3().status.user.timeline.list3)
print(Chain3().users('Jack').repos)
print(Chain3().users.repos)