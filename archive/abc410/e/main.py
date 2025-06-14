import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque, defaultdict

def check(mid, A, B, h, m):
    link = [[(h,m)]]
    for i in range(1,mid+1):
        ok = False
        l = []
        for tmp in link[-1]:
            l.append((tmp[0] - A[i-1],tmp[1])) if tmp[0] - A[i-1] >= 0 else ...
            l.append((tmp[0],tmp[1] - B[i-1])) if tmp[1] - B[i-1] >= 0 else ...
            if tmp[0] - A[i-1] >= 0 or tmp[1] - B[i-1] >= 0:
                ok = True
        link.append(l)
        if not ok:
            return i-1
    return mid


def main():
    # N (整数)
    # n = int(input())
    
    # N K (整数)
    # n,k = map(int,input().split())
    
    # N M (整数)
    n,h,m = map(int,input().split())
    
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
    B = []
    
    for i in range(n):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
            
    print(check(n, A, B, h, m))

if __name__ == "__main__": 
    main()