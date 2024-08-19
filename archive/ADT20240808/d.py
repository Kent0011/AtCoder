import numpy as np
import math 
import sys
from functools import lru_cache

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

def func(n:int):
    if n == 0:
        return 1
    else:
        return func(n//2)+func(n//3)
    
print(func(n))