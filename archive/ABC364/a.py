import numpy as np
import math 
import sys

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

n = int(input())

flag1 = False
flag2 = False
ans = 0

for i in range(n):
    if flag2 == True:
        ans = 1
    s = input()
    if s == 'sweet':
        if flag1 == True:
            flag2 = True
        else:
            flag1 = True
    else:
        flag1 = False
        flag2 = False

if ans == 0:
    print('Yes')
else:
    print('No')
        
    