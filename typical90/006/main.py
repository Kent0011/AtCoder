import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,k = map(int,input().split())
S = list(input())

# S = [[i,s] for i,s in enumerate(S)]
ans = []
current = 0

for count in range(k):
    tmp = min(enumerate(S[current:n-k+1+count]),key=lambda x: x[1])
    ans.append(tmp[1])
    current = tmp[0]+current+1
    
print(''.join(ans))