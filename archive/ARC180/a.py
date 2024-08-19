import numpy as np
import math 
import sys

N = int(input())

S = input()

ans = 1
n = N

while(1):
    
    for i in range(n):
        if S[i-1] == S[i+1] and S[i+1] != S[i]:
            ans += 1
    n = n-2