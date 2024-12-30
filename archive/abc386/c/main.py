import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect


if __name__ == "__main__":
    ...
    # n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    K = int(input())
    S = list(str(input()))
    T = list(str(input()))
    
    
    if len(S) == len(T):
        for i, s in enumerate(S):
            if s == T[i]:
                continue
            else:
                S[i] = T[i]
                break
    
    elif len(S) - len(T) == 1:
        for i, s in enumerate(S):
            if i == len(S) - 1:
                S.pop(i)
                break
            if s == T[i]:
                continue
            else:
                S.pop(i)
                break
    
    elif len(T) - len(S) == 1:
        for i, t in enumerate(T):
            if i == len(T) - 1:
                T.pop(i)
                break
            if t == S[i]:
                continue
            else:
                T.pop(i)
                break
        
    if S == T:
        print("Yes")
    else:
        print("No")