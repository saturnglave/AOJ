# coding:utf-8
n = int(input())
a = list(map(int, input().split()))
print('{} {} {}'.format(min(a), max(a), sum(a)))