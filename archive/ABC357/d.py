import numpy as np
import math 
import sys


n = int(input())

m = str(n)

ans = n

for i in range(n-1):
    ans = ans*(10**len(m))
    ans = (ans + n)%998244353
    
print(ans)