# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:30:11 2015

@author: nknezek
"""
#%%
import csv
import string
with open('./p022_names.txt','rb') as csvnames:
    reader = csv.reader(csvnames)
    names = reader.next()
names.sort()
tot=0
for ind,name in enumerate(names):
    tot += sum([string.ascii_uppercase.index(x)+1 for x in name])*(ind+1)