import numpy as np
import math 
import sys

n,x,y = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

R = list(zip(A,B))

R_a = sorted(R,key=lambda x:x[0])
R_b = sorted(R,key=lambda x:x[1])

