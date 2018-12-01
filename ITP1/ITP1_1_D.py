# coding: utf-8
s = int(input())
print(int(s/3600), ':', int(s%3600/60), ':', int(s%3600%60), sep='')
