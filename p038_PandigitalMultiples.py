# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:40:24 2015

@author: nknezek
"""

#%%
maxs=0
for n in range(1,10**4):
    if n<10**2:
        for m in range(1,6):
            s = ''.join(map(str,[x*n for x in range(1,m+1)]))
            ss = set(s)
            ss.discard('0')
            if (len(ss) == 9) and (int(s) > maxs) and (len(s) == 9):
                maxs = int(s)
                print n,range(1,m+1),s
    elif n<10**3:
        for m in range(1,4):
            s = ''.join(map(str,[x*n for x in range(1,m+1)]))
            ss = set(s)
            ss.discard('0')
            if (len(ss) == 9) and (int(s) > maxs) and (len(s) == 9):
                maxs = int(s)
                print n,range(1,m+1),s
    elif n<10**4:
        for m in range(1,3):
            s = ''.join(map(str,[x*n for x in range(1,m+1)]))
            ss = set(s)
            ss.discard('0')
            if (len(ss) == 9) and (int(s) > maxs) and (len(s) == 9):
                maxs = int(s)
                print n,range(1,m+1),s

print maxs