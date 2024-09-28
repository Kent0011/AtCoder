import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

C_1,C_2 = [0], [0]

for i in range(n):
    c,p = map(int,input().split())
    if c==1:
        C_1.append(C_1[-1]+p)
        C_2.append(C_2[-1])
    if c==2:
        C_2.append(C_2[-1]+p)
        C_1.append(C_1[-1])
        
q = int(input())

for i in range(q):
    l,r = map(int,input().split())
    ans = [C_1[r]-C_1[l], C_2[r]-C_2[l]]
    print(*ans)