#coding:utf-8

def insertionSort(A,N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(' '.join(map(str, A)))


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    

    print(' '.join(map(str, A)))
    insertionSort(A, N)