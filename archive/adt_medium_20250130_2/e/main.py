import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq

def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
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



if __name__ == "__main__":
    ...
    # n = int(input())
    h, w = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    A = []
    l = h + w - 2
    ans = 0
    
    for i in range(h):
        A.append(list(map(int,input().split())))
        
    L = [0 for _ in range(w-1)] + [1 for _ in range(h-1)]
    
    a = set()
    a.add(A[0][0])
    tmp = [0,0]
    flag = True
    for j in L:
        if j == 1:
            tmp = [tmp[0] + 1, tmp[1]]
            if tmp[0] >= h or tmp[1] >= w:
                flag = False
                break
            if A[tmp[0]][tmp[1]] in a:
                flag = False
                break
            a.add(A[tmp[0]][tmp[1]])
        else:
            tmp = [tmp[0], tmp[1] + 1]
            if tmp[0] >= h or tmp[1] >= w:
                flag = False
                break
            if A[tmp[0]][tmp[1]] in a:
                flag = False
                break
            a.add(A[tmp[0]][tmp[1]])
    if flag:
        ans += 1
        
    while next_permutation(L):
        a = set()
        a.add(A[0][0])
        tmp = [0,0]
        flag = True
        for j in L:
            if j == 1:
                tmp = [tmp[0] + 1, tmp[1]]
                if tmp[0] >= h or tmp[1] >= w:
                    flag = False
                    break
                if A[tmp[0]][tmp[1]] in a:
                    flag = False
                    break
                a.add(A[tmp[0]][tmp[1]])
            else:
                tmp = [tmp[0], tmp[1] + 1]
                if tmp[0] >= h or tmp[1] >= w:
                    flag = False
                    break
                if A[tmp[0]][tmp[1]] in a:
                    flag = False
                    break
                a.add(A[tmp[0]][tmp[1]])
        if flag:
            ans += 1
    print(ans)