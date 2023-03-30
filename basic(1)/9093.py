import sys

T = int(input())

for _ in range(T):
    ans = ''
    sentence = list(sys.stdin.readline().rstrip().split())
    for word in sentence:
        print(*reversed(word))
        ans += "".join(reversed(word)) + ' '
    print(ans)
