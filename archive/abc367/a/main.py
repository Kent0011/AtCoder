import numpy as np
import math 
import sys
from functools import lru_cache

# n = int(input())
a,b,c = map(int,input().split())
# A = list(map(int,input().split()))

if b > c:
    c+=24
    
if b<a and a<c:
    print('No')
elif a < b:
    a+=24
    if b<a and a<c:
        print('No')
    else:
        print('Yes')
else:
    print('Yes')

    