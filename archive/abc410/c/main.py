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
    n,q = map(int,input().split())
    
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
    
    A = [i for i in range(1,n+1)]
    head = 0
    
    for i in range(q):
        tmp = list(map(int,input().split()))
        
        if tmp[0] == 1:
            p = tmp[1] - 1
            x = tmp[2]
            A[(head+p)%n] = x
        elif tmp[0] == 2:
            p = tmp[1] - 1
            print(A[(head+p)%n])
        else:
            k = tmp[1]
            head = (head+k)%n

if __name__ == "__main__": 
    main()