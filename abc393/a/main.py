import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque


def main(s_1, s_2):
    
    if s_1 == s_2:
        if s_1 == 'sick':
            print(1)
        else:
            print(4)
    else:
        if s_1 == 'sick':
            print(2)
        else:
            print(3)

if __name__ == "__main__":
    # n = int(input())
    # n,k = map(int,input().split())
    s_1, s_2 = map(str,input().split())
    # S = list(str(input()))
    
    main(s_1, s_2)