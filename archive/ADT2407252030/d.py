import numpy as np
import math 
import sys

n = int(input())

A = list(map(int,input().split()))
B = [0]


for a in A:
    B.append(max(B[-1]+a,0))

print(B.pop())