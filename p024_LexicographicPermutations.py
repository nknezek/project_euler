# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:52:30 2015

@author: nknezek
"""
#%%
import itertools as it

nums = range(10)
p = list(it.permutations(nums))[10**6-1]
ans = ''
for c in p:
    ans += str(c)

print ans