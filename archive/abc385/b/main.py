import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
h, w, x, y = map(int,input().split())
# A = list(map(int,input().split()))

S = []

for i in range(h):
    S.append(list(input()))
    
T = list(input())

x-=1
y-=1
count = 0

for t in T:
    if t == 'U':
        if x == 0:
            continue
        else:
            if S[x-1][y] == '#':
                continue
            elif S[x-1][y] == '@':
                count +=1
                x-=1
                S[x][y] = '.'
            else:
                x-=1
            

    if t == 'D':
        if x == h-1:
            continue
        else:
            if S[x+1][y] == '#':
                continue
            elif S[x+1][y] == '@':
                count +=1
                x+=1
                S[x][y] = '.'
            else:
                x+=1
            

    if t == 'L':
        if y == 0:
            continue
        else:
            if S[x][y-1] == '#':
                continue
            elif S[x][y-1] == '@':
                count +=1
                y-=1
                S[x][y] = '.'
            else:
                y-=1


    if t == 'R':
        if y ==w-1:
            continue
        else:
            if S[x][y+1] == '#':
                continue
            elif S[x][y+1] == '@':
                count +=1
                y+=1
                S[x][y] = '.'
            else:
                y+=1

print(x+1, y+1, count)