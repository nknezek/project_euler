# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:27:43 2015

@author: nknezek
"""

#%%
def find_sols(n):
    sols = set()
    for c in range(2,n-1):
        for a in range(1,(n-c)/2+1):
            b = n-a-c
            if a**2 + b**2 == c**2:
                sols.add((a,b,c))
    return sols

maxl = 0
for n in range(1000):
    sols = find_sols(n)
    if len(sols) > maxl:
        maxl = len(sols)
        s = sols
        ans = n

print ans