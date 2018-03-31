# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:34:47 2015

@author: nknezek
"""

#%%
from bitarray import bitarray
def sieve_of_eratosthenes(max_num):
    max_array = (max_num-1)/2
    B = bitarray(max_array)
    B.setall(True)
    p = 3
    i = 0
    primes = [2]
    sum_of_primes = 2
    finished = False
    while(not finished):
        if max_num < p**2:
            while(i<max_array):
                if B[i]:
                    primes.append(p)
                    sum_of_primes += p
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
            sum_of_primes += p
            j = (p**2 - 3)/2
        while(j < max_array):
            B[j] = False
            j += p
        i = i+1
        p = p+2
    return primes, sum_of_primes

max_num = 2*10**6
primes, sum_of_primes = sieve_of_eratosthenes(max_num)
print 'sum is %i' %sum_of_primes