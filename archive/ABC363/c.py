import numpy as np
import math 
import sys


def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

def ispalindrome(a: list) -> bool:
    n = len(a)
    for i in range(n//2):
        if a[i] != a[-i-1]:
            return False
    return True




n,k = map(int,input().split())
s = sorted(list(input()))

ans = 0

flag = False
for i in range(n-k+1):
    if ispalindrome(s[i:i+k]):
        flag = True
if flag == False:
    ans+=1
    

while next_permutation(s,0):
    flag = False
    for i in range(n-k+1):
        if ispalindrome(s[i:i+k]):
            flag = True
    if flag == False:
        ans+=1

print(ans)
