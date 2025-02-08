import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq

def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False


if __name__ == "__main__":
    ...
    # n = int(input())
    # n,k = map(int,input().split())
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    A.sort()
    if A[0]* A[1] == A[2]:
        print('Yes')
        sys.exit()
    
    while next_permutation(A):
        if A[0]* A[1] == A[2]:
            print('Yes')
            sys.exit()
    
    print('No')