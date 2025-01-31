import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

if __name__ == "__main__":
    ...
    # n = int(input())
    n, nn, m = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    A = {}
    
    for i in range(m):
        a, b = map(int,input().split())
        a -= 1
        b -= 1
        if a in A.keys():
            A[a].append(b)
        else:
            A[a] = [b]
        if b in A.keys():
            A[b].append(a)
        else:
            A[b] = [a]
    

    N_1 = [-1 for _ in range(n+nn)]
    N_2 = [-1 for _ in range(n+nn)]
    N_1_max = 0
    N_2_max = 0
        
    q = deque([0])
    
    N_1[0] = 0
    while q:
        tmp = q.popleft()
        for i in A.get(tmp, []):
            if N_1[i] == -1:
                N_1[i] = N_1[tmp] + 1
                N_1_max = max(N_1_max, N_1[i])
                q.append(i)
    
    q = deque([n + nn - 1])
    N_2[n + nn - 1] = 0
    
    while q:
        tmp = q.popleft()
        for i in A.get(tmp, []):
            if N_2[i] == -1:
                N_2[i] = N_2[tmp] + 1
                N_2_max = max(N_2_max, N_2[i])
                q.append(i)

    
    print(N_1_max+N_2_max+1)
