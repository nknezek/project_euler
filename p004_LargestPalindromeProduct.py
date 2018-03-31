# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:57:44 2015

@author: nknezek
"""
#%%
def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False

#%%
palindromes = []
max_test = int(1e3)
for n in range(max_test):
    for m in range(n):
        prod = n*m
        if is_palindrome(prod):
            palindromes.append(prod)

print palindromes
print max(palindromes)

