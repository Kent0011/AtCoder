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
    dragon_stack = [[i,0] for i in range(n,0,-1)]
    
    for _ in range(q):
        x,y = map(str,input().split())
        x = int(x)

        
        if x == 1:
            c = y
            head = dragon_stack[-1].copy()
            if c == 'L':
                head[0] -= 1
                dragon_stack.append(head)
            elif c == 'R':
                head[0] += 1
                dragon_stack.append(head)
            elif c == 'U':
                head[1] += 1
                dragon_stack.append(head)
            elif c == 'D':
                head[1] -= 1
                dragon_stack.append(head)
        elif x == 2:
            p = int(y)
            print(*dragon_stack[-1*p])
            

if __name__ == "__main__": 
    main()