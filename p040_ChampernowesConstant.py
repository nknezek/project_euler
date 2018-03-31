# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:02:49 2015

@author: nknezek
"""


#%%
def get_d(D):
    D -= 1
    if D == 0:
        return 1
    else:
        n = 0
        dmax = 0
        dbuff = 0
        while(D>=dbuff):
            n += 1
            dmax = 9*n*10**(n-1)
            dbuff += dmax
        dbuff -= dmax
        Dn = D-dbuff
        m = Dn%n
        l = Dn/n
        if m == 0:
            return (l/(10**(n-m-1)))%10+1
        else:
            return (l/(10**(n-m-1)))%10
#%% Testing
s = ''.join(map(str,[x for x in range(1,112)]))
for d in range(2880,2900):
    print get_d(d)

#%%
ans = 1
for d in [10**i for i in range(6)]:
    print d, get_d(d)
    ans *= get_d(d)
print ans