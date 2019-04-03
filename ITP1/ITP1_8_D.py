# coding: utf-8
import string
s = input()
p = input()

# make ring
s = s + s
#print(s)

# find pattern
result = p in s
if result == True:
    print('Yes')
elif result == False:
    print('No')
