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
    n, m = map(int, input().split())
    P = np.array(list(map(int, input().split())))
    # S = list(str(input()))

    A = []

    # Pのコピー
    for i, p in enumerate(P):
        A.append([p, 0, i])

    heapq.heapify(A)

    mm = 0  # 買った金額の合計
    ans = 0  # 買った個数

    while A and mm < m:  # Aが空でないことを確認
        x = heapq.heappop(A)
        if mm + x[0] > m:  # 予算をオーバーするかチェック
            break
        mm += x[0]
        x[1] += 1
        x[0] = P[x[2]] * (x[1]+1)**2 - P[x[2]] * (x[1])**2
        ans += 1
        heapq.heappush(A, x)

    print(ans)  # 最後の無効な購入を差し引く必要がないので、-1を削除
