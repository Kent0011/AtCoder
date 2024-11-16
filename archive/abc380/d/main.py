import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

S = str(input())
l = len(S)
Q = int(input())
K = list(map(int,input().split()))

ans = []

for k in K:
    k-=1
    x = k//l
    y = k%l
    
    if bin(x).count('1')%2 == 0:
        ans.append(S[y])
    else:
        ans.append(S[y].swapcase())

print(*ans)