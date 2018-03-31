# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:54:46 2015

@author: nknezek
"""

#%%
N = 100
ns = set([])
for a in range(2,N+1):
    for b in range(2,N+1):
        pd = a**b
        if pd not in ns:
            ns.add(pd)
print len(ns)
