import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

n = list(str(input()))

n = list(map(int,n))

if n.count(1) == 1 and n.count(2) == 2 and n.count(3) == 3:
    print('Yes')
else:
    print('No')