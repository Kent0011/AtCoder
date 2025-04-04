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
    
    branch = defaultdict(set)
    
    for _ in range(m):
        u,v = list(map(int,input().split()))
        u -=1
        v -=1
        
        branch[u].add(v)
        branch[v].add(u)
        
    
    ans = 0
    parent = [-1] * n
    visited = [False] * n
    stack = deque()
    stack.append(0)
    count = n
    ff = False
    
    while count > 0:
        flag = False
        while stack:
            now = stack.popleft()
            visited[now] = True
            count -= 1
            for nex in branch[now]:
                if nex != parent[now]:
                    if visited[nex]:
                        ans += 1
                        ff = True
                        z = nex
                        w = now
                        print(z,w)
                        break
                    else:
                        stack.append(nex)
                        parent[nex] = now
            if ff:
                branch[z].discard(w)
                branch[w].discard(z)
            if count == 0:
                break
        for i,v in enumerate(visited):
            if not v:
                stack.append(i)
                flag = True
                break
        if not flag:
            print(ans)
            return

    
    

if __name__ == "__main__": 
    main()