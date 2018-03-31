# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:59:17 2015

@author: nknezek
"""
import numpy as np
#%%
with open('p081_matrix.txt', 'rb') as f:
    data = f.read()
M = np.matrix(data)
M = M.reshape((80,80))
N = 79
O = np.matrix(M)
#%%
for i in range(80):
    for j in range(i):
        O[j,N-j-1] += max(O[j,N-j], O[j+1,N-j-1])