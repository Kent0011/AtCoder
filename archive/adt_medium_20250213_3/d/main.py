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
    
    s = 2025
    
    x = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    cnt = 0
    
    for i in range(1,10):
        if x%i == 0 and x//i < 10:
            cnt+=1
    
    print(s - x*cnt)