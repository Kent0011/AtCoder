import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_max = max(A)
C = np.full(A_max+1,-1)
tmp = A_max+1

for i,a in enumerate(A):
    if a<= tmp:
        C[a:tmp] = i+1
        tmp = a

for b in B:
    if b > A_max:
        print(1)
    else:
        print(C[b])