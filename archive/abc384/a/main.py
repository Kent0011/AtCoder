import numpy as np
import pandas as pd
import itertools
import math
import sys
from functools import lru_cache
import random


# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))
# S = list(str(input()))

n, c1, c2 = map(str,input().split())
n = int(n)

S = list(str(input()))

ans = []

for s in S:
    if s == c1:
        ans.append(s)
    else:
        ans.append(c2)

print("".join(ans))