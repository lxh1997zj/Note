# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'公钥加密算法的实现'
# 前面说过，公钥加密算法是由Crypto.Cipher子包下的PKCS1_v1_5.py或PKCS1_OAEP.py模块以已经存在的密钥对儿为密钥来实现的，现在常用的是PKCS1_v1_5。另外，我们前面提到过，使用对方的公钥加密，使用对方的私钥解密才能保证数据的机密性，因此这里以上面生成的公钥进行加密数据，以上面生成的私钥解密数据：

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64

# 数据加密
message = 'This is an plain text'

with open('rsa.pub', 'r') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    cipher_text = base64.b64encode(cipher_obj.encrypt(message.encode('utf-8')))
    print('cipher test:', cipher_text)

# 数据解密
with open('rsa.key', 'r') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    random_generator = Random.new().read
    plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator)
    print('plain text:', plain_text)
