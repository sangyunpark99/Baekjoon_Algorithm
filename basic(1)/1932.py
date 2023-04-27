import sys

n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

if n == 1:
    print(dp[0][0])
    exit()

dp[1][0] = dp[0][0] + dp[1][0]
dp[1][1] = dp[0][0] + dp[1][1]

for i in range(2, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][0] += dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][len(dp[i])-1] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))
