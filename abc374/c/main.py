import numpy as np
import math 
import sys
from functools import lru_cache
import itertools



n = int(input())
# n,k = map(int,input().split())
K = list(map(int,input().split()))

K.sort()

s = sum(K)

ans = s

for i in range(n):
    for k in itertools.combinations(K,i+1):
        tmp = sum(k)
        a = max(tmp,s-tmp)
        ans = min(ans,a)


print(ans)