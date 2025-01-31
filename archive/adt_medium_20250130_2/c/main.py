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
    h, m = map(int, input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))

    while 1:
        a = h//10
        b = h % 10
        c = m//10
        d = m % 10
        
        if a*10 + c < 24 and b*10 + d < 60:
            break
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0

    print(h, m)
