import sys

t = int(input())


def ans(num):
    dp = [0] * (num+3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])


for _ in range(t):
    value = int(sys.stdin.readline().rstrip())
    ans(value)