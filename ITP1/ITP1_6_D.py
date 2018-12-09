# coding:utf-8
n, m = map(int, input().split())
a = [[]*n for i in range(m)]
b = [[0]*1 for i in range(m)]
#print(a)
#print(b)

#行列Aの生成
#n行の部分は連続でスペース区切りで入力
for i in range(n):
        a[i] = list(map(int, input().split()))

#行列Bの生成
for i in range(m):
    b[i] = int(input())

#行列計算
for i in range(n):
    c = 0
    for j in range(m):
        c += a[i][j]*b[j]
    print(c)
