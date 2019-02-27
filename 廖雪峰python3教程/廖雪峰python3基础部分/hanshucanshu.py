# -*- coding: utf-8 -*-
def product(*n):
    if len(n) <= 0:
        raise TypeError('At least ONE parameter is wanted.')    #拒绝空数组
    s = 1
    for i in n:
        if not isinstance(i,(int,float)):
            raise TypeError('Numbers only')
        s = s * i
    return s
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')         #检查是否能输入空数组
    except TypeError:
        print('测试成功!')