import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
H = list(map(int,input().split()))

highest = 0
count = 0

for i in range(1,len(H)):
    if H[i] >= highest:
        count+=1
        highest = H[i]
    
ans = []
ans.append(count)