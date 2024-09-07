import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

A=  []
for _ in range(n):
    tmp = list(map(int,input().split()))
    A.append(tmp)
    
ans = 1

for i in range(n):
    if ans<=i:
        ans = A[i][ans-1]
    else:
        ans = A[ans-1][i]
    
print(ans)