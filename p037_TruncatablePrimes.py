# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:40:20 2015

@author: nknezek
"""

#%%
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
ltrpr = [[2,3,5,7]]
p = []
nums = range(1,10)
N = 6
for i in range(N):
    p.append(sieve_of_eratosthenes(10**(i+1), min_num = 10**(i)))
    if i>0:
        ltrpr.append([])
        for pr in ltrpr[i-1]:
            ltr = True
            prstr = str(pr)
            for n in nums:
                if int(str(n)+prstr) in p[i]:
                    ltrpr[i].append(str(n)+prstr)

#%%
trpr = []
for i in range(1,N):
    for pr in ltrpr[i]:
        tr = True
        prstr = str(pr)
        while(len(prstr)>0):
            if (int(prstr) not in p[len(prstr)-1]):
                tr = False
                break
            prstr = prstr[:-1]
        if tr:
            trpr.append(pr)
    i += 1

sum([int(x) for x in trpr])