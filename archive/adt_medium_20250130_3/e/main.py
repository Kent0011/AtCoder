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
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # S = list(str(input()))

    print(max(A)+max(B))