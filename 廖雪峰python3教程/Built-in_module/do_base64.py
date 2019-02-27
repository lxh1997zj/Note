# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

def safe_base64_decode(s):
    '''
    n = 4 - len(s) % 4
    # s = s + b'=' * (4 - (4 if len(s) % 4 == 0 else len(s) % 4)) # 方法一
    # s = s + b'=' * n     # 方法二
    while n:   # 方法三
        s += b'=' * n
        n -= 1
    return base64.b64decode(s)
    # return base64.b64decode(s + (len(s) % 4) * b'=')   # 方法四
    '''
    if isinstance(s,bytes):  # 方法五

        answer = base64.b64decode(s + (len(s) % 4) * b'=')
    else:
        answer = base64.b64decode(s + (len(s) % 4) * '=')
    return answer



# 测试
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')