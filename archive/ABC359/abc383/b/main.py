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
    h,w,d = map(int,input().split())
    
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
    for _ in range(h):
        A.append(list(str(input())))
    ...
    
    ans = 0
    
    for i in range(h):
        for j in range(w):
            if A[i][j] == '#':
                continue
            for ii in range(h):
                for jj in range(w):
                    if A[ii][jj] == '#':
                        continue
                    num = 0
                    for iii in range(h):
                        for jjj in range(w):
                            if A[iii][jjj] == '#':
                                continue
                            if abs(iii-i)+abs(jjj-j) <= d or abs(iii-ii)+abs(jjj-jj) <= d:
                                num+=1
                    ans = max(num,ans)
    
    print(ans)

if __name__ == "__main__": 
    main()