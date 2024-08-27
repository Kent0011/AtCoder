import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,k = map(int,input().split())
A = list(map(int,input().split()))

B = []
for i in range(k):
    B.append(A.pop())
    
B.reverse()

print(*(B+A))