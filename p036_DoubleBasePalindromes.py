# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:45:31 2015

@author: nknezek
"""

#%%
s = 0
for a in range(1,10):
    N1 = int(''.join(map(str,[a])))
    bN1 = bin(N1)
    if bN1[2:] == bN1[:1:-1]:
        s += N1
    N2 = int(''.join(map(str,[a,a])))
    bN2 = bin(N2)
    if bN2[2:] == bN2[:1:-1]:
        s += N2
    for b in range(10):
        N3 = int(''.join(map(str,[a,b,a])))
        bN3 = bin(N3)
        if bN3[2:] == bN3[:1:-1]:
            s += N3
        N4 = int(''.join(map(str,[a,b,b,a])))
        bN4 = bin(N4)
        if bN4[2:] == bN4[:1:-1]:
            s += N4
        for c in range(10):
            N5 = int(''.join(map(str,[a,b,c,b,a])))
            bN5 = bin(N5)
            if bN5[2:] == bN5[:1:-1]:
                s += N5
            N6 = int(''.join(map(str,[a,b,c,c,b,a])))
            bN6 = bin(N6)
            if bN6[2:] == bN6[:1:-1]:
                s += N6
