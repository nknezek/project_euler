# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 02:09:08 2015

@author: nknezek
"""
#%%
import random
import numpy as np
#%% Game Code
spaces = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
          'C1', 'U1', 'C2', 'C3','R2','D1','CC2','D2','D3','FP','E1','CH2',
          'E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4',
          'CH3','H1','T2','H2']
class chance:
    def __init__(self):
        self.cards = list(np.random.permutation(16))
        self.ind = -1

    def draw(self, loc):
        self.ind = (self.ind+1)%16
        n = self.cards[self.ind]
        outcomes = {0:0, 1:10, 2:11, 3:24, 4:39, 5:5}
        if n<=5:
            return outcomes[n]
        elif n==6 or n==7:
            return (((loc-5)/10+1)*10+5)%40
        elif n==8:
            if loc < 12 or loc > 28:
                return 12
            else:
                return 28
        elif n==9:
            return loc-3
        else:
            return loc

class commchest:
    def __init__(self):
        self.cards = list(np.random.permutation(16))
        self.ind = -1

    def draw(self, loc):
        self.ind = (self.ind+1)%16
        n = self.cards[self.ind]
        if n==0:
            return 0
        elif n==1:
            return 10
        else:
            return loc

def roll(Ndie, dside):
    s = []
    for d in range(Ndie):
        s.append(random.randint(1,dside))
    return s

class game:
    def __init__(self, Ndie, dside):
        self.cc = commchest()
        self.ch = chance()
        self.spaces = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
          'C1', 'U1', 'C2', 'C3','R2','D1','CC2','D2','D3','FP','E1','CH2',
          'E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4',
          'CH3','H1','T2','H2']
        self.chsp = [7, 22, 36]
        self.ccsp = [2, 17, 33]
        self.player = player()
        self.Ndie = Ndie
        self.dside = dside

    def turn(self,verbose=False):
        player = self.player
        dbls = 0
        rollagain = True
        while(rollagain):
            rl = roll(self.Ndie,self.dside)
            if verbose:
                print 'rolled %s' %rl
            if rl[0] == rl[1]:
                dbls += 1
                rollagain = True
                if dbls == 3:
                    player.loc == 10
                    break
            else:
                rollagain = False
            player.advance(sum(rl))
            if verbose:
                print 'advanced to sq %i, %s' % (player.loc, self.spaces[player.loc])
            if player.loc == 30:
                if verbose:
                    print 'to jail to sq %i, %s' % (player.loc, self.spaces[player.loc])
                player.loc = 10
            elif player.loc in self.chsp:
                player.loc = self.ch.draw(player.loc)
                if verbose:
                    print 'chance to sq %i, %s' % (player.loc, self.spaces[player.loc])
            elif player.loc in self.ccsp:
                player.loc = self.cc.draw(player.loc)
                if verbose:
                    print 'cc to sq %i, %s' % (player.loc, self.spaces[player.loc])
        return player.loc

class player:
    def __init__(self):
        self.loc = 0
    def advance(self, spaces):
        self.loc = (self.loc+spaces)%40

#%% Run Game
dside = 4
Ndie = 2
gm = game(Ndie, dside)
dist = dict(zip(range(40),[0]*40))
for n in range(500000):
    dist[gm.turn(verbose=False)] += 1
import operator
dist_st = sorted(dist.items(), key=operator.itemgetter(1))
for t in dist_st:
    print t[1], t[0], gm.spaces[t[0]]

#%% Plot Histogram
import matplotlib.pyplot as plt
plt.bar(dist.keys(), dist.values())


#%% Die Roll Distributions
dside = 4
Ndie = 3
dist = dict(zip(range(2,dside*Ndie+1),[0]*len(range(2,dside*Ndie+1))))
for n in range(80000):
    dist[sum(roll(Ndie,dside))] += 1
plt.bar(dist.keys(), dist.values())
