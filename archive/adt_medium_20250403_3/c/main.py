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
    n,t = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    C = list(map(int,input().split()))
    R = list(map(int,input().split()))
    
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
    
    winner = False
    max_score = 0
    for i in range(n):
        if C[i] == t:
            if max_score < R[i]:
                max_score = R[i]
                winner = i+1
    
    if not winner:
        t = C[0]
        for i in range(n):
            if C[i] == t:
                if max_score < R[i]:
                    max_score = R[i]
                    winner = i+1
    
    print(winner)

if __name__ == "__main__": 
    main()