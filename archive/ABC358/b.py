import numpy as np
import math 
import sys

n, a = map(int,input().split())

T = list(map(int,input().split()))

tmp = 0
for i in range(n):
    if i == 0:
        tmp = T[i]+a
        print(tmp)
    else:
        tmp = max(T[i]+a,tmp+a)
        print(tmp)
        