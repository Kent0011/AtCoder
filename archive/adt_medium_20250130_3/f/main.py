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
    
    A.sort()
    
    av = np.average(A)
    
    ave = int(av)
    diff = sum(A) - ave * n
    
    ans = 0
    for i in range(n-diff):
        ans += abs(A[i] - ave)
    
    for i in range(n-diff, n):
        ans += abs(A[i] - (math.ceil(av)))
    
    print(ans//2)
    