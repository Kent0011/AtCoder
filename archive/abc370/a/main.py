import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
L,R = map(int,input().split())
# A = list(map(int,input().split()))

if L == 1 and R == 0:
    print('Yes')
elif L ==0 and R==1:
    print('No')
else:
    print('Invalid')