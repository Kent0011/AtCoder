import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

s = str(input())

if s.endswith("san"):
    print('Yes')
else:
    print('No')