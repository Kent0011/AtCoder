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
    
    a = ["#" for _ in range(n)]
    ans = []
    
    if n%2 == 0:
        f = 0
    else:
        f = 1
    
    
    for i in range(n//2):
        ans.append(a.copy())
        if i%2 == 0:
            for j in range(n-2*i-2):
                a[i+j+1] = "."
        else:
            for j in range(n-2*i-2):
                a[i+j+1] = "#"
    
    if f == 1:
        ans.append(a)
    
    ans2 = ans.copy()
    ans2.reverse()
    
    if f == 1:
        ans2.pop(0)
    
    ans = ans + ans2
    
    for i in range(n):
        print("".join(ans[i]))

if __name__ == "__main__": 
    main()