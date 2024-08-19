import numpy as np
import math 
import sys

n = int(input())
# n,k = map(int,input().split())
A = list(map(int,input().split()))


B = sorted(A)

print(A.index(B[-2])+1)