import sys
list1 = list(sys.stdin.readline().rstrip())
list2 = []

for _ in range(int(sys.stdin.readline().rstrip())):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == 'P':
        list1.append(command[1])

    if command[0] == 'L':
        if list1:
            list2.append(list1.pop())

    if command[0] == 'D':
        if list2:
            list1.append(list2.pop())

    if command[0] == 'B':
        if list1:
            list1.pop()

list1.extend(reversed(list2))
print(''.join(list1))

