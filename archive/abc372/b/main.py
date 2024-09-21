import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

m = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

def to_ternary(n):
    if n == 0:
        return '0'
    
    ternary = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary = str(remainder) + ternary
    
    return ternary

m_3 = list(to_ternary(m))

m_3 = m_3[::-1]

ans = []

for i in range(len(m_3)):
    for _ in range(int(m_3[i])):
        ans.append(i)

print(len(ans))

print(*ans)