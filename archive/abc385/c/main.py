import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
H = list(map(int,input().split()))
ans=0

for i in range(n):
    current = H[i]
    a = 1
    for j in range(i+1,n):
        if H[j] == current:
            dist = j-i
            tmp = 2
            c = j
            while(1):
                c = c + dist
                if c < n:
                    if H[c] == current:
                        tmp+=1
                    else:
                        break
                else:
                    break
            a = max(a,tmp)
    ans = max(ans,a)

print(ans)