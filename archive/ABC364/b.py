import numpy as np
import math 
import sys

# n = int(input())
h,w = map(int,input().split())
si,sj = map(int,input().split())

C = []

for i in range(h):
    A = list(input())
    C.append(A)
    
X = input()

si-=1
sj-=1

for i in range(len(X)):
    if X[i] == 'L' and sj != 0 and C[si][sj-1] == '.':
        sj-=1
    if X[i] == 'R' and sj != w-1 and C[si][sj+1] == '.':
        sj+=1
    if X[i] == 'U' and si != 0 and C[si-1][sj] == '.':
        si-=1
    if X[i] == 'D' and si != h-1 and C[si+1][sj] == '.':
        si+=1
    
print(si+1,sj+1)