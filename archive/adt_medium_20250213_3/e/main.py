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
    ...
    # n = int(input())
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    # S = list(str(input()))
    
    A = deque(A)
    ans = []
    past = 0
    
    for i in range(m):
        tmp = A.popleft()
        for j in range(past,tmp):
            print(str(tmp-j-1))
        past = tmp