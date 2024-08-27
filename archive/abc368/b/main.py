import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
A = list(map(int,input().split()))

count = 0

while(1):
    A.sort(reverse=True)
    
    A[0]-=1
    A[1]-=1
    
    count+=1
    count2=0
    for a in A:
        if a>0:
            count2+=1
    if count2<=1:
        break
    
print(count)