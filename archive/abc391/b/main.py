import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq


if __name__ == "__main__":
    ...
    # n = int(input())
    n,m = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    S = []
    T = []
    
    for _ in range(n):
        S.append(list(str(input())))
        
    for _ in range(m):
        T.append(list(str(input())))
    
    S = np.array(S)
    T = np.array(T)
        
    for i in range(n-m+1):
        for j in range(n-m+1):
            
            flag = False
            for k in range(m):
                for l in range(m):
                    
                    if S[i+k, j+l] != T[k,l]:
                        flag = True
                        break
                if flag == True:
                    break
            if flag == False:   
                print(i+1,j+1)
                exit()
                
