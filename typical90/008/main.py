import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
S = str(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

S_list = []

for s in S:
    if s == 'a'or't'or'c'or'o'or'd'or'e'or'r':
        S_list.append(s)

