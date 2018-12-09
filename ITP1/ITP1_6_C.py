# coding:utf-8
n = int(input())
dorm = [[[0]*10 for i in range(3)] for j in range(4)]
#print(dorm)

# 入居状況の更新
for loop in range(n):
    b, f, r, v = map(int, input().split())
    dorm[b-1][f-1][r-1] += v

# 区切り判定用のカウンタ
x = 0
for i in range(4):
    if x != 0:
        print('#'*20)
    x += 1

    for j in range(3):
        for k in range(10):
            print('', dorm[i][j][k], end = '')
        print()
