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
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    ans = [i for i in range(1, n+1)]
    ans = set(ans)
    
    for a in A:
        ans.remove(a)
        
    ans = list(ans)
    
    print(len(ans))
    print(*ans)