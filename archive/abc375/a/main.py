import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))
s = list(str(input()))

ans= 0

for i in range(1,n-1):
    if s[i-1] == '#' and s[i] == '.' and s[i+1] == '#':
        ans += 1
        
print(ans)