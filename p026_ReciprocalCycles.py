# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:54:22 2015

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
p, _ = sieve_of_eratosthenes(1000)
#%%
def test3cycle(n):
    l = len(n)/3
    if (n[:l] == n[l:2*l]) and (n[l:2*l] == n[2*l:3*l]):
        return True
    else:
        return False
#%%
cycle_length = {}
for d in p:
    found = False
    decimal = []
    decimal.append(int(str(10/d)[0]))
    rem = 10%d
    while(not found):
        if rem == 0:
            found = True
            cycle_length[d] = 0
            break
        quot, rem = divmod(rem*10, d)
        decimal.append(quot)
        if len(decimal)%3 == 0:
            if test3cycle(decimal):
                found = True
                cycle_length[d] = len(decimal)/3
                break
import operator
max(cycle_length.iteritems(), key=operator.itemgetter(1))