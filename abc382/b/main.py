import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,d = map(int,input().split())
# A = list(map(int,input().split()))

S = list(str(input()))

count = 0

for i in range(n):
    if S[n-i-1] == '@':
        S[n-i-1] = '.'
        count += 1
    if count == d:
        break
    
print("".join(S))