# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:29:00 2015

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
    return primes
#%%
N = 10**6
p = sieve_of_eratosthenes(N)
#%% Find break locations of different lengths of prime numbers
ind = 0
brks = [0]
for d in range(1,6):
    found = False
    while(not found):
        ind += 1
        if len(str(p[ind]))  > d:
            brks.append(ind)
            found = True
            break
brks.append(len(p)-1)
b6 = [0]
p6 = p[brks[-2]:]
ind = 0
for d in range(1,9):
    found = False
    while(not found):
        ind += 1
        if not str(p6[ind])[0] == str(d):
            b6.append(ind)
            found = True
            break
b6.append(len(p6)-1)
#%%
cp = set()
for i in range(6):
    print 'searching primes of length %i' %(i+1)
    pms = p[brks[i]:brks[i+1]+1]
    if i == 5:
        for pr in pms:
            prstr = str(pr)
            circ = True
            for ind in range(len(prstr)):
                p1 = int(prstr[0])
                if int(prstr) not in pms[b6[p1-1]:b6[p1]+1]:
                    circ = False
                    break
                prstr = prstr[1:]+prstr[0]
            if circ:
                cp.add(pr)
    else:
        for pr in pms:
            prstr = str(pr)
            circ = True
            for ind in range(len(prstr)):
                if int(prstr) not in pms:
                    circ = False
                    break
                prstr = prstr[1:]+prstr[0]
            if circ:
                cp.add(pr)
print '%i cicular primes found:'%len(cp)
print cp
