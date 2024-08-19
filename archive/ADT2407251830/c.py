import numpy as np
import math 
import sys


n = int(input())

s = []

for i in range(n):
    tmp = input()
    s.append(min(tmp,tmp[::-1]))

s = list(set(s))
ans = len(s)

print(ans)