from collections import deque

stick_laser = list(input())

stk = deque()

answer = 0

for i in range(len(stick_laser)):
    if stick_laser[i] == '(':
        stk.append('(')
    else:
        if stick_laser[i-1] == '(':
            stk.pop()
            answer += len(stk)
        else:
            stk.pop()
            answer += 1

print(answer)