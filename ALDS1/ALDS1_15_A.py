#coding:utf-8
n = int(input())
coin = [25, 10, 5, 1]
ans = 0

for i in range(0, 4):
    #貪欲法。金額が高いものから使ってお釣りを生成する
    ans += n // coin[i]
    n = n % coin[i]

print(ans)