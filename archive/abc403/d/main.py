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
    n,d = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    # w,h = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    A = list(map(int,input().split()))
    
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
    
    if d == 0:
        A_set = set(A)
        print(len(A)-len(A_set))
        return
    
    ...
    A.sort()
    ans = 0
    
    mods = [{} for _ in range(d)]
    mod_num = [0 for _ in range(d)]
    
    max_mod = [0 for _ in range(d)]
    
    for a in A:
        if a//d in mods[a%d]:
            mods[a%d][a//d] += 1
        else:
            mods[a%d][a//d] = 1
        mod_num[a%d] += 1
        max_mod[a%d] = max(max_mod[a%d],a//d)
        
    for i,mod in enumerate(mods):
        dp = [0]
        First = True
        for m in range(max_mod[i]+1):
            if First:
                dp.append(mod.get(m,0))
                First = False
            else:
                dp.append(max(dp[-1],dp[-2]+mod.get(m,0)))
                
        ans += mod_num[i] - dp[-1]
            
    print(ans)
if __name__ == "__main__": 
    main()