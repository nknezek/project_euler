# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:42:57 2015

@author: nknezek
"""
from bitarray import bitarray
import numpy as np
from operator import mul

#%%
def sieve_of_eratosthenes(max_num, return_sum=False):
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
    if return_sum:
        return primes, sum_of_primes
    else:
        return primes

def generate_triangle_nums(num):
    t = []
    t.append(1)
    for n in range(2,num+1):
        t.append(t[-1]+n)
    return t

def prime_factors(n, primes=None, sort=False):
    factors = []
    if not primes:
        primes = sieve_of_eratosthenes(n)
    remaining = n
    primes_to_test = [x for x in primes if x <= n]
    while(not remaining==1):
        temp = primes_to_test[:]
        for prime in temp:
            if remaining%prime == 0:
                factors.append(prime)
                remaining = remaining/prime
            else:
                primes_to_test.remove(prime)
    if sorted:
        factors.sort()
    return factors

def divisors(n):
    f = []
    for i in range(1,n/2+1):
        if n%i==0:
            f.append(i)
    f.append(n)
    return f

def divisors_from_prime_factors(prime_factors):
    d = [1]
    prime_factors.sort()
    for r in range(1,len(prime_factors)+1):
        for subset in it.combinations(prime_factors,r):
            d.append(reduce(mul,subset))
    return list(set(d))


#%% test old methods
import time
num = 2*3*4*5*7*3*3*10*23
start_t = time.time()
prime_factors(num)
print 'primetime = %f' %(start_t-time.time())
t1 = time.time()
divisors(num)
print 'factors = %f' %(t1-time.time())
#%%
cur_num = 100
found=False
Ndivs = 50
while(not found):
    cur_num += 2
    divs = divisors(cur_num)
    if len(divs)>Ndivs:
        found=True
        print 'smallest number with >%i factors: %i with %i divisors' % (Ndivs, cur_num, len(divs))
        print facs

#%% Find divisors by iterating on small prime factors
import itertools as it
from operator import mul
max_prime = 100
primes = sieve_of_eratosthenes(max_prime)
found=0
Ndivisors = 50
ind = 4
ans = []
while(found<10):
    to_test = []
    for x in range(ind):
        to_test += [primes[x]]*(ind-x)
    for r in range(2,len(to_test)+1):
        for subset in it.combinations(to_test,r):
            if len(divisors_from_prime_factors(list(subset))) > Ndivisors:
                found += 1
                ans.append(reduce(mul,subset,1))
min(ans)

#%%
tnums = generate_triangle_nums(4000)
n = 1000
found = False
while(not found):
    Ndiv = len(divisors(tnums[n]))
    if Ndiv > 500:
        print 'smallest triangle >500 div is %i' %tnums[n]
        found = True
        break
    n+=1

#%%
number = 0
i = 1
def number_of_divisors(n):
    nod = 0
    sqrt = int(np.sqrt(n))
    for i in range(1, sqrt):
        if number%i == 0:
            nod += 2
    if sqrt*sqrt == n:
        nod += 1
    return nod

while(number_of_divisors(number) < 500):
    number += i
    i += 1

