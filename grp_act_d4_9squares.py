#!/usr/bin/env sage -python

from sage.all import *

G = DihedralGroup(4)
X = Matrix([[1,2,3],[4,5,6],[7,8,9]])
g = G("(1,3)")
print(g(X[1][0]))
