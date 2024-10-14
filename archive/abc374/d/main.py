import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

def dist(a,b,c,d):
    return math.sqrt(pow(a-c,2)+pow(b-d,2))

# n = int(input())
n,s,t = map(int,input().split())
# A = list(map(int,input().split()))

Lines = []
d = 0

for i in range(n):
    tmp = list(map(int,input().split()))
    tmp.insert(0,i)
    d+=dist(*tmp[1:])
    Lines.append(tmp)
    

def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False
    
ans = float('inf')
lis = [i+1 for i in range(n)]

for x in range(1<<n):
    current = [0,0]
    a = 0
    for i in lis:
        line = Lines[i-1]
        if x & (1<<i):
            a += dist(*current,*line[1:3])/s
            a += dist(*line[1:])/t
            current = line[3:]
        else:
            a += dist(*current,*line[3:])/s
            a += dist(*line[1:])/t
            current = line[1:3]
    ans = min(ans,a)
            
    
while(next_permutation(lis)):
    for x in range(1<<n):
        current = [0,0]
        a = 0
        for i in lis:
            line = Lines[i-1]
            if x & (1<<i):
                a += dist(*current,*line[1:3])/s
                a += dist(*line[1:])/t
                current = line[3:]
            else:
                a += dist(*current,*line[3:])/s
                a += dist(*line[1:])/t
                current = line[1:3]
        ans = min(ans,a)
    
    
print(ans)