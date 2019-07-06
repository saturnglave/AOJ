#coding:utf-8
import math

def prime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return  False
    else:
        i = 3
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 2

        return True


if __name__ == "__main__":
    x = int(input())
    counter = 0

    for i in range(x):
        n = int(input())
        if prime(n) == True:
            counter += 1

    print(counter)
