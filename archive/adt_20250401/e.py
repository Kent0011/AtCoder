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
    
    branch = [[] for _ in range(n)]
    
    for _ in range(m):
        u,v = list(map(int,input().split()))
        u -=1
        v -=1
        
        branch[u].append(v)
        branch[v].append(u)
        
    
    ans = 0
    visited = [False] * n
    stack = deque()
    
    for i in range(n):
        if not visited[i]:
            stack.append(i)
        else:
            continue
        
        while stack:
            now = stack.popleft()
            for nex in branch[now]:
                if not visited[nex]:
                    visited[nex] = True
                    stack.append(nex)
            
        ans += 1
        
        
    print(ans)


if __name__ == "__main__": 
    main()