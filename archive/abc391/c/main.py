import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq


if __name__ == "__main__":
    ...
    # n = int(input())
    n,q = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    P = {}
    H = [1 for i in range(n)]
    ans = set()
    
    for i in range(n):
        P[i] = i
        
    for _ in range(q):
        tmp = list(map(int,input().split()))
        
        if tmp[0] == 1:
            tmp[1] -= 1
            tmp[2] -= 1
            p = P[tmp[1]]
            
            H[p] -= 1
            H[tmp[2]] += 1
            
            if H[tmp[2]] == 2:
                ans.add(tmp[2])
            if H[p] == 1 and p in ans:
                ans.remove(p)
                
            P[tmp[1]] = tmp[2]
            
        else:
            print(len(ans))
            