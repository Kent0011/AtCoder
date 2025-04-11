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
    # n,k = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    n,h,w = map(int,input().split())
    
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
    
    sy,sx = map(int,input().split())
    sy -= 1
    sx -= 1
    
    S = list(str(input()))
    
    A = []
    
    for _ in range(h):
        A.append(list(map(int,input().split())))
        
    ans = []
        
    for s in S:
        if s == "F":
            sy -= 1
        elif s == "B":
            sy += 1
        elif s == "L":
            sx -= 1
        elif s == "R":
            sx += 1
            
        ans.append(A[sy][sx])
    
    for a in ans:
        print(a)
    
if __name__ == "__main__": 
    main()