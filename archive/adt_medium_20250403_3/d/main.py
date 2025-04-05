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
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    S = []
    S.append(list(str(input())))
    S.append(list(str(input())))
    S.append(list(str(input())))
    
    # S1 S2 S3 ... Sn (文字列)
    # S = list(map(str,input().split()))
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    T = list(map(int,list(str(input()))))
    
    ans = []
        
    
    for i in range(len(T)):
        if T[i] == 1:
            ans.extend(S[0])
        elif T[i] == 2:
            ans.extend(S[1])
        elif T[i] == 3:
            ans.extend(S[2])
    
    print("".join(ans))
    
    

if __name__ == "__main__": 
    main()