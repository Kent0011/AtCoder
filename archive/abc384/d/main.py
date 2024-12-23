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
    n,s = map(int,input().split())
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    s = s % sum(A)
    
    A = A + A
    
    cum = [0]
    
    for a in A:
        cum.append(cum[-1] + a)
        
    cum = set(cum)
        
    for i in cum:
        if i + s in cum:
            print("Yes")
            sys.exit()
    
    print("No")