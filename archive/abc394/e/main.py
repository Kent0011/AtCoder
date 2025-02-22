import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

def ispalindrome(a: list) -> bool:
    n = len(a)
    for i in range(n//2):
        if a[i] != a[-i-1]:
            return False
    return True


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
    A = {}
    for i in range(n):
        tmp = list(str(input()))
        for j in range(n):
            if tmp[j] != '-':
                A[i] = [j,tmp[j]]
    ...
    X = []
    for i in range(n):
        ans = []
        for j in range(n):
            start = i
            goal = j
            # 情報のテーブルを初期化 今回は頂点 start からの距離
            dist = [[] for _ in range(n)]
            dist[start] = 0

            Q = deque([start])

            # stackが空になるまで
            flag = False
            while Q:
                current_node = Q.popleft()

                # 注目ノードと連結しているノード
                for next_node in A.get(current_node, False):
                    if not next_node:
                        continue
                    print(next_node)
                    if dist[next_node[0]] == []: # -1:　 未探索
                        Q.append(next_node[0]) # スタックに追加
                        # 情報を追加　今回は始点からの距離
                        dist[next_node[0]] = dist[current_node]+next_node[1]
                        
                if len(dist[goal]) > 0 and ispalindrome(dist[goal]):
                    flag = True
                    break
            if flag:
                ans.append(dist[goal])
            else:
                ans.append(-1)
        X.append(ans)
    
    for i in range(n):
        print(*X[i])

if __name__ == "__main__": 
    main()