# coding:utf-8
string = list(input())
q = int(input())

for i in range(q):
    command, a, b, *p = input().split()
    a = int(a)
    b = int(b)

    if command == 'print':
        print(*string[a:b+1], sep ='')
    elif command == 'reverse':
        string[a:b+1] = reversed(string[a:b+1])
    else:
        string[a:b+1] = p[0]
