words = list(input())
ans = [-1]*26

for i in range(len(words)):
    if ans[ord(words[i]) - ord('a')] == -1:
        ans[ord(words[i]) - ord('a')] = i

print(*ans)