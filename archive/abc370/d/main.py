import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
h,w,q = map(int,input().split())
# A = list(map(int,input().split()))

X = np.zeros((h,w))
ans = h*w

for i in range(q):
    r,c = map(int,input().split())
    r-=1
    c-=1
    
    if X[r][c] == 0:
        X[r][c] = 1
        ans-=1
    else:
        j = 1
        while(r-j >= 0):
            if X[r-j][c] == 0:
                X[r-j][c] = 1
                ans-=1
                break
            j += 1
            
        j = 1
        while(r+j <= h-1):
            if X[r+j][c] == 0:
                X[r+j][c] = 1
                ans-=1
                break
            j += 1
                
        j = 1
        while(c-j >= 0):
            if X[r][c-j] == 0:
                X[r][c-j] = 1
                ans-=1
                break
            j += 1
                
        j = 1
        while(c+j <= w-1):
            if X[r][c+j] == 0:
                X[r][c+j] = 1
                ans-=1
                break
            j += 1

        
print(ans)