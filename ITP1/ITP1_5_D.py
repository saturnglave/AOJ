# coding:utf-8
# 1からnまでの整数のうち、3の倍数と3がつく時に出力

n = int(input())
x = 0

for i in range(1,n+1):
    if i % 3 == 0:
        # 3の倍数
        print('', i, end = '')

    else:
        # 3がつく数
        x = i
        while (x):
            if x % 10 == 3:
                print('', i, end = '')
                break
            # x = x / 10(整数)と同じ
            x //= 10
# 最後に開業
print()
