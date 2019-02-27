# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
'''

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GBK')) # 原为'utf-8',不能实现.可改为:print(output.decode('utf-8','ignore'))
print('Exit code:',p.returncode)
# 错误纠正链接 url ='https://blog.csdn.net/lilong117194/article/details/74936407'