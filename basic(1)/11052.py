import sys

n = int(sys.stdin.readline())

money = list(map(int, sys.stdin.readline().split()))
money.insert(0, 0) # 인덱스 안헷갈리려고

dp = [0] * (n+1)

dp[1] = money[1]

for i in range(2, n+1):
    dp[i] = money[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

print(dp[n])