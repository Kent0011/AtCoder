import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
S = list(map(str,input().split()))

if S[0] != S[1]:
    print('A')
elif S[0] == S[2]:
    print('B')
else:
    print('C')