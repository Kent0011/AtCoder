import numpy as np
import math 
import sys

s = input()

if len(s) == 1:
    print(s)
else:
    u = 0
    l = 0

    for i in s:
        u += i.isupper()
        l += i.islower()
    
    if u > l:
        print(s.upper())
    else:
        print(s.lower())