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
    S = list(str(input()))
    T = "ABC"
    
    S = list(S)
    T = list(T)
    cnt = 0
    
    for w in range(1,len(S)):
        for c in range(1,w+1):
            t = deque(T[:])
            ans = []
            for i in range(1,len(S)+1):
                if i % w == c % w:
                    ans.append(S[i-1])
                    if len(ans)>=3:
                        if ans[-3:] == ["A","B","C"]:
                            cnt+=1
                            ans = []
        
    print(cnt)