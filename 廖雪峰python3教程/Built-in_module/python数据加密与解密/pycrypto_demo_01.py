# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'使用SHA256算法获取一段数据的摘要信息'

from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update('Hello, World!'.encode('utf-8'))
digest = hash.hexdigest()
print(digest)