import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,m = map(int,input().split())
# A = list(map(int,input().split()))

out = set()

for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    out.add((a,b))
    if a > 1 and b > 0:
        out.add((a-2,b-1))
    if a > 1 and b < n-1:
        out.add((a-2,b+1))
    if a > 0 and b > 1:
        out.add((a-1,b-2))
    if a > 0 and b < n-2:
        out.add((a-1,b+2))
    if a < n-1 and b > 1:
        out.add((a+1,b-2))
    if a < n-1 and b < n-2:
        out.add((a+1,b+2))
    if a < n-2 and b > 0:
        out.add((a+2,b-1))
    if a < n-2 and b < n-1:
        out.add((a+2,b+1))
        
print(n**2 - len(out))