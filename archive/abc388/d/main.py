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
    if n == 1:
        print(A[0])
        return
    
    delta_A = [0] * n
    A_added = [0] * n
    B = []
    
    for i in range(n-1):
        A_added[i] = A_added[i-1] + delta_A[i]
        tmp = A[i] + A_added[i]
        delta_A[i+1] += 1
        if i+1+tmp < n:
            delta_A[i+1+tmp] -= 1
        B.append(max(0,tmp-(n-i-1)))
        
    B.append(A[-1] + A_added[-2] + delta_A[-1])
    print(*B)

if __name__ == "__main__": 
    main()