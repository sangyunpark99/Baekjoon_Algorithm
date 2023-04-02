import sys

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = 0

n,b = sys.stdin.readline().split()

num = len(n)-1
for word in n:
    ans += int(a.find(word)) * int(b) ** num
    num -= 1

print(ans)