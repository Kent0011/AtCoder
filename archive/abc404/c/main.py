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
    n,m = map(int,input().split())
    
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
    
    branch = defaultdict(list)
    
    for _ in range(m):
        a,b = map(int,input().split())
        branch[a].append(b)
        branch[b].append(a)
        
    if n != m:
        print("No")
        return
    
    for b in branch:
        if len(branch[b]) != 2:
            print("No")
            return
    
    q = deque()
    q.append(1)
    
    visited = set()
    
    while q:
        now = q.popleft()
        visited.add(now)
        for nex in branch[now]:
            if nex not in visited:
                q.append(nex)
    
    if len(visited) != n:
        print("No")
        return
    
    print("Yes")
    

if __name__ == "__main__": 
    main()