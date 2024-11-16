import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

# n = int(input())
n,k = map(int,input().split())
# A = list(map(int,input().split()))

S = list(str(input()))

count = 0
flag = False
num = 0
dest1 = []

for i,s in enumerate(S):
    if s == '1' and flag == False:
        flag = True
        count+=1
        num = 1
        dest1.append([0,0])
        dest1[count-1][0] = i
    elif s == '1' and flag == True:
        num +=1
        
    elif s == '0' and flag == True:
        flag = False
        dest1[count-1][1] = num
        
    if i == len(S)-1:
        dest1[count-1][1] = num
        
ans = np.full(n,'0')

dest1[k-1][0] = dest1[k-2][0]+dest1[k-2][1]

for i in range(len(dest1)):
    
    ans[dest1[i][0]:dest1[i][0]+dest1[i][1]] = '1'

ans = list(ans)

print(''.join(ans))
