# coding:utf-8
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x >= y:
        print('{} {}'.format(y, x))
    else:
        print('{} {}'.format(x, y))
