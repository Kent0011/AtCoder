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
    H = list(map(int,input().split()))
    # S = list(str(input()))
    
    tmp = H[0]

    for i in range(1, n):
        if H[i] > tmp:
            tmp = H[i]
        else:
            break
    
    print(tmp)