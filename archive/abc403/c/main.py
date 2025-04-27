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
    n,m,q = map(int,input().split())
    
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
    users = defaultdict(set)
    masterusers = set()
    
    for _ in range(q):
        A = list(map(int,input().split()))
        if A[0] == 1:
            users[A[1]].add(A[2])
        elif A[0] == 2:
            masterusers.add(A[1])
        elif A[0] == 3:
            if A[2] in users[A[1]] or A[1] in masterusers:
                print('Yes')
            else:
                print('No')

if __name__ == "__main__": 
    main()