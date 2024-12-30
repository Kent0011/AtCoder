import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect


if __name__ == "__main__":
    ...
    # n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    S = list(str(input()))
    
    ans = 0
    tmp = False
    
    for s in S:
        if s == "0":
            if tmp:
                tmp = False
                continue
            else:
                ans += 1
                tmp = True
        else:
            ans += 1
            tmp = False
    
    print(ans)