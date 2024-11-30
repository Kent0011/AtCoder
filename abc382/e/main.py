import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,x = map(int,input().split())
P = list(map(int,input().split()))

P = list(map(lambda x: x/100,P))

sum = P.sum()

print()