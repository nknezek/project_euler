# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:39:43 2015

@author: nknezek
"""
#%%
def pascals_triangle(rows):
    r0 = [1]
    r1 = [1, 1]
    t = [r0,r1]
    for n in range(1,rows):
        r = [1]
        for i in range(len(t[n])-1):
            r.append(t[n][i]+t[n][i+1])
        r.append(1)
        t.append(r)
    return t

#%%
p = pascals_triangle(20)
sum([x**2 for x in p[-1]])
