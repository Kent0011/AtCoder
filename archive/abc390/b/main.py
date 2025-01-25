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
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    if n==2:
        print('Yes')
        exit()
    for i in range(2,n):
        if A[i]*A[i-2] != A[i-1]**2:
            print('No')
            exit()
    print('Yes')
