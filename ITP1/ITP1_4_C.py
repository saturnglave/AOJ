# coding:utf-8

while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)

    if op == '?':
        break
    elif op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        # なぜか判定では//じゃないと通らなかった（エスケープ？）
        print(a//b)
