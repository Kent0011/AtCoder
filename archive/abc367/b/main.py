import numpy as np
import math 
import sys
from functools import lru_cache

n = list(str(input()))
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

flag = True

for i in range(3):
    if n[-1] == '0':
        n.pop()

if n[-1] == '.':
    n.pop()

print(''.join(n))