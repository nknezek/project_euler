# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:18:25 2015

@author: nknezek
"""
#%%
def ssd(n):
    return sum(int(c)**2 for c in str(n))
#%%
ends89 = set([89])
num89 = 0
num1 = 0
ends1 = set([1])

for N in range(1,10**3):
    cur_found = set([N])
    done = False
    n = N
    while(not done):
        if n in ends89:
            ends89 = ends89.union(cur_found)
            num89 += 1
            done = True
        elif n in ends1:
            ends1 = ends1.union(cur_found)
            num1 += 1
            done = True
        else:
            cur_found.add(n)
            n = ssd(n)
print num89, num1, num89+num1

#%%
import itertools as it
import math

for s in it.combinations_with_replacement('0123456789', 3):
    print s
#%%
for N in range(10**3, 10**7):
    n = ssd(N)
    if n in ends89:
        num89 += 1
    elif n in ends1:
        num1 += 1


print num89, num1, num89+num1