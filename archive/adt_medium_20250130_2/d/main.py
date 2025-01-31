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
    n,a = map(int,input().split())
    T = list(map(int,input().split()))
    # S = list(str(input()))
    
    ans = [0]
    
    for t in T:
        ans.append(max(t+a, ans[-1] + a))
        
    ans.pop(0)
    
    for i in range(n):
        print(ans[i])