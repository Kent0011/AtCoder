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
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    
    a = 1
    ans = 0
    
    while 1:
        # n//(2**a)の平方根を求める
        target = n // (2**a)
        if target == 0:
            break
            
        # 二分探索で平方根を求める
        left = 0
        right = target
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= target:
                left = mid + 1
            else:
                right = mid - 1
        sqrt_val = right
        
        ans += (sqrt_val + 1) // 2
        a += 1
        
    print(ans)

if __name__ == "__main__": 
    main()