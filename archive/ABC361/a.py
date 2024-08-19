import numpy as np
import math 
import sys


n,k,x = map(int,input().split())

A = list(map(int,input().split()))

A.insert(k,x)

print(*A)