# coding:utf-8
import sys
import string

text = []
for l in sys.stdin:
    text.append(l)

sentence = ''.join(text).lower()

for ltr in string.ascii_lowercase:
    print('{} : {}'.format(ltr, sentence.count(ltr)))
