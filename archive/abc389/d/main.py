import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect

def is_ok(arg: int) -> bool:

    return (i+0.5)**2 + (arg+0.5)**2 <= r**2


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
    r = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    ans = 0
    
    for i in range(r):
        ans += bisect(2*r, 0, is_ok)+1
    
    print(ans*4 - (r-1)*4 - 3)