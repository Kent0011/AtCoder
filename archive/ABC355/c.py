import numpy as np
import math 
import sys

n,t = map(int,input().split())

a = list(map(int,input().split()))
    
column = np.zeros(n)
row = np.zeros(n)
diagonal = np.zeros(2)

count = 0
flag = False
for i in a:
    count += 1
    
    if row[int((i-1)/n)] == n-1:
        print(count)
        flag = True
        break
    else:
        row[int((i-1)/n)] += 1
        
    if column[(i-1)%n] == n-1:
        print(count)
        flag = True
        break
    else:
        column[(i-1)%n] += 1
        
        
    if (i-1)//n == (i-1)%n:
        if diagonal[0] == n-1:
            print(count)
            flag = True
            break
        else:
            diagonal[0] += 1
            
    if n - (i-1)//n - 1 == (i-1)%n:
        if diagonal[1] == n-1:
            print(count)
            flag = True
            break
        else:
            diagonal[1] += 1
        

if flag == False:
    print(-1)