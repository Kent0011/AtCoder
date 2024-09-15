import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,m = map(int,input().split())
# A = list(map(int,input().split()))

A = []

for _ in range(m):
    a,b = map(str,input().split())
    A.append([int(a),b])
    
exist_taro = [False for _ in range(n)]


for a in A:
    if exist_taro[a[0]-1] == False and a[1] == 'M':
        print('Yes')
        exist_taro[a[0]-1] = True
    else:
        print('No')