# coding: utf-8
W = input().lower()
count = 0

while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    count += T.lower().split().count(W)

print(count)
