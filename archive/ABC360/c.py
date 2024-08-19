N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

Box = [[A[i],W[i]] for i in range(N)]
Box = sorted(Box, reverse=False, key=lambda x: x[0])

ans = 0
n = 0
Max = 0
for i in range(N):
    ans += Box[i][1]
    if Box[i][0] == n:
        Max = max(Max, Box[i][1])
    else:
        n = Box[i][0]
        ans -= Max
        Max = Box[i][1]
ans -= Max

print(ans)
