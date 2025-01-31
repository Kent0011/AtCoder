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
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    A = set()
    ans = 0
    for i in range(n):
        x,y = (map(int,input().split()))
        A.add((x,y))
        
    while A:
        stack = [A.pop()]
        while stack:
            x,y = stack.pop()
            if (x-1,y-1) in A:
                stack.append((x-1,y-1))
                A.remove((x-1,y-1))
            if (x-1,y) in A:
                stack.append((x-1,y))
                A.remove((x-1,y))
            if (x,y-1) in A:
                stack.append((x,y-1))
                A.remove((x,y-1))
            if (x,y+1) in A:
                stack.append((x,y+1))
                A.remove((x,y+1))
            if (x+1,y) in A:
                stack.append((x+1,y))
                A.remove((x+1,y))
            if (x+1,y+1) in A:
                stack.append((x+1,y+1))
                A.remove((x+1,y+1))
        ans += 1
        
    print(ans)
