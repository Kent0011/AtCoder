import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque, defaultdict


def main():
    # N (整数)
    # n = int(input())
    
    # N K (整数)
    n,k = map(int,input().split())
    n += 1
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
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
    
    A = []
    A_sum = [0]
    
    
    for i in range(n):
        if i < k:
            A.append(1)
            A_sum.append((A_sum[-1]+A[-1])%1000000000)
        else:
            A.append((A_sum[-1]-A_sum[i-k])%1000000000)
            A_sum.append((A_sum[-1]+A[-1])%1000000000)
    
    print(A[-1])

if __name__ == "__main__": 
    main()