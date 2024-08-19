import numpy as np
import math 
import sys

sx,sy = map(int,input().split())
tx,ty = map(int,input().split())

if (sx+sy)%2==1:
    sx-=1
if (tx+ty)%2==1:
    tx-=1
    

if abs(sy-ty) >= abs(sx-tx):
    print(abs(sy-ty))
else:
    print((abs(sx-tx)+abs(sy-ty))//2)