import numpy as np
import math 
import sys

n, m = map(int,input().split())

h = list(map(int,input().split()))

ans = 0
flag = False

for alien in h:
    ans += 1
    m = m - alien
    
    if m < 0:
        print(ans-1)
        flag = True
        break
      
if flag == False:
    print(n)