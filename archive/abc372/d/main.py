import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
H = list(map(int,input().split()))

H_shorter = []

for i in range(1,n):
    if H[i]<H[i-1]:
        H_shorter.append(i)

H_shorter.append(n)

print(H_shorter)

ans = []
j = 0

for i in range(n):
    if i == H_shorter[j]:
        j += 1
    ans.append(max(H_shorter[j]-i-1,1))
    
print(*ans)