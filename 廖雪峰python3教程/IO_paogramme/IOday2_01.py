# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from io import StringIO
f = StringIO('1234567890abcdef')
f.seek(0,2)
f.write('hello world')
f.seek(0,0)
s = f.read()
print(s)
f.close()

f = StringIO('hello world')
print('StringIO position ='+str(f.tell()))
f.write('asdf')
f.write('1234')
print('write position ='+str(f.tell()))
f.seek(0)
s = f.read()
print(s)
f.close()
