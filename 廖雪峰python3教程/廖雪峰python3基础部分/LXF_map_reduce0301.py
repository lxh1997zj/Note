# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    n=s.index('.')                                              # 找出小数点位置
    s=s[:n]+s[n+1:]                                             # 去除小数点，因为pop无法在str使用
    return reduce(lambda x,y:x*10+y,map(int,s))/(10**len(s[n:]))# 先取整再除以10的次方让小数点归位
# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456 ) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
