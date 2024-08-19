import numpy as np

n, m, k = map(int,input().split())
c = []
a = []
r = []

for i in range(m):
    tmp = list(map(str,input().split()))
    c.append(int(tmp[0]))
    r.append(tmp.pop())
    a.append(list(map(int,tmp[1:])))

ans = 0

for keys in range(2**n):  #鍵の組
    flag = True
    for j in range(m):   #試行
        ok = 0
        for l in a[j]:   #それぞれの鍵穴
            ok += (keys >> l-1) & 1
        if (ok >= k) ^ (r[j] == 'o'):
            flag = False
            break
    if flag == True:
        ans += 1
        
print(ans)

