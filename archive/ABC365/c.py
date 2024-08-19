import numpy as np
import math 
import sys

# n = int(input())
n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

if sum(A) <= m:
    print('infinite')
    sys.exit()
    
left = 0
right = A[-1]

while(left<=right):
    ans = 0
    mid = (left+right)//2
    for a in A:
        ans += min(mid,a)
    if right - left <= 1:
        break
    if ans>m:
        right = mid
    if ans<=m:
        left = mid

print(left)
