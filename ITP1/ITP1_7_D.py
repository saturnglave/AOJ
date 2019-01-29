# coding: utf-8
import numpy as np
n,m,l = map(int,input().split())

A = np.array([input().split() for i in range(n)])
B = np.array([input().split() for i in range(m)])

C = np.dot(A, B)

for i in range(m):
    print(' '.join(map(str, C[m])))