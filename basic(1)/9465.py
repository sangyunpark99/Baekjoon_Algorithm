T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, n):
            for j in range(2):
                if j == 0:
                    dp[j][i] = max(dp[j + 1][i - 1] + dp[j][i], dp[j + 1][i - 2] + dp[j][i])
                else:
                    dp[j][i] = max(dp[j - 1][i - 1] + dp[j][i], dp[j - 1][i - 2] + dp[j][i])

    print(max(dp[0][-1], dp[1][-1]))