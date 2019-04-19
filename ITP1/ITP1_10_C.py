# coding:utf-8
import math
import statistics

while True:
    n = int(input())

    if n == 0:
        break

    *S, = map(int, input().split())
    print(statistics.pstdev(S))
