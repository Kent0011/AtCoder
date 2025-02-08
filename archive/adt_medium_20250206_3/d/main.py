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
    n,d = map(int,input().split())
    # A = list(map(int,input().split()))
    S = list(str(input()))
    
    count = 0
    
    for i in range(n):
        tmp = S.pop()
        if tmp == "@":
            count += 1
        if count >= d:
            nn = i
            break
        
    ans = S + ["." for _ in range(nn+1)]
    
    print("".join(ans))