# -*- coding:utf-8 -*-


def perm(n,begin,end):
    if begin>=end:
        print(n)
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
 
n=[1,2]
perm(n,0,len(n))

