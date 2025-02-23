import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

def num_of_children(node: int, branches: dict, table: list):
    table[node] = 0
    ans = 0
    for child in branches[node]:
        if table[child] == -1:
            ans += (1+num_of_children(child,branches,table))
            
    return ans
    


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
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    
    # 連結ノードを辞書で管理
    branch = {}
    for i in range(n-1):
        u,v = map(int,input().split())
        u-=1
        v-=1
        
        if u not in branch:
            branch[u] = []
        if v not in branch:
            branch[v] = []  
        branch[u].append(v)
        branch[v].append(u)
    
    
    # 子孫ノードの数を管理する木DPテーブル
    table = [0]*n
    
    # 帰りがけ順でDFSし、子孫ノードの数を数える
    Q = deque()
    for node in branch[0]:
        Q.append((node,0,False))
        
    while(Q):
        node,parent,flag = Q.pop()
        
        if flag:
            for child in branch[node]:
                if child != parent:
                    table[node] += table[child]+1
                    
        else:
            if len(branch[node]) == 1:
                table[node] = 0
            else:
                Q.append((node,parent,True))
                
            for child in branch[node]:
                if child != parent:
                    Q.append((child,node,False))
    
    for node in branch[0]:
        table[0] += table[node]+1
    
    tmp = 0
    for node in branch[0]:
        tmp = max(tmp,table[node]+1)
    print(table[0]-tmp+1)
    

if __name__ == "__main__": 
    main()