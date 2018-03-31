# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:57:01 2015

@author: nknezek
"""

#%%
def sum_dig(n,p):
    if sum([int(x)**p for x in str(n)]) == n:
        return True
    else:
        return False
N1 = 2
N2 = 9**5*6
p = 5
ns = []
for n in range(N1,N2):
    if sum_dig(n,p):
        ns.append(n)

print ns
print sum(ns)