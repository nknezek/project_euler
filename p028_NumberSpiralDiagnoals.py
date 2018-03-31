# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:35:25 2015

@author: nknezek
"""
#%%
N = 1001
sm = 1
for s in range(3,N+1,2):
    sm += sum([s**2-x for x in range(0,(s-1)*4,(s-1))])
print sm