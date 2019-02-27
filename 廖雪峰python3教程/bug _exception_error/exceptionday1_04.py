# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 源程序
'''
from functools import reduce
def str2num(s):
	return int(s)
def calc(exp):
	ss = exp.split('+')
	ns = map(str2num,ss)
	return reduce(lambda acc,x: acc+x,ns)
def main():
	r = calc('100+200+345')
	print('100+200+345=',r)
	r = calc('99+88+7.6')
	print('99+88+7.6=',r)
main()
'''

from functools import reduce
# 方法一：

def str2num(s):
	try:
		return int(s)
	except ValueError as e:
		return float(s)

# 方法二：
'''
def str2num(s):
	try:
		s = int(s)
	except ValueError as e:
		try:
			s = float(s)
		except ValueError as e:
			raise ValueError(r"'%s' is not literal" % s)
	return s
'''

# 方法三：
'''
def str2num(s):
	s = s.split('.')
	if len(s) == 1:
		return int(s[0])
	else:
		return reduce(lambda x,y:10*x+y,map(int,s[0]+s[1])) / pow(10,len(s[1]))
		# return int(s[0]) + float(s[1])/10**len(s[1])
'''

# 方法四：
'''
def str2num(s):
	isFlo = s.find('.')
	if isFlo == -1:
		return int(s)
	else:
		return float(s)
'''

def calc(exp):
	ss = exp.split('+')
	ns = map(str2num,ss)
	return reduce(lambda acc,x: acc+x,ns)
def main():
	r = calc('100+200+345')
	print('100+200+345=',r)
	r = calc('99+88+7.6')
	print('99+88+7.6=',r)
main()