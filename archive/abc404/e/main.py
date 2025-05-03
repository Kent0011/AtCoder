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
    C = list(map(int,input().split()))
    C.insert(0,0)
    
    # B1 B2 B3 ... Bn (整数)
    A = list(map(int,input().split()))
    A.insert(0,0)
    
    # S (文字列)
    # S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    dp = [float("inf") for _ in range(n)]
    dp[n-1] = 0
    
    for i in range(n-1,0,-1):
        if A[i] == 0:
            dp[i-1] = min(dp[i-1],dp[i])
        else:
            flag = True
            for j in range(1,C[i]+1):
                if i-j >= 0:
                    if A[i-j] > 0:
                        dp[i-j] = dp[i]+1
                        flag = False
                        break
                    else:
                        dp[i-j] = dp[i]+1
            if flag:
                A[max(0,i-C[i])] = 1
                
    
    print(dp[0])

if __name__ == "__main__": 
    main()