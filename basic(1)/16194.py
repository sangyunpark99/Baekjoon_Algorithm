n = int(input())
p = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = p[i]
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + dp[i-j-1])


print(dp[n-1])