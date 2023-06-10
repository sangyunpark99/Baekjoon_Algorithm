from collections import deque


def VPS(arr):
    stack = deque()
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        else:
            if len(stack) > 0: # 이미 (가 있는 경우
                stack.pop() # 빼버려!
            else: # (가 존재하지 않는 경우
                print('NO') # 뭘해도 안됨~
                return
    if len(stack) == 0: # 짝이 전부 존재하는 경우
        print('YES')
    else: # 짝이 존재하지 않는 경우
        print('NO')


n = int(input())
for _ in range(n):
    VPS(list(input()))
