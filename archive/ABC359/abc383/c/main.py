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
    # n,m = map(int,input().split())
    
    # W H (整数)
    h,w,d = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    # S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    
    que = deque()
    
    A = []
    for i in range(h):
        tmp = list(str(input()))
        for j in range(len(tmp)):
            if tmp[j] == 'H':
                que.append([i,j])
        A.append(tmp)
    
    ans = 0
    grid = [[-1 for _ in range(w)] for _ in range(h)]
    
    for q in que:
        grid[q[0]][q[1]] = 0
        ans += 1
    
    while(que):
        cur = que.popleft()
        
        now = grid[cur[0]][cur[1]]
        
        if cur[0] < h-1:
            if grid[cur[0]+1][cur[1]] == -1 and A[cur[0]+1][cur[1]] == '.':
                grid[cur[0]+1][cur[1]] = now+1
                que.append([cur[0]+1,cur[1]])
                if now+1 <= d:
                    ans+=1
        if cur[0] > 0:
            if grid[cur[0]-1][cur[1]] == -1 and A[cur[0]-1][cur[1]] == '.':
                grid[cur[0]-1][cur[1]] = now+1
                que.append([cur[0]-1,cur[1]])
                if now+1 <= d:
                    ans+=1
        if cur[1] < w-1:
            if grid[cur[0]][cur[1]+1] == -1 and A[cur[0]][cur[1]+1] == '.':
                grid[cur[0]][cur[1]+1] = now+1
                que.append([cur[0],cur[1]+1])
                if now+1 <= d:
                    ans+=1
        if cur[1] > 0:
            if grid[cur[0]][cur[1]-1] == -1 and A[cur[0]][cur[1]-1] == '.':
                grid[cur[0]][cur[1]-1] = now+1
                que.append([cur[0],cur[1]-1])
                if now+1 <= d:
                    ans+=1
        
    print(ans)
    

if __name__ == "__main__": 
    main()