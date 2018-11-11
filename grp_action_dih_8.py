#!/usr/bin/env sage -python

from sage.all import *

G = DihedralGroup(4)
X = [1, 2, 3, 4]
for g in G:
    print(g)
    out = []
    for x in X:
        print("{} -> {}".format(x, X[g(X.index(x) + 1) - 1]))
        out.append(X[g(X.index(x) + 1) - 1])
    print(out)
