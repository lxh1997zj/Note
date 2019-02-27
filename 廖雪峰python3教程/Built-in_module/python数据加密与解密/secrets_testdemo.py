# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'https://www.cnblogs.com/yyds/p/7072492.html'

import secrets
import string

# 实例一:生成一个由8位数字和字母组成的随机密码
alphanum = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphanum) for i in range(8))
print(password)

# 实例二:生成一个由10位数字和字母组成的随机密码，要求至少有一个小写字符，至少一个大写字符 和 至少3个数字
alphanum = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphanum) for i in range(10))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and len(list(c.isdigit() for c in password)) >= 3):
        break
print(password)

# 实例三:生成一个用于找回密码应用场景的、包含一个安全令牌的、很难猜到的临时URL
url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
print(url)
