# coding: utf-8
n,m,l = map(int,input().split())

A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(m)]
C = [[0]*l for i in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += B[k][j]*A[i][k]


for i in range(n):
    print(' '.join(map(str, C[i])))
