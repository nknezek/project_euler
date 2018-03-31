# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 01:49:30 2015

@author: nknezek
"""

def collatz_iter(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1
#%%
chain_items = {1:1}
for i in range(2,10**6):
    if i not in chain_items:
        found_chain = False
        n0 = int(i)
        tmp_chain = {}
        tmp_chain[n0] = 0
        length = 0
        while(not found_chain):
            n1 = collatz_iter(n0)
            length += 1
            tmp_chain[n1] = -length
            if n1 in chain_items:
                found_chain = True
                tmp_chain.update([(k,v+length+chain_items[n1]) for k,v in zip(tmp_chain.keys(), tmp_chain.values())])
                chain_items.update(tmp_chain)
            n0 = n1

    else:
        pass


v=list(chain_items.values())
k=list(chain_items.keys())
longest_key = k[v.index(max(v))]
print 'longest length: %i' % chain_items[longest_key]
print 'number = %i' % longest_key
