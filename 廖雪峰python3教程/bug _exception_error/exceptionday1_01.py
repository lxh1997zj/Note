# !/usr/bin/env python3
# -*- coding:utf-8 -*-
try:
	print('try...')
	r = 10 / int('2')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error !')
finally:
	print('finally...')
print('END')
print('-'*80)

def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')

main()



