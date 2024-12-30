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
    n,m = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    B = []
    W = []
    
    for i in range(m):
        x, y, c = input().split()
        if c == "B":
            B.append((int(x), int(y)))
        if c == "W":
            W.append((int(x), int(y)))
        
    if len(B) == 0 or len(W) == 0:
        print("Yes")
        sys.exit()
    
    x_max = max(B, key=lambda x: x[0])
    y_max = max(B, key=lambda x: x[1])
    
    for w in W:
        x = w[0]
        y = w[1]
        
        if x <= x_max[0] and y <= x_max[1]:
            print("No")
            sys.exit()
        elif x <= y_max[0] and y <= y_max[1]:
            print("No")
            sys.exit()
    
    print("Yes")