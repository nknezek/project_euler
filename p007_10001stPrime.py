# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:38:00 2015

@author: nknezek
"""

#%%
def next_prime(n):
    test = n
    found_prime = False
    while(not found_prime):
        test += 1
        for i in range(2, test):
            if test%i == 0:
                break
        else:
            found_prime = True
            prime = test
    return prime

start = 1
cur_prime = start
for n in range(10001):
    cur_prime = next_prime(cur_prime)
print n,cur_prime