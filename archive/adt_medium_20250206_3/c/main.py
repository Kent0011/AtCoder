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
    x, y, d = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    a = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    
    theta += d * np.pi / 180
    
    print(a * np.cos(theta), a * np.sin(theta))