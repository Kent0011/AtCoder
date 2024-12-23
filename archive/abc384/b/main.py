import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect


if __name__ == "__main__":
    # n = int(input())
    n,r = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    for i in range(n):
        tmp = list(map(int,input().split()))
        D = tmp[0]
        A = tmp[1]
        
        if (1600 <= r and r <= 2799 and D == 1) or (1200 <= r and r <= 2399 and D == 2):
            r += A
    
    print(r)