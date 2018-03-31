# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:01:42 2015

@author: nknezek
"""

#%%
coins = [200, 100, 50, 20, 10, 5, 2, 1]
aim = 200
combs = 0
def enum_into(coins,aim):
    global combs
    remain = aim-coins[0]
    if remain == 0:
        combs += 1
        if len(coins) > 1:
            enum_into(coins[1:], aim)
    elif remain > 0:
        enum_into(coins, remain)
        if len(coins) > 1:
            enum_into(coins[1:], aim)
    elif remain < 0 and len(coins) > 1:
        enum_into(coins[1:], aim)
#%%
combs = 0
enum_into(coins, 200)
print 'Number of combs = %i' % combs
