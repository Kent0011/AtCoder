import numpy as np
import pandas as pd
import itertools
import math
import sys
from functools import lru_cache
import bisect


if __name__ == "__main__":
    ...
    q = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))

    Q = []  # i番目の蛇のしっぽの位置
    d = 0  # 抜けた蛇の長さの和
    e = 0  # 先頭の蛇のインデックス

    for i in range(q):

        tmp = list(map(int, input().split()))

        if tmp[0] == 1:
            l = tmp[1]

            if len(Q) == 0:
                Q.append(l)
            else:
                Q.append(Q[-1]+l)

        elif tmp[0] == 2:
            d = Q[e]
            e += 1
            
        elif tmp[0] == 3:
            k = tmp[1]

            if k == 1:
                print(0)
            else:
                print(Q[e+k-2]-d)
