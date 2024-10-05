import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

s =str(input())
t =str(input())

for i in range(min(len(s),len(t))):
    if s[i]!=t[i]:
        print(i+1)
        sys.exit()
    
if len(s)!=len(t):
    print(min(len(s),len(t))+1)
else:
    print(0)