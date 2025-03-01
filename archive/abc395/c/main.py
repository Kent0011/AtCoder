import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

sys.setrecursionlimit(10**6)

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
    
    a = set()
    
    left = 0
    right = 0
    ans = float("inf")
    f= False
    
    while(right < n and left <= right):
        if f == False:
            if A[right] in a:
                f = True
                d = A[right]
            else:
                a.add(A[right])
                right += 1
        else:
            if A[left] == d:
                ans = min(ans,right-left+1)
                f = False
                right += 1
            else:
                if A[left] in a:
                    a.remove(A[left])
                left += 1
                
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
    
    

if __name__ == "__main__": 
    main()