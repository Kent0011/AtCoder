import numpy as np
import math 
import sys
from functools import lru_cache
import itertools
import copy


n = int(input())

def rotate_3(i,j):
    return [j,n-1-i]

def rotate_2(i,j):
    return [n-1-i,n-1-j]

def rotate_1(i,j):
    return [n-1-j,i]


A = []

for i in range(n):
    A.append(list(str(input())))

Ans = copy.deepcopy(A)

for i,a in enumerate(Ans):
    for j in range(len(a)):
        if i < n//2 and j < n//2:
            if min(i,j)%4 == 3:
                Ans[i][j] = A[i][j]
            elif min(i,j)%4 == 0:
                Ans[i][j] = A[rotate_1(i,j)[0]][rotate_1(i,j)[1]]
            elif min(i,j)%4 == 1:
                Ans[i][j] = A[rotate_2(i,j)[0]][rotate_2(i,j)[1]]
            elif min(i,j)%4 == 2:
                Ans[i][j] = A[rotate_3(i,j)[0]][rotate_3(i,j)[1]]
                
        elif i < n//2 and j >= n//2:
            if min(i,n-j-1)%4 == 3:
                Ans[i][j] = A[i][j]
            elif min(i,n-j-1)%4 == 0:
                Ans[i][j] = A[rotate_1(i,j)[0]][rotate_1(i,j)[1]]
            elif min(i,n-j-1)%4 == 1:
                Ans[i][j] = A[rotate_2(i,j)[0]][rotate_2(i,j)[1]]
            elif min(i,n-j-1)%4 == 2:
                Ans[i][j] = A[rotate_3(i,j)[0]][rotate_3(i,j)[1]]
                
        elif i >= n//2 and j < n//2:
            if min(n-i-1,j)%4 == 3:
                Ans[i][j] = A[i][j]
            elif min(n-i-1,j)%4 == 0:
                Ans[i][j] = A[rotate_1(i,j)[0]][rotate_1(i,j)[1]]
            elif min(n-i-1,j)%4 == 1:
                Ans[i][j] = A[rotate_2(i,j)[0]][rotate_2(i,j)[1]]
            elif min(n-i-1,j)%4 == 2:
                Ans[i][j] = A[rotate_3(i,j)[0]][rotate_3(i,j)[1]]
                
        elif i >= n//2 and j >= n//2:
            if min(n-i-1,n-j-1)%4 == 3:
                Ans[i][j] = A[i][j]
            elif min(n-i-1,n-j-1)%4 == 0:
                Ans[i][j] = A[rotate_1(i,j)[0]][rotate_1(i,j)[1]]
            elif min(n-i-1,n-j-1)%4 == 1:
                Ans[i][j] = A[rotate_2(i,j)[0]][rotate_2(i,j)[1]]
            elif min(n-i-1,n-j-1)%4 == 2:
                Ans[i][j] = A[rotate_3(i,j)[0]][rotate_3(i,j)[1]]
                

for a in Ans:
    print(''.join(a))