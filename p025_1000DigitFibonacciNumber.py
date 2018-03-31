# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:26:43 2015

@author: nknezek
"""
#%%
b0 = 1.
b1 = 1.
b = 2
c = 3
d = 1
while(d < 1000):
    b0 = b1
    b1 = b
    b = b0 + b1
    if b>10:
        b = b/10.
        b1 = b1/10.
        d += 1
    c += 1
print c, b, d
