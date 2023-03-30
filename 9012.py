from collections import deque
import sys

T = int(input())

for _ in range(T):
    flag = False
    data = sys.stdin.readline().rstrip()

    if data[0] == ')':
        print('NO')
        continue

    dq = deque(data[0])
    for i in range(1, len(data)):
        if data[i] == '(': # ( 를 받은 경우
            dq.append('(')
        else:
            if not len(dq): # ( 가 존재하지 않는데, )값을 받은 경우
                print('NO')
                flag = True
                break;
            else: # ( 가 존재하는데 ) 값을 받은 경우
                dq.pop()
    if len(dq): # dq의 길이가 0보다 크다면 VPS 조건 탈락
        print('NO')
    else: # dq의 길이가 0이라면 VPS
        if not flag:
            print('YES')
