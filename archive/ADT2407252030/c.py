import numpy as np
import math 
import sys


n = int(input())

s = list(map(int,input().split()))

t = list(map(int,input().split()))

for i in range(n):
    t[i] = min(t[i],t[i-1]+s[i-1])
    
for i in range(n):
    t[i] = min(t[i],t[i-1]+s[i-1])
    
for i in range(n):
    print(t[i])