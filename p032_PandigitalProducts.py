# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:05:28 2015

@author: nknezek
"""
#%%
import itertools as it
n = range(1,10)
total = 0
count = 0
things = []
for perm in it.permutations(n,9):
    for a in range(1,3):
        for b in range(2,6-a):
            aint = int(''.join(map(str,perm[:a])))
            bint = int(''.join(map(str,perm[a:a+b])))
            prod = int(''.join(map(str,perm[a+b:])))
            if aint*bint == prod:
                total += prod
                count += 1
                things.append((aint, bint, prod))

#%%
print total
print things
print sum(set([x[2] for x in things]))