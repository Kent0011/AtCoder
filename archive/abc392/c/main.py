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
    n = int(input())
    # n,k = map(int,input().split())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    # S = list(str(input()))
    
    dic = {}
    for i in range(n):
        dic[i] = Q[i]-1
    
    A = []
    
    for i in range(n):
        A.append([i,P[i]-1,Q[i]-1])
    
    B = sorted(A,key=lambda x:x[2])
    
    ans = []
    
    for i in range(n):
        ans.append(dic[B[i][1]])
        
    ans = list(map(lambda x:x+1, ans))
    
    print(*ans)