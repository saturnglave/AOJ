# coding:utf-8
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    # H+Wが偶数の時は#, 奇数の場合は.が出る
    for height in range(h):
        for width in range(w):
            if (height+width) % 2 == 0:
                print('#', end = '')
            else:
                print('.', end = '')
        # 次の行へ
        print ('')
    # 次のデータセットへ
    print('')
