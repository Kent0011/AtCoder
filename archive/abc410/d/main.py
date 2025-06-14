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
    
    for i in range(m):
        a,b,w = map(int,input().split())
        a -= 1
        b -= 1
        branch[a].append((b,w))
    
    queue = deque([0])
    
    XORs = [set() for _ in range(n)]
    XORs[0].add(0)
    
    while queue:
        now = queue.popleft()
        
        for b,w in branch[now]:
            if not {x ^ w for x in XORs[now]} <= XORs[b]:
                XORs[b] |= {x ^ w for x in XORs[now]}
                queue.append(b)
            
    if len(XORs[n-1]) == 0:
        print(-1)
    else:
        print(min(XORs[n-1]))

if __name__ == "__main__": 
    main()