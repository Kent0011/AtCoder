import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,q = map(int,input().split())
# A = list(map(int,input().split()))
s = str(input())

s = list(s)

num = 0
for i in range(n-2):
    if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
        num += 1

for _ in range(q):
    x,c = map(str,input().split())
    x = int(x)
    x -=1
    
    if x <= n-3 and s[x] == 'A':
        if s[x:x+3] == ['A', 'B', 'C']:
            num -= 1
    if x >= 1 and x <= n-2 and s[x] == 'B':
        if s[x-1:x+2] == ['A', 'B', 'C']:
            num -= 1
    if x >= 2 and s[x] == 'C':
        if s[x-2:x+1] == ['A', 'B', 'C']:
            num -= 1
            
    s[x] = c
    
    if x <= n-3 and s[x] == 'A':
        if s[x:x+3] == ['A', 'B', 'C']:
            num += 1
    if x >= 1 and x <= n-2 and s[x] == 'B':
        if s[x-1:x+2] == ['A', 'B', 'C']:
            num += 1
    if x >= 2 and s[x] == 'C':
        if s[x-2:x+1] == ['A', 'B', 'C']:
            num += 1
        

    print (num)