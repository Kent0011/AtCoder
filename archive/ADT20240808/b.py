import numpy as np
import math 
import sys

# n = int(input())
n,m = map(int,input().split())
# A = list(map(int,input().split()))
A = []
B = []
for i in range(m):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
ans = []

for i in range(n):
    if (i+1 in B) == False:
        ans.append(i+1)

if len(ans) == 1:
    print(ans[0])
else:
    print(-1)