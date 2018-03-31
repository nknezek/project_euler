# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:21:50 2015

@author: nknezek
"""

#%%
f = open('p042_words.txt','rb')
s = f.read()
f.close()
l = [w.replace('\"','') for w in s.split(',')]
tri = [n*(n+1)/2 for n in range(40)]
twords = 0
for w in l:
    if sum([ord(x)%32 for x in w]) in tri:
        twords += 1