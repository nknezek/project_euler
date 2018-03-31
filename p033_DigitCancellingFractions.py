# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:49:02 2015

@author: nknezek
"""

#%%
things = []
for denom in range(10,100):
    for numer in range(10, denom):
        nstr = str(numer)
        dstr = str(denom)
        for  x in range(2):
            for y in range(2):
                if (not dstr[(y+1)%2] == '0') and nstr[x] == dstr[y]:
                    redfrac = float(nstr[(x+1)%2])/float(dstr[(y+1)%2])
                    if redfrac == float(numer)/float(denom):
                        things.append((numer,denom))

things2 = [x for x in things if not x[1]%10==0]
#%%
import fractions
from operator import mul
numerprod = reduce(mul,[x[0] for x in things2])
denomprod = reduce(mul,[x[1] for x in things2])
gcd = fractions.gcd(numerprod,denomprod)
print denomprod/gcd