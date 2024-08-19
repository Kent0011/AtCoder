import numpy as np
import math 
import sys


n,k = map(int,input().split())

A = list(map(int,input().split()))


A.sort()

ans = A[-1]-A[k]

for i in range(k+1):
    ans = min(ans,A[-(1+i)]-A[k-i])
        
print(ans)