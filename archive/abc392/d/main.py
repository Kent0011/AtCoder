import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq

def daice(a_len: int, a: dict, b_len: int, b: dict) -> float:
    ans = 0
    for i in a.keys():
        ans += (a[i] / a_len) * (b.get(i,0) /b_len)
    return ans


if __name__ == "__main__":
    ...
    n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    K = []
    A = []
    
    for i in range(n):
        tmp = list(map(int,input().split()))
        K.append(tmp.pop(0))
        a = {}
        for i in range(K[i]):
            if tmp[i] in a:
                a[tmp[i]] += 1
            else:
                a[tmp[i]] = 1
        A.append(a)
    
    ans = 0
    
    for i,j in itertools.combinations([i for i in range(n)], 2):
        tmp = daice(K[i],A[i],K[j],A[j])
        ans = max(ans,tmp)
    
    print(ans)