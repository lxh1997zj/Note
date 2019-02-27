# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email'

import re

def is_vaild_email(addr):
    if re.match(r'^[\w.]+@\w+.\w{3}$',str(addr)):
        return True
    return False

# 测试
assert is_vaild_email('someone@gmail.com')
assert is_vaild_email('bill.gates@microsoft.com')
assert not is_vaild_email('bob#example.com')
assert not is_vaild_email('mr-bob@example.com')
print('ok')