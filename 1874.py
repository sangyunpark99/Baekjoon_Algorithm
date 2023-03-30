from collections import deque
import sys

dq = deque()

n = int(input())

start = 1

ans = list()

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while start <= num:
        dq.append(start)
        ans.append('+')
        start += 1

    if dq.pop() == num:
        ans.append('-')
    else:
        print('NO')
        exit()

for i in ans:
    print(i)
