from collections import deque
import sys

N = int(input())

dq = deque()


def executeOrder(name, num=0):
    if name == 'push' and num > 0:
        dq.append(num)
    elif name == 'pop':
        if len(dq):
            print(dq.pop())
        else:
            print(-1)
    elif name == 'size':
        print(len(dq))
    elif name == 'empty':
        if len(dq):
            print(0)
        else:
            print(1)
    elif name == 'top':
        if dq:
            print(dq[-1])
        else:
            print(-1)


for _ in range(N):
    order = sys.stdin.readline().rstrip()

    if order.find(' ') > -1:  # 띄워쓰기가 있는 경우
        name, num = order.split()
        executeOrder(name, int(num))
    else:  # 띄워쓰기가 있지 않은 경우
        executeOrder(order)
