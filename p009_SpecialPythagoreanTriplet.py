# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:16:14 2015

@author: nknezek
"""
#%%
product = 0
for a in range(1,333):
    for b in range(1,(999-a)/2+2):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            a0 = a
            b0 = b
            c0 = c
            product = a*b*c
            print '%i * %i * %i = %i' % (a0, b0, c0, product)
            break
