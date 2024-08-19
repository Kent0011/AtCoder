import numpy as np
import math 
import sys


n = int(input())

A = list(map(int,input().split()))

ans = [0]

for i in range(n):
    ans.append((ans[-1]+A[i])%360)
    
ans.sort()

a=0
for i in range(len(ans)-1):
    a = max(a,abs(ans[i]-ans[i+1]))
    
a = max(a,abs(ans[-1]-360))

print(a)