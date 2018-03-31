# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:44:19 2015

@author: nknezek
"""
import itertools as it
#%%
def pdivisors(n):
    tocheck = range(1,int(n**0.5)+1)
    f = []
    done = False
    i = tocheck[0]
    while(not done):
        if n%i == 0:
            try:
                nxt = tocheck[tocheck.index(i)+1]
            except:
                done = True
            tocheck.remove(i)
            f.append(i)
            if not n/i == i:
                if n/i <= int(n**0.5):
                    tocheck.remove(n/i)
                f.append(n/i)
        else:
            try:
                nxt = tocheck[tocheck.index(i)+1]
            except:
                done = True
        i = nxt
    f.remove(n)
    return f
#%%
MaxN = 28123
nums = range(1,MaxN)
abN = []
for n in range(12,MaxN):
    if sum(pdivisors(n))>n:
        abN.append(n)
sum2abN = [sum(c) for c in it.combinations_with_replacement(abN, r=2)]
sum2abN.sort()
non_representable = set(range(1,MaxN)) - set(sum2abN)
answer = sum(non_representable)
print answer