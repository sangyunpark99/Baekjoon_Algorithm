s = list(map(int, input()))

cnt = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cnt += 1

print((cnt+1)//2) # 뒤집은 횟수가 홀수개 인경우 고려