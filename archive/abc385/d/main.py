import numpy as np
import math 
import sys
from functools import lru_cache
import itertools
import bisect

# n = int(input())
n, m, x, y = map(int,input().split())
# A = list(map(int,input().split()))

d_ikey = {}
d_jkey = {}

for i in range(n):
    A = list(map(int,input().split()))
    if A[0] not in d_ikey:
        d_ikey[A[0]] = []
    if A[1] not in d_jkey:
        d_jkey[A[1]] = []
        
    bisect.insort(d_ikey[A[0]], A[1])
    bisect.insort(d_jkey[A[1]], A[0])
    
D = []
C = []
for i in range(m):
    A = list(input().split())
    D.append(A[0])
    C.append(int(A[1]))

x-=1
y-=1
count = 0

for i,d in enumerate(D):
    if d == 'L':
        if y in d_jkey:
            s=bisect.bisect_left(d_jkey[y], x-C[i])
            e=bisect.bisect_right(d_jkey[y], x+1)
            count+=(e-s)
            for h in range(s,e):
                tmpi = d_ikey[d_jkey[y][h]].index(y)
                del d_ikey[d_jkey[y][h]][tmpi]
            del d_jkey[y][s:e]
        x-=C[i]

    if d == 'R':
        if y in d_jkey:
            s=bisect.bisect_left(d_jkey[y], x)
            e=bisect.bisect_right(d_jkey[y], x+C[i]+1)
            count+=(e-s)
            for h in range(s,e):
                tmpi = d_ikey[d_jkey[y][h]].index(y)
                del d_ikey[d_jkey[y][h]][tmpi]
            del d_jkey[y][s:e]
        x+=C[i]

    if d == 'D':
        if x in d_ikey:
            s=bisect.bisect_left(d_ikey[x], y-C[i])
            e=bisect.bisect_right(d_ikey[x], y+1)
            count+=(e-s)
            for h in range(s,e):
                tmpj = d_jkey[d_ikey[x][h]].index(x)
                del d_jkey[d_ikey[x][h]][tmpj]
            del d_ikey[x][s:e]
        y-=C[i]


    if d == 'U':
        if x in d_ikey:
            s=bisect.bisect_left(d_ikey[x], y)
            e=bisect.bisect_right(d_ikey[x], y+C[i]+1)
            count+=(e-s)
            for h in range(s,e):
                tmpj = d_jkey[d_ikey[x][h]].index(x)
                del d_jkey[d_ikey[x][h]][tmpj]
            del d_ikey[x][s:e]
        y+=C[i]

print(x+1, y+1, count)