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
    n = int(input())
    
    # N K (整数)
    # n,k = map(int,input().split())
    
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
    A = []
    for _ in range(n):
        A.append(list(input()))
    
    B = []
    for _ in range(n):
        B.append(list(input()))
        
    ans_0 = 0
    ans_90 = 3
    ans_180 = 2
    ans_270 = 1
    
    for i in range(n):
        for j in range(n):
            if A[i][j] != B[i][j]:
                ans_0 += 1
            if A[i][j] != B[n-j-1][i]:
                ans_90 += 1
            if A[i][j] != B[n-i-1][n-j-1]:
                ans_180 += 1
            if A[i][j] != B[j][n-i-1]:
                ans_270 += 1
                
    print(min(ans_0,ans_90,ans_180,ans_270))
        
if __name__ == "__main__": 
    main()