import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

ans = 0

for i in range(12):
    s = str(input())
    if len(s) == i+1:
        ans+=1
        
print(ans)