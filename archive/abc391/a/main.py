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
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    S = list(str(input()))
    
    ans = []
    
    for s in S:
        if s == 'N':
            ans.append('S')
        elif s == 'S':
            ans.append('N')
        elif s == 'E':
            ans.append('W')
        elif s == 'W':
            ans.append('E')
            
    print(''.join(ans))