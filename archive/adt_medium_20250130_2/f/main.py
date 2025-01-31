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
    B = set()
    count = 0
    
    for i in range(n):
        a = str(input())
        b = a[::-1]
        if a == b:
            B.add(a)
        else:
            A.add(a)
            A.add(b)
        
    print((len(A)//2)+len(B))