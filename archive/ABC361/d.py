import numpy as np
import math 
import sys


n = int(input())
s = input()
t = input()

ans = n
tmp = 0

if s.count('W') == t.count('W'):
    for i in range(n):
        if s[i]==t[i]:
            ans -=1
            
    
    print(ans)
else:
    print(-1)