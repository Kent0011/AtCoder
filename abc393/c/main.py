import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


if __name__ == "__main__":
    # n = int(input())
    n,m = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    branch = set()
    for i in range(n):
        branch.add((i,i))
    cnt = 0
    
    for i in range(m):
        u,v = map(int,input().split())
        u-=1
        v-=1
        if u>v:
            u,v = v,u
        if (u,v) in branch:
            cnt+=1
        else:
            branch.add((u,v))
    
    print(cnt)