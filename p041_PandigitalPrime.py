# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:56:29 2015

@author: nknezek
"""
from bitarray import bitarray
def sieve_of_eratosthenes(max_num, min_num = None):
    max_array = (max_num-1)/2
    B = bitarray(max_array)
    B.setall(True)
    p = 3
    i = 0
    primes = [2]
    finished = False
    while(not finished):
        if max_num < p**2:
            while(i<max_array):
                if B[i]:
                    primes.append(p)
                i+=1
                p+=2
            finished = True
            break
        if not B[i]:
            i += 1
            p += 2
            continue
        else:
            primes.append(p)
            j = (p**2 - 3)/2
        while(j < max_array):
            B[j] = False
            j += p
        i = i+1
        p = p+2
    if min_num:
        return [x for x in primes if x >= min_num]
    else:
        return primes

#%%
primes = sieve_of_eratosthenes()
#%%
maxpp = 0
for p in primes:
    strp = str(p)
    if strp == strp[::-1]:
        if p > maxpp:
            maxpp = p