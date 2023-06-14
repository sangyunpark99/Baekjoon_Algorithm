from collections import deque

n = int(input())


def solution(s):
    stack = deque()

    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append('(')
        else:  # )인 경우
            if len(stack) > 0: # 이미 (가 들어있는 경우
                stack.pop()
            else: # (가 나오지도 않았는데 )가 들어간 경우
                print('NO')
                return

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


for i in range(n):
    solution(list(input()))
