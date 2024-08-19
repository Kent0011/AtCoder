import numpy as np
import math 
import sys


n = int(input())

A = list(map(int,input().split()))

ans = []

for i in range(n-1):
    if A[i]<A[i+1]:
        for j in range(A[i+1]-A[i]):
            ans.append(A[i]+j)
    else:
        for j in range(A[i]-A[i+1]):
            ans.append(A[i]-j)
            
ans.append(A[-1])
            
print(*ans)