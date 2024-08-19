import numpy as np
import math 
import sys


S = (input())
flag = False
f = False

for i in range(len(S)):
    if S[i] == 'R':
        flag = True
    if S[i] == "M" and flag == True:
        print("Yes")
        f = True
        
if f == False:
    print("No")
