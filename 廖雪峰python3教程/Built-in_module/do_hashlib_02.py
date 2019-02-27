# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib,random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符,返回值是当前整数对应的ascii字符。
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    return user.password == get_md5(password + user.salt)  # 前一个password是数据库的密码，后一个是输入的登录密码。


# 测试
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '12234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')