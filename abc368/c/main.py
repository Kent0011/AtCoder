import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
H = list(map(int,input().split()))

count = 0
next = 0

for h in H:
    h+=next
    count-=next
    next = 0
    count+=3*(h//5)
    if h%5 == 0:
        continue
    elif h%5 == 1:
        count+=1
        next = 1
    elif h%5 == 2:
        count+=2
        next = 2
    else:
        count+=3

print(count)