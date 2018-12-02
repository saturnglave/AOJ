# coding:utf-8
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for height in range(h):
        print('#'*w)
    print('')
