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
    n,k = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    onum = 0
    dotnum = 0
    qnum = 0
    
    que = deque()
    for i,s in enumerate(S):
        if s == 'o':
            onum += 1
            que.append(i)
        elif s == '.':
            dotnum += 1
        elif s == '?':
            qnum += 1

    while que:
        i = que.popleft()
        
        if S[i] == 'o':
            if 0<i:
                if S[i-1] == '?':
                    S[i-1] = '.'
                    qnum -= 1
                    dotnum += 1
            if i+1<n:
                if S[i+1] == '?':
                    S[i+1] = '.'
                    qnum -= 1
                    dotnum += 1
    
    if qnum > k - dotnum:
        print("".join(S))
    else:
        for s in S:
            if s == '?':
                s = 'o'
            else:
                print(s,end='')
        print()
            
if __name__ == "__main__": 
    main()