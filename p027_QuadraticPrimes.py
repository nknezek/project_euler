# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:48:40 2015

@author: nknezek
"""
#%%
def quad(a,b,n):
    return n**2 + a*n + b

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


#%%
N = 1000
p, _ = sieve_of_eratosthenes(N)
#%%
longest = 0
al = 0
bl = 0
for a in range(-(N-1),N):
    for b in range(-(N-1), N):
        nonprimefound = False
        n = 0
        l = 0
        while(not nonprimefound):
            if quad(a,b,n) in p:
                l += 1
                n += 1
            else:
                nonprimefound = True
                if l > longest:
                    longest = l
                    al = a
                    bl = b
#%%
print 'longest a=%i, b=%i, length=%i' % (al, bl, longest)
print 'a*b = %i' % (al*bl)