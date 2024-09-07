import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

s = list(input())
t = list(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

x = []
tmp = []
for i in range(len(s)):
    if s[i]>t[i]:
        tmp.append(1)
    if s[i]==t[i]:
        tmp.append(0)
    if s[i]<t[i]:
        tmp.append(-1)

for i in range(len(tmp)):
    if tmp[i] == 1:
        s[i] = t[i]
        x.append(''.join(s))
    
for i in range(len(tmp)-1,-1,-1):
    if tmp[i] == -1:
        s[i] = t[i]
        x.append(''.join(s))

print(len(x))
for i in range(len(x)):
    print(x[i])