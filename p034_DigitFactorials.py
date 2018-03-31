# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:26:45 2015

@author: nknezek
"""
#%%
import math
s = 0
f = [math.factorial(x) for x in range(10)]
for n in range(3,f[-1]*7):
    if sum([f[int(d)] for d in str(n)]) == n:
        s += n
print s