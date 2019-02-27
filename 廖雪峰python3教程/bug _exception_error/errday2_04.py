# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'pdb.set_trace()的调试程序！'
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)

# 可以用命令 p 变量名 查看变量，或者用命令c继续运行