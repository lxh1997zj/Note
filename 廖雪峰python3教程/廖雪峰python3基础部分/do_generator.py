# -*- coding: utf-8 -*-
def newtriangles():
    L = [1]
    while True:
        yield L
        K = [L[i] + L[i+1] for i in range(len(L) - 1)]
        L = [L[0] + 2] + K + [2*len(L) + 1]                # L[0]+2 和 [2*len(L) + 1] 效果一样
#测试:
n = 0
results = []
for t in newtriangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [3, 3],
    [5, 6, 5],
    [7, 11, 11, 7],
    [9, 18, 22, 18, 9],
    [11, 27, 40, 40, 27, 11],
    [13, 38, 67, 80, 67, 38, 13],
    [15, 51, 105, 147, 147, 105,51, 15],
    [17, 66, 156, 252, 294, 252, 156, 66, 17],
    [19, 83, 222, 408, 546, 546, 408, 222, 83, 19]
]:
    print('测试通过!')
else:
    print('测试失败!')