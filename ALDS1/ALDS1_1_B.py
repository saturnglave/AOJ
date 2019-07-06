#coding:utf-8
# ユークリッドの互除法

def gcd(x, y):
    # yの方が大きい場合は値を入れ替える
    if x < y:
        x, y = y, x
    # yが0になるまで余りを計算する
    while y > 0:
        tmp = x % y
        x = y
        y = tmp
    return x

if __name__ == "__main__":
    x, y = map(int, input().split())
    result = gcd(x, y)
    print(result)