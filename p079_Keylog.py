# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:52:39 2015

@author: nknezek
"""
#%%
inputs = []

with open("p079_keylog.txt",'r') as f:
    for line in f:
       inputs.append(int(line.strip()))
#%%
uniq = list(set(inputs))
uniq.sort()
uniq
working = []
for key,item in enumerate(uniq):
    for l in range(key+1, len(uniq)):
        if item/100 == uniq[l]/100:
            if item/10%10 == uniq[l]%10:
                working.append(int(str(item)[0]+))
            elif item%10 == uniq[l]/10%10:
