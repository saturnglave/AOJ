#coding:utf-8

def max_value(rt, n):
    minv = rt[0]
    maxv = rt[1] - rt[0]
    for j in range(1, n):
        maxv = max(maxv, rt[j]-minv)
        minv = min(minv, rt[j])
    return maxv


if __name__ == "__main__":
    n = int(input())
    rt = [int(input()) for i in range(n)]
    #print(rt)
    result = max_value(rt, n)
    print(result)

