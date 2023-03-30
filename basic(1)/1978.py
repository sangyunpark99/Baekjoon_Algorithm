n = int(input())
nums = list(map(int, input().split()))
ans = 0

for num in nums:
    count = 0
    if num == 1:
        continue
    for i in range(1,num):
        if num % i == 0:
            count += 1
    if count == 1:
        ans += 1

print(ans)