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
    A = list(map(int, input().split()))
    # S = list(str(input()))

    ans = (n-1)*sum(A)
    count = 0

    A.sort()

    def func(left: int, right: int) -> bool:
        if left == right:
            return False
        return A[left]+A[right] >= 10**8

    right = n
    for left in range(n):
        right = max(right, left+1)
        while func(left, right-1):
            right -= 1
        count += n-right

    print(ans-count*10**8)

