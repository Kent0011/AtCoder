import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect

def is_ok(arg: int) -> bool:

    a = 1
    for i in range(1,arg+1):
        a *= i
    return a <= x


def bisect(ng, ok, is_ok):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    ...
    x = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    print(bisect(21, 0, is_ok))