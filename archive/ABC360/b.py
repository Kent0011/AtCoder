import numpy as np
import math 
import sys


S, T = map(str,input().split())
f = False

W = range(len(S))

for w in W:
    for i in range(w):
        X=S[i:]
        if T == X[::w]:
            print("Yes")
            f = True
            break
    if f == True:
        break

if f == False:
    print('No')
        
        
