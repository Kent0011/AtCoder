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
    a, b, c, d, e = map(int, input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))

    point = {"A": a, "B": b, "C": c, "D": d, "E": e}

    L = [
        'ABCDE',
        'BCDE',
        'ACDE',
        'ABDE',
        'ABCE',
        'ABCD',
        'CDE',
        'BDE',
        'ADE',
        'BCE',
        'ACE',
        'BCD',
        'ABE',
        'ACD',
        'ABD',
        'ABC',
        'DE',
        'CE',
        'BE',
        'CD',
        'AE',
        'BD',
        'AD',
        'BC',
        'AC',
        'AB',
        'E',
        'D',
        'C',
        'B',
        'A'
    ]
    
    L = list(map(list, L))
    

    for A in L:
        p = 0
        for a in A:
            p += point[a]
        A.append(p)

    L.sort(key=lambda x: x[:-1])
    L.sort(key=lambda x: x[-1], reverse=True)

    for l in L:
        print("".join(l[:-1]))
