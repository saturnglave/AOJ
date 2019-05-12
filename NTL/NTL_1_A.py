#coding:utf-8
import math

n = int(input())
m = n
result=[]

def prime_factor(num, result):
    i = 2
    while(i <= math.sqrt(num)):
        if num % i == 0:
            num //= i
            result.append(str(i))
        else:
            i += 1
    
    if num != 1:
        result.append(str(num))

if __name__ == "__main__":
    prime_factor(n, result)
    print(str(m) + ': ' + ' '.join(result))


