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
    nodes = defaultdict(list)
    
    for _ in range(n-1):
        u,v = list(map(int,input().split()))
        u -= 1
        v -= 1
        nodes[u].append(v)
        nodes[v].append(u)
    ...
    
    visited = [0] * n
    group = [-1] * n
    group0 = [0]
    group1 = []
    stack = [0]
    
    group[0] = 0
    
    while(stack):
        
        current = stack.pop()
        now = group[current]
        
        for i in nodes[current]:
            if visited[i] == 0:
                stack.append(i)
                if now == 0:
                    group1.append(i)
                    group[i] = 1
                else:
                    group0.append(i)
                    group[i] = 0
                    
        visited[current] = 1
    
    ans = set()
    
    for i in group0:
        for j in group1:
            if not i in nodes[j]:
                x,y = i,j
                if i>j:
                    x,y = j,i
                ans.add((x+1,y+1))

    if len(ans)%2 == 0:
        print('Second')
    else:
        print('First')
        print(*ans.pop())
    
    while(1):
        a,b = map(int, input().split())
        if a == -1 and b == -1:
            return
        ans.discard((a,b))
        print(*ans.pop())

if __name__ == "__main__": 
    main()