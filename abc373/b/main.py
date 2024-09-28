import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

s = list(input())

A = list('BCDEFGHIJKLMNOPQRSTUVWXYZ')

ans = 0
current = s.index('A')

for a in A:
    ans += abs(current - s.index(a))
    current = s.index(a)
    
print(ans)