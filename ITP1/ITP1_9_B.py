# coding:utf-8
while True:
    string = input(str())
    if string == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        string = string[h:] + string[:h]
    print(string)
