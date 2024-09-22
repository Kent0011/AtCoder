import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
h,w = map(int,input().split())
# A = list(map(int,input().split()))

A = []
A_sum = []
At_sum = [0 for _ in range(w)]

for _ in range(h):
    a = list(map(int,input().split()))
    A_sum.append(sum(a))
    for i, arg in enumerate(a):
        At_sum[i]+=arg
    A.append(a)
    
    
B = [[] for _ in range(h)]

for i, b in enumerate(B):
    for j in range(w):
        b.append(A_sum[i]+At_sum[j]-A[i][j])
        
for b in B:
    print(*b)