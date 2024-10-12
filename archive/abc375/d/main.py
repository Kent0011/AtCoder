import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))
s = list(str(input()))

def find_duplicate_indices(arr):
    ans = 0
    # 要素の出現回数を保持する辞書
    element_count = {}
    count = {}
    
    # 各要素の出現回数をカウント
    for index, value in enumerate(arr):
        if value in element_count:
            ans += count[value]*(index-1) - element_count[value]
            element_count[value]+=index
            count[value] += 1
        else:
            element_count[value] = index
            count[value] = 1
            
            
    return ans

A = find_duplicate_indices(s)
        
print(A)