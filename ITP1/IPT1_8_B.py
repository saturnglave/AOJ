# coding:utf-8
while True:
    x = str(input())
    if x[0] == '0':
        break
    else:
        print(sum(int(num) for num in (x)))
