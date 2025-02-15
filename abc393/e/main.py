import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])
    
    if arr==[]:
        arr.append([n, 1])
        
    return arr


def main():
    ...

if __name__ == "__main__":
    # n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    main()