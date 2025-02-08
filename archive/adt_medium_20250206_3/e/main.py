import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq

def root_5(x,y):
    ans = set()
    ans.add((x+2,y+1))
    ans.add((x+2,y-1))
    ans.add((x-2,y+1))
    ans.add((x-2,y-1))
    ans.add((x+1,y+2))
    ans.add((x+1,y-2))
    ans.add((x-1,y+2))
    ans.add((x-1,y-2))
    return ans


if __name__ == "__main__":
    ...
    # n = int(input())
    x_1, y_1, x_2, y_2 = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    tmp = root_5(x_1, y_1)
    tmp2 = root_5(x_2, y_2)
    
    a = tmp | tmp2
    
    if len(a) == 16:
        print('No')
    else:
        print('Yes')