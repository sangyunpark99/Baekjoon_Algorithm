import sys

t = int(input())
nums = [True] * 1000001

# 소수 구하기
for i in range(2, 1001):
    if nums[i]:
        for j in range(i + i, 1000001, i):  # 배수 제거
            nums[j] = False

for _ in range(t):
    ans = []
    num = int(sys.stdin.readline().rstrip())
    for i in range(2, int(num//2)+1): # 절반만 돌기 + 1
        if nums[i]: # 소수라면
            if nums[num - i] and num-i!=1: # 존재 한다면
                    ans.append((i, num - i))

    print(len(ans))