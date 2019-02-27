# -*- coding: utf-8 -*-
def hanoi(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)
#调用(期待输出)
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
hanoi(3,'A','B','C')
