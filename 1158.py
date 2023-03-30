from collections import deque

n, k = map(int, input().split())
dq = deque()

point = 0

list = [i for i in range(1, n+1)]

while list:

    point += k-1

    if point >= len(list):
        point %= len(list)

    dq.append(list.pop(point))

ans_list = []

while dq:
    ans_list.append(dq.popleft())

ans = '<'

for i in range(len(ans_list)):
    if i == len(ans_list)-1:
        ans += f'{ans_list[i]}'
    else:
        ans += f'{ans_list[i]}, '

ans += '>'

print(ans)

