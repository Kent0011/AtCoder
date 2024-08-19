import numpy as np
import math 
import sys

# n = int(input())
n,k = map(int,input().split())
# A = list(map(int,input().split()))
S = list(input())

count = 0
for i in range(len(S)):
    if S[i]=='o':
        count+=1
    if count>k:
        S[i] = 'x'
    
print(''.join(S))
