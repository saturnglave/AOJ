# coding:utf-8
r, c = map(int, input().split())
table_input = [[0]*(c) for i in range(r)]
table_ans = [[0]*(c+1) for i in range(r+1)]
#print(table_input)

# table settings
for i in range(r):
    table_input[i] = list(map(int, input().split()))

print(table_input)


# 計算とテーブル穴埋め
for i in range(r+1):
    for j in range(c+1):
        if i < r and j < c:
            table_ans[i][j] = table_input[i][j]
        elif i < r and j == c:
            table_ans[i][c] = sum(table_input[i])
        elif i == r and j < c:
            table_ans[r][j] = 0


for j in range(c+1):
    for i in range(r+1):
        table_ans[r][j] += table_ans[i][j]

print(' '.join(map(str, table_ans)))
