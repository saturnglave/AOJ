# coding:utf-8
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for height in range(0,h):
        if height == 0 or height == h-1:
            print('#'*w)
        else:
            print('#'+'.'*(w-2)+'#')
    print('')
