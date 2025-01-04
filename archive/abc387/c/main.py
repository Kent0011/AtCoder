import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect

def is_snake(x:int) -> bool:
    
    x = list(str(x))
    
    head = int(x.pop(0))
    
    for i in x:
        if int(i) >= head:
            return False
    return True

def next_snake(x: int) -> int:
    x = list(str(x))
    x_len = len(x)
    
    head = int(x[0])
    ans = []
    
    for i in range(x_len):
        a = int(x.pop())
        if a+1 < head:
            ans.insert(0, str(a+1))
            return int("".join(x+ans))
        else:
            ans.insert(0, str(0))
    ans = ["0" for _ in range(x_len-1)]
    ans.insert(0, str(head+1))
    return int("".join(ans))


if __name__ == "__main__":
    ...
    # n = int(input())
    l,r = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))
    
    l_x = np.full(len(list(str(l))),"0").tolist()
    l_x[0] = str(int(list(str(l))[0])+1)
    L = int(list("".join(l_x))[0])
    l_x = int("".join(l_x))
    
    r_x = np.full(len(list(str(r))),"0").tolist()
    r_x[0] = str(int(list(str(r))[0]))
    R = int(r_x[0])
    r_x = int("".join(r_x))
    
    ans = 0
    
    if is_snake(l):
        ans += 1
    
    while(1):
        l = next_snake(l)
        if l >= r:
            print(ans)
            sys.exit()
        if l == l_x:
            break
        ans += 1


    while(1):
        ans+=len(list(itertools.product(range(L), repeat=len(list(str(l_x)))-1)))
        L+=1
        tmp = list(str(l_x))
        tmp.pop(0)
        if [str(L)] + tmp == list(str(r_x)):
            break
    
    while(1):
        r_x = next_snake(r_x)
        if r_x >= r:
            print(ans)
            sys.exit()
        ans += 1