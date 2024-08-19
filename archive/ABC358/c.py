import numpy as np
import math 
import sys

def check_bit(number, bit_position):
    return (number & (1 << bit_position)) != 0

def check_bit_2(number,size):
    ans = []
    for s in size:
        if check_bit(number,s):
            ans.append(s)
    return ans
        


n,m = map(int,input().split())

s = []

for i in range(n):
    tmp = input().replace('x', '0').replace('o', '1')
    s.append(int(tmp,2))
    
ans = []
M = [i for i in range(m)]

while(len(M) != 0):
    tmp_ans = []
    for j in M:
        tmp = 0
        count = 0
        for i in range(n):
            if check_bit(s[i],j):
                count += 1
                tmp = i
        if count == 1:
            tmp_ans.append(tmp)
            
    if len(tmp_ans) == 0:
        x = 0
        for i in range(n):
            if x < len(check_bit_2(s[i],M)):
                x = len(check_bit_2(s[i],M))
                y = i
        tmp_ans.append(y)

    for t in tmp_ans:
        M = [item for item in M if item not in check_bit_2(s[t],M)]
        
    ans += tmp_ans
    
print(len(set(ans)))