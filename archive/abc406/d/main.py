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
    h,w,n = map(int,input().split())
    
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
    
    trashi = defaultdict(list)
    trashj = defaultdict(list)
    inum = [0 for _ in range(h)]
    jnum = [0 for _ in range(w)]
    for _ in range(n):
        a,b = map(int,input().split())
        trashi[a-1].append(b-1)
        trashj[b-1].append(a-1)
        inum[a-1] += 1
        jnum[b-1] += 1
        
    q = int(input())
    for _ in range(q):
        a,b = map(int,input().split())
        
        if a == 1:
            print(inum[b-1])
            if inum[b-1] > 0:
                for i in trashi[b-1]:
                    jnum[i] = max(0,jnum[i]-1)
                trashi[b-1] = []
            inum[b-1] = 0
        else:
            print(jnum[b-1])
            if jnum[b-1] > 0:
                for i in trashj[b-1]:
                    inum[i] = max(0,inum[i]-1)
                trashj[b-1] = []
            jnum[b-1] = 0

if __name__ == "__main__": 
    main()