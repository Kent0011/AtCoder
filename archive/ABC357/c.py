N=int(input())

for i in range(3**N):
  ans=""
  for j in range(3**N):
    nFlg=0
    for n in range(N):
      if i%3**(n+1)>=3**n and i%3**(n+1)<2 * 3**n \
         and j%3**(n+1)>=3**n and j%3**(n+1)<2 * 3**n:
        nFlg=1
        break
    if nFlg:ans+="."
    else:ans+="#"
  print(ans)