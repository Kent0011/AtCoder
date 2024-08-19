import numpy as np
import math 
import sys

n = int(input())
A = []
for i in range(n):
    s,t = map(str,input().split())
    A.append([s,int(t)])

origin = set()
score = 0
ans = 0

for i in range(n):
    if A[i][0] in origin:
        continue
    if score < A[i][1]:
        score = A[i][1]
        ans = i+1
    origin.add(A[i][0])

print(ans)
    