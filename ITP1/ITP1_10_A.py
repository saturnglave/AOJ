# coding:utf-8
import math
x1, y1, x2, y2 = map(float, input().split())

# 絶対値を出しておく（絶対値なしで二乗したらRE）
x = abs(x2-x1)
y = abs(y2-y1)
p = math.sqrt(x*x + y*y)
print(p)
