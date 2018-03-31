# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:26:34 2015

@author: nknezek
"""
#%%
def divisors(n):
    f = []
    for i in range(1,n/2+1):
        if n%i==0:
            f.append(i)
    f.append(n)
    return f
def pdivisors(n):
    f = []
    for i in range(1,n/2+1):
        if n%i==0:
            f.append(i)
    return f
#n = 4
#done = False
#while(not done):
#    if nums.index(n) == len(nums)-1:
#        done = True
#        break
#    tmp = sum(divisors(n))
#    bk = sum(divisors(tmp))
#    if bk == n:
#        n = nums[nums.index(n)+1]
#        nums.remove(bk)
#        nums.remove(tmp)
#    else:
#        n = nums[nums.index(n)+1]
nums = range(1,10000)
am = []
for n in nums:
    tmp = sum(pdivisors(n))
    if sum(pdivisors(tmp)) == n and not (tmp == n):
        am.append(n)
sum(am)