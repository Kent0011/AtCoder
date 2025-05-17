import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque, defaultdict

def comb(N,R):
    return (math.factorial(N)//math.factorial(N-R)//math.factorial(R))


def main():
    # N (整数)
    t = int(input())
    
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
    ...
    
    for _ in range(t):
        n,k = map(int,input().split())
        
        a = len(bin(n)) - 3
        
        ans = (2**a - 1) * comb(a-1,k-1) % 998244353
        
        for i in range(n+1-2**a):
            if bin(i).count("1") == k-1:
                ans = (ans + i+2**a) % 998244353
                
        print(ans)
    

if __name__ == "__main__": 
    main()