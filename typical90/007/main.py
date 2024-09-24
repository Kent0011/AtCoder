import numpy as np
import math 
import sys
from functools import lru_cache
import itertools



n = int(input())
# n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

q = int(input())

def is_ok(b: int, arg: int) -> bool:
    # 条件を満たすかどうか？問題ごとに定義
    return arg<n and b>=A[arg] or arg<0


def meguru_bisect(b, ng, ok):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(b,mid):
            ok = mid
        else:
            ng = mid
    return ok


for _ in range(q):
    b = int(input())
    
    ans = meguru_bisect(b,n,-1)
    if ans >=n-1:
        print(abs(b-A[ans]))
    else:
        print(min(abs(b-A[ans]),abs(b-A[ans+1])))
    
