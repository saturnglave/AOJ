# coding:utf-8
import math
a, b, C = map(int, input().split())

# Cの正弦を出す
sinC = math.sin(math.radians(C))
cosC = math.cos(math.radians(C))

# 面積S=(ab*sinC)/2
S = (a*b*sinC)/2
c = math.sqrt(pow(a, 2) + pow(b, 2) - 2*a*b*cosC)
L = a + b + c
h = b * sinC

print(S)
print(L)
print(h)
