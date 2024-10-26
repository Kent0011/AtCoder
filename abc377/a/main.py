import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

s = list(str(input()))

if s.count('A') == 1 and s.count('B') == 1 and s.count('C') == 1:
    print('Yes')
else:
    print('No')