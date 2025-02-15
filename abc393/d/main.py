import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


def main(S):
    ones = deque()
    for i in range(len(S)):
        if S[i] == 1:
            ones.append([i,1])
            
    ans = 0
    
    while(1):
        if len(ones) <= 2:
            break
        left = ones.popleft()
        right = ones.pop()
        ones[0][1]+=left[1]
        ones[-1][1]+=right[1]
        ans += (ones[0][0] - left[0] - 1)*left[1]
        ans += (right[0] - ones[-1][0] - 1)*right[1]
    
    if len(ones) == 2:
        ans += (ones[1][0] - ones[0][0] - 1) * min(ones[0][1],ones[1][1])
    
    print(ans)
    
    
    
    

if __name__ == "__main__":
    n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    S = list(str(input()))
    S = list(map(int,S))
    
    main(S)