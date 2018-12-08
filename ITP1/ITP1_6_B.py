# coding:utf-8
n = int(input())
card = [[False]*14 for i in range(4)]
suits = ['S', 'H', 'C', 'D']

#print(card)

for loop in range(n):
    suit, number = input().split()
    number = int(number)

    # 入力にあったものについてTrueにしておく
    if suit == 'S':
        card[0][number] = True
    elif suit == 'H':
        card[1][number] = True
    elif suit == 'C':
        card[2][number] = True
    elif suit == 'D':
        card[3][number] = True

for i in range(4):
    for j in range(1,14):
        if card[i][j] == False:
            print(suits[i], j)
