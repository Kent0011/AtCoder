import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


if __name__ == "__main__":
    ...
    # n = int(input())
    # n,k = map(int,input().split())
    S, T = map(str,input().split())
    # S = list(str(input()))
    
    S = list(S)
    T = list(T)
    
    for w in range(1,len(S)):
        for c in range(1,w+1):
            t = deque(T[:])
            
            for i in range(1,len(S)+1):
                f = False
                if i % w == c % w:
                    if S[i-1] != t.popleft():
                        f = True
                        break
                    if len(t) == 0:
                        print('Yes')
                        sys.exit()
                if f == True:
                    break
        
    print('No')