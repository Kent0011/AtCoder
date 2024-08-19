import numpy as np
import math 
import sys

n, k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Blist = []

for i in range(k):
    Blist.append(A[B[i]-1])

if max(A) == max(Blist):
    print('Yes')
else:
    print('No')