# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:48:21 2015

@author: nknezek
"""
#%%
n = sum([int(x) for x in str(int('0b1'+'0'*1000,2))])
print n