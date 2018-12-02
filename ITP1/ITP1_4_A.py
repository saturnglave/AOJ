# coding:utf-8
a, b = map(int, input().split())
d = int(a/b)
r = a%b
f = '{:.5f}'.format(a/b)

print('{} {} {}'.format(d, r, f))
