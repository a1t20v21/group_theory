#!/usr/bin/env sage -python

from sage.all import *

G = DihedralGroup(4)
X = [1, 2, 3, 4]
for x in X:
    for g in G:
        print("{} * {} -> {} ".format(g, x, g.orbit(x)))
