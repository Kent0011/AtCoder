import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

if n%2 == 1:
    sys.exit()

ans1 = ['(' for _ in range(n//2)]
ans2 = [')' for _ in range(n//2)]

ans = ans1 + ans2

ans.sort()

print(''.join(ans))
while next_permutation(ans):
    count = 0
    flag = True
    for a in ans:
        if a == '(':
            count+=1
        if a == ')':
            count-=1
        if count<0:
            flag = False
            break

    if flag:print(''.join(ans))