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
    # A = []
    aa = []
    for _ in range(n):
        
        m = int(input())
        S = list(map(int,input().split()))
        ans = 0
        tmp = deque()
        tmp.append(0)
        tmp.append(0)
        a = set()
        for i in range(2*m-1):
            
            if S[i] == S[i+1]:
                tmp.append((S[i],S[i+1]))
                tmp.append((S[i+1],S[i]))
                a.add(tmp.popleft())
                a.add(tmp.popleft())
                continue
            if (S[i],S[i+1]) not in a and (S[i+1],S[i]) not in a:
                ...
            else:
                if S[i] != S[i-1]: 
                    ans += 1
            tmp.append((S[i],S[i+1]))
            tmp.append((S[i+1],S[i]))
            a.add(tmp.popleft())
            a.add(tmp.popleft())
        
        aa.append(ans)
    
    for a in aa:
        print(a)
    
    

if __name__ == "__main__": 
    main()