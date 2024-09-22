import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

G = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    
def dfs(s):
    # 頂点 s からの距離
    dist = [-1] * n
    dist[s] = 0

    # スタックで DFS
    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
                
    return dist

dist0 = dfs(0)

mv = max(enumerate(dist0),key=lambda x: x[1])[0]

dist = dfs(mv)

print(max(dist)+1)