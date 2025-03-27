import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


def main():
    # N (整数)
    # n = int(input())
    
    # N K (整数)
    # n,k = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    w,r,c = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    fgrid = set()
    fire = [0,0]
    ans = []
    
    fgrid.add((0,0))
    
    for s in S:
        
        if s == 'S':
            r-=1
            fire[0]-=1
            fgrid.add(tuple(fire))
        elif s == 'E':
            c-=1
            fire[1]-=1
            fgrid.add(tuple(fire))
        elif s == 'N':
            r+=1
            fire[0]+=1
            fgrid.add(tuple(fire))
        elif s == 'W':
            c+=1
            fire[1]+=1
            fgrid.add(tuple(fire))
        
        if (r,c) in fgrid:
            ans.append("1")
        else:
            ans.append("0")
        
        
    
    print("".join(ans))
    

if __name__ == "__main__": 
    main()