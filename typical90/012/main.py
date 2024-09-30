import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

def dfs(start, end, edges):
    # 情報のテーブルを初期化 今回は頂点 start からの距離
    nodes = [[0 for _ in range(w)]for _ in range(h)]
    nodes[start[0]][start[1]] = 1

    stack = [start]
    
    # stackが空になるまで
    while stack:
        current_r,current_c = stack.pop()
        
        # 注目ノードと連結しているノード
        for next_r,next_c in edges[current_r][current_c]:
            if nodes[next_r][next_c] == 0:
                stack.append([next_r, next_c]) # スタックに追加
                nodes[next_r][next_c] = 1
                
            if nodes[end[0]][end[1]] == 1:
                return True
            
    if nodes[end[0]][end[1]] == 1:
        return True
    else:
        return False

# n = int(input())
h,w = map(int,input().split())
q = int(input())
# A = list(map(int,input().split()))

X = np.zeros((h,w))
edges = [[[] for _ in range(w)]for _ in range(h)]

for i in range(q):
    A = list(map(int,input().split()))
    
    if A[0] == 1:
        r,c = A[1]-1,A[2]-1
        X[r][c] = 1
        
        if r>0 and X[r-1][c] == 1:
            edges[r][c].append([r-1,c])
            edges[r-1][c].append([r,c])
        if r<h-1 and X[r+1][c] == 1:
            edges[r][c].append([r+1,c])
            edges[r+1][c].append([r,c])
        if c>0 and X[r][c-1] == 1:
            edges[r][c].append([r,c-1])
            edges[r][c-1].append([r,c])
        if c<w-1 and X[r][c+1] == 1:
            edges[r][c].append([r,c+1])
            edges[r][c+1].append([r,c])
            
    else:
        r_1,c_1 = A[1]-1,A[2]-1
        r_2,c_2 = A[3]-1,A[4]-1
        if X[r_1][c_1] == 1 and X[r_2][c_2] == 1:
            if dfs([r_1,c_1],[r_2,c_2],edges):
                print('Yes')
            else:
                print('No')
        else:
            print('No')