from collections import deque

s = list(input())

stack = deque()
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:  # )인 경우
        if stack[-1] == '(' and s[i - 1] != ')':  # ()
            stack.pop()
            cnt += len(stack)
        else:  # ))
            cnt += 1
            stack.pop()

print(cnt)
