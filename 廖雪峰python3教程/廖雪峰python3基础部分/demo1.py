# -*- coding: utf-8 -*-
def chashu(N, M):
    s = list(range(1, N + 1))
    s.append("+")
    s.append("-")
    s.append(" ")
    for i in s:
        if s[i] + s[i+1] == M or s[i] - s[i+1] == M:
            s.append('+')
