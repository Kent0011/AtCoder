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
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    ans = 0
    S = [[0]]
    
    for i in range(n):
        tmp = []
        for s in S[-1]:
            tmp.append(s+A[i])
            tmp.append(s^A[i])
        S.append(tmp)
        print(S)
    
    print(len(set(S[-1])))
