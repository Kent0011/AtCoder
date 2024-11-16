import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

S = list(str(input()))
count = 0
ans = []

for s in S:
    if s == '|':
        ans.append(count)
        count = 0
    if s == '-':
        count+=1

print(*ans[1:])