import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


def main():
    # N (整数)
    n = int(input())
    
    # N K (整数)
    # n,k = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    # S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    uniq = set()
    notuni = set()
    
    for i in range(n):
        if A[i] not in uniq and A[i] not in notuni:
            uniq.add(A[i])
        elif A[i] in uniq:
            uniq.remove(A[i])
            notuni.add(A[i])
    
    if len(uniq) == 0:
        print(-1)
        return
    
    a = max(uniq)
    
    print(A.index(a)+1)
    

if __name__ == "__main__": 
    main()