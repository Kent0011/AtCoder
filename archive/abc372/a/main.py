import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

s = str(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

ans = []

for i in range(len(s)):
    if s[i] != '.':
        ans.append(s[i])
        
print(''.join(ans))