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
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    flag = False
    
    for i in range(len(A)):
        if A[i] == i+1:
            flag = False
        elif A[i] == i+2 and i != len(A)-1:
            A[i], A[i+1] = A[i+1], A[i]
            flag = True
            break
    
    if not flag:
        print('No')
        exit()
    
    for i in range(len(A)):
        if A[i] != i+1:
            print('No')
            exit()
    print('Yes')
