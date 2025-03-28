import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
S = str(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

S_list = {}

S_list['a'] = 0
S_list['t'] = 0
S_list['c'] = 0
S_list['o'] = 0
S_list['d'] = 0
S_list['e'] = 0
S_list['r'] = 0

for s in S:
    if s == 'a':
        S_list['a'] += 1
    elif s == 't':
        S_list['t'] += S_list['a']
    elif s == 'c':
        S_list['c'] += S_list['t']
    elif s == 'o':
        S_list['o'] += S_list['c']
    elif s == 'd':
        S_list['d'] += S_list['o']
    elif s == 'e':
        S_list['e'] += S_list['d']
    elif s == 'r':
        S_list['r'] += S_list['e']

print(S_list['r']%(10**9+7))