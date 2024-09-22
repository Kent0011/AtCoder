import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,b,k = map(int,input().split())
c = list(map(int,input().split()))

count = 0

for i in itertools.product(c, repeat=n):
    if i[0] != 0:
        a = int(''.join(map(str,i)))
        if a%b == 0: count = count%1000000007 + 1
    
print(count%1000000007)