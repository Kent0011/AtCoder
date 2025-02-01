import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq


def f(j: int, n: int) -> int:
    # n>>(j+1)<<j の部分：完全なブロックの数を計算
    res = (n >> (j + 1)) << j
    
    # n の j ビット目が 1 の場合
    if n & (1 << j):
        # 残りの部分を計算：n の下位 j ビットの値 + 1
        res += (n & ((1 << j) - 1)) + 1
    
    return res


if __name__ == "__main__":
    n,m = map(int,input().split())
    MOD = 998244353
    
    # 最上位ビットを見つける
    l = n.bit_length()
    
    # 2^l-1までの和を計算
    ans = 0
    for i in range(l):
        if m & (1 << i):
            tmp = f(i,n)
            ans += tmp
            ans %= MOD
    print(ans)