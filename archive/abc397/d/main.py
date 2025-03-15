import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque

def make_divisors(N):
    res = []
    for i in range(1,N+1):
        #√N 以下だけ確認
        if i*i > N:
            break
        #iがNの約数でない場合
        if N%i !=0:
            continue
        else:
            res.append(i)
            #N÷i　もNの約数
            if N//i != i:
                res.append(N//i)
    
    res.sort()
    return res


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
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    for a in range(1,int(n**(1/2))):
        
        if n%a != 0:
            continue
        
        y_1 = -1 * ((12*n*a - 3*a**4)**(1/2) + 3*a**2)/(6*a)
        y_2 = ((12*n*a - 3*a**4)**(1/2) - 3*a**2)/(6*a)
        
        if abs(y_1 - np.round(y_1)) < 0.00000000001 and y_1 >0:
            
            y_1 = np.round(y_1)
            ok = (y_1**3 + n)**(1/3)
            
            print(int(np.round(ok)),int(y_1))
            return
            
        if abs(y_2 - np.round(y_2)) < 0.00000000001 and y_2 >0:
            
            y_2 = np.round(y_2)
            ok = (y_2**3 + n)**(1/3)
            print(int(np.round(ok)),int(y_2))
            return
        
    print(-1)
    

if __name__ == "__main__": 
    main()