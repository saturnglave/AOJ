# coding:utf-8
n = int(input())
tp = 0
hp = 0

for i in range(n):
    t, h = map(str, input().split())
    if t > h:
        tp += 3
    elif t == h:
        tp += 1
        hp += 1
    else:
        hp += 3

print(tp, hp)
