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
    
    maxmin = []
    ma = set()
    mi = set()
    
    for i in range(1,n-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            maxmin.append([i,True])
            ma.add(i)
        elif A[i] < A[i-1] and A[i] < A[i+1]:
            maxmin.append([i,False])
            mi.add(i)
            
    ans = 0
            
    for i,m in enumerate(maxmin):
        if i == len(maxmin) - 1:
            break
        if m[1] and not maxmin[i+1][1]:
            left = m[0]
            right = maxmin[i+1][0]
            
            if i == 0:
                left_x = 0
            else:
                left_x = maxmin[i-1][0]
            
            if i == len(maxmin) - 2:
                right_x = n-1
            else:
                right_x = maxmin[i+2][0]
                
            ans += (left - left_x) * (right_x - right)
            
    
    print(ans)
    

if __name__ == "__main__": 
    main()