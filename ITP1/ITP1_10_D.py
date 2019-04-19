# coding:utf-8
import math

n = int(input())
x = map(int, input().split())
y = map(int, input().split())

p1 = sum([(abs(x[i]-y[i]) for i in range(n)])
p2 = sqrt(sum([pow(abs(x[i]-y[i]), 2) for i in range(n)]))
p3 = pow(sum([pow(abs(x[i]-y[i]), 3)]),1/3)
p = max([abs(x[i] - y[i]) for i in range(n)])

print(p1)
print(p2)
print(p)
