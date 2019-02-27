# !/usr/bin/env python3
# -*- codimg:utf-8 -*-

import pickle

with open('hero.txt','wb') as f:
	f.write(pickle.dumps('美好的事情即将发生'))
with open('hero.txt','rb') as f:
	print(pickle.loads(f.read()))
  
with open('bro.txt','wb') as f:
	pickle.dump('美好的事情即将发生',f)

with open('bro.txt','rb') as f:
	print(pickle.load(f))	

import json

obj1 = dict(name = '小明',age = 20)
obj2 = dict(name = 'lvxiing',age = 20) 

s1 = json.dumps(obj1,ensure_ascii = True)

s2 = json.dumps(obj1,ensure_ascii = False)

s3 = json.dumps(obj2,ensure_ascii = True)

s4 = json.dumps(obj2,ensure_ascii = False)

# 如果ensure_ascii为true（默认值），则保证输出将所有传入的非ASCII字符转义。如果ensure_ascii为false，则这些字符将按原样输出。
# Python官方文档(English)
# If ensure_ascii is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is false, these characters will be output as-is.

print(s1)
print(s2)
print(s3)
print(s4)