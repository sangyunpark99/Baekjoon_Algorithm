import sys

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())
ans = ''

while n != 0:
    ans += str(a[n % b])
    n //= b # 몫의 값 추가

print(ans[::-1])