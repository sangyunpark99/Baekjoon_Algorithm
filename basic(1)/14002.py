n = int(input())

nums = list(map(int, input().split()))

dp = [0] * n
dp_list = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            dp_list[i] = dp_list[j][:] # 얕은 복사
    dp[i] += 1
    dp_list[i].append(nums[i])

max_value = max(dp)
max_index = 0

for i in range(n):
    if dp[i] == max_value:
        max_index = i
        break
print(max_value)
print(*dp_list[max_index])
