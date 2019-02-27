# -*- coding:utf-8 -*-
# 方法一
# def is_palindrome(n):
#	return int(str(n)[::-1]) == n

# 方法二
# def is_palindrome(n):
#	n_s = str(n)
#	for i in range(len(n_s)):
#		return n_s[i] == n_s[-i-1]

# 方法三
def is_palindrome(n):
	I,m = n,0
	while I:
		m = m * 10 + I % 10
		I //=10
		'''
	    12321
	    m=1,I=1232,
	    m=10+2=12,I=123,
	    m=120+3=123,I=12,
	    m=1230+2=1232,I=1,
	    m=12320+1=12321,I=0,
	    break
	    '''
	return m == n










# 测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')