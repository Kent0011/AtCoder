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
    h, w = map(int, input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))

    S = []
    left = 2000
    right = 0
    flag = False

    for i in range(h):
        tmp = list(str(input()))
        S.append(tmp)
        if '#' in tmp:
            if not flag:
                top = i
            flag = True
            bottom = i
            a = tmp.index('#')
            tmp2 = list(reversed(tmp))
            b = w-1-tmp2.index('#')
            left = min(left, a)
            right = max(right, b)

    for i in range(top,bottom+1):
        if "." in S[i][left:right+1]:
            print("No")
            exit()
    print("Yes")
