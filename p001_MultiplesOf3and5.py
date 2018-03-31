# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:25:40 2015

@author: nknezek
"""

sum = 0
num_max = 1000
for n in range(1, num_max):
    if n%3==0 or n%5==0:
        sum += n
print sum