# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:34:55 2015

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
#%%
num_to_factor = 600851475143
#num_to_factor = 15
factored = False
test_prime = 2
prime_factors = []
while(not factored):
    if num_to_factor == 1:
        factored = True
    elif num_to_factor%test_prime == 0:
        prime_factors.append(test_prime)
        num_to_factor = num_to_factor/test_prime
    else:
        test_prime = next_prime(test_prime)
print 'prime factors %s' % prime_factors
print 'largest prime factor %i' % max(prime_factors)