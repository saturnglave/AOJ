# coding:utf-8
W, H, x, y, r = map(int, input().split())

if (x+r < W) and (x-r > W) and (y+r < H) and (y-r > H):
    print("Yes")
else:
    print("No")
