import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,l = map(int,input().split())
k = int(input())
A = list(map(int,input().split()))
A.append(l)

def is_ok(arg: int) -> bool:
    current = 0
    count = 0
    for a in A:
        if a-current >= arg:
            count+=1
            current = a
    return count > k


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(l+1,0))