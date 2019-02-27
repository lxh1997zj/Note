# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
版本二可以提取出带名字的Email地址：
<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
'''

import re

def name_of_email(addr):
    '''
    m = re.split(r'[<>@.]+',addr)
    if m[0] == '':
        return m[1]
    return m[0]
    '''
    """
    p = r'^<([\w ]+)>|^(\w+)'
    r = re.match(p,addr)
    if r.group(1):
        return r.group(1)
    return r.group(2)
    """
    m = re.match(r'<?(\w+\s?\w+)>?.*@\w+.\w{3}',addr)
    return m.group(1)

# 测试
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
