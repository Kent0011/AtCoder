import numpy as np
import math 
import sys

# n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

Y = int(input())

if Y%4 != 0:
    print(365)
    
elif Y%100!=0:
    print(366)

elif Y%400 != 0:
    print(365)

else: print(366)