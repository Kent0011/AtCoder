import numpy as np
import math 
import sys
from functools import lru_cache 
import itertools

# n = int(input())
n,k = map(int,input().split())
R = list(map(int,input().split()))

for i in itertools.product(*(range(1, r + 1) for r in R)):
    if sum(i)%k==0: print(*i)