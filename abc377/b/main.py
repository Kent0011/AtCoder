import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

A = []
NG_i = set()
NG_j = set()

for i in range(8):
    tmp = list(str(input()))
    for j,a in enumerate(tmp):
        if a == '#':
            NG_i.add(i)
            NG_j.add(j)
            
ans = 0

for i in range(8):
    for j in range(8):
        if (i in NG_i) == False and (j in NG_j) == False:
            ans+=1
            
print(ans)
    
