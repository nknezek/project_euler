# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:52:31 2015

@author: nknezek
"""
#%%
mths = [31,28]+[31,30]*2+[31,31]+[30,31]*2
wk = 7
yrsta = 1901
yrend = 2000
yrs = range(yrsta,yrend+1)
yr = yrsta
dy = 2
Nsun = 0
while(yr<=yrend):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                m = mths[:]
                m[1] += 1
        else:
            m = mths[:]
            m[1] += 1
    else:
        m = mths[:]
    for ndays in m:
        dy = (dy+ndays)%7
        if dy==0:
            Nsun+=1
    yr+=1

Nsun