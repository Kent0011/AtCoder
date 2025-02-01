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
    # S = list(str(input()))
    
    P.insert(0,0)
    
    tmp = -1
    count = 0
    
    while 1:
        tmp = P[tmp]-1
        count += 1
        if tmp == 0:
            break
    
    print(count)