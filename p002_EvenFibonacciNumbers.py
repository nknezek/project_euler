# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:28:51 2015

@author: nknezek
"""
#%%
num_max = 4e6
#num_max = 10
even_sum = 0
fib_num0 = 1
fib_num1 = 1
while fib_num1 < num_max:
    temp = fib_num1
    fib_num1 += fib_num0
    fib_num0 = temp
    if fib_num1%2==0:
        even_sum += fib_num1
    print fib_num0
print 'sum of even terms = '+str(even_sum)