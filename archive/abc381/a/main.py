import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

n = int(input())
# n,k = map(int,input().split())
# A = list(map(int,input().split()))

S = list(str(input()))

if n%2 == 0:
    print("No")
    sys.exit()
    
if S == ["/"]:
    print("Yes")
    sys.exit()

for i in range((n+1)//2-1):
    if S[i] == "1":
        continue
    else:
        print("No")
        sys.exit()

for i in range((n+1)//2,n):
    if S[i] != "2":
        print("No")
        sys.exit()

if S[(n+1)//2-1] == "/":
    print("Yes")
else:
    print("No")