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
    n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    T = list(str(input()))
    ans = [0, 0]

    f = 'E'

    for t in T:
        if t == 'S':
            if f == 'E':
                ans[0] += 1
            elif f == 'N':
                ans[1] += 1
            elif f == 'W':
                ans[0] -= 1
            elif f == 'S':
                ans[1] -= 1
        else:
            if f == 'E':
                f = 'S'
            elif f == 'N':
                f = 'E'
            elif f == 'W':
                f = 'N'
            elif f == 'S':
                f = 'W'
    
    print(*ans)
        