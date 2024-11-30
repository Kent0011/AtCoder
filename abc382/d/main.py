import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,m = map(int,input().split())
# A = list(map(int,input().split()))

a = m-10*(n-1)

l = list(range(1,a+1))

X = []
count = 0

for i in itertools.combinations_with_replacement(l, n):
    X.append([i[j]+10*j for j in range(n)])
    
print(len(X))
for x in X:
    print(*x)