# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:22:24 2015

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

def factor(num_to_factor):
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
    return prime_factors

def subset(list1, list2):
    #test if list1 is subset of list2
    temp = list(list2)
    for item in list1:
        try:
            temp.remove(item)
        except:
            return False
    return True

#%%
inclusive_factors = []
for n in range(1,21):
    temp = list(inclusive_factors)
    for item in factor(n):
        try:
            temp.remove(item)
        except:
            inclusive_factors.append(item)
inclusive_factors.sort()
print 'prime factors of 1-20: %s' % inclusive_factors
product = 1
for item in inclusive_factors:
    product = product*item
print 'product = %i' %product
