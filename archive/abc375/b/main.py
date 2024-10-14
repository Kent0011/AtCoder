import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

def dist(a,b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

current = [0,0]
ans = 0

for i in range(n):
    A = list(map(int,input().split()))
    ans += dist(current,A)
    current = A
    

print(ans + dist(current,[0,0]))
    