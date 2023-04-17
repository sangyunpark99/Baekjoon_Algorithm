n, k = list(map(int, input().split()))

# n은 0부터
# k는 1부터

dp = [[0]*k for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(0, k):
    dp[0][i] = 1

for i in range(1, n+1):
    for j in range(1, k): # 실제로는 2를 의미
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[-1][-1])