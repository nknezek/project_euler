# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:35:10 2015

@author: nknezek
"""
#%%
sum_sq = 0
sum_n = 0
for n in range(1,101):
    sum_sq += n**2
    sum_n += n
print 'sum difference = %i' % (sum_n**2 - sum_sq)