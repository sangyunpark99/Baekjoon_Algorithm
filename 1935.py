import sys

n = int(input())

data = list(input())
stack = []
nums = []  # 각 알파벳에 주어진 숫자
result = 0

for i in range(n):
    nums.append(int(sys.stdin.readline()))

for i in range(len(data)):
    if 'A' <= data[i] <= 'Z':
        stack.append(nums[ord(data[i]) - ord('A')])
    else:
        num1 = float(stack.pop())
        num2 = float(stack.pop())

        if data[i] == '+':
            result = num2 + num1
        if data[i] == '-':
            result = num2 - num1
        if data[i] == '*':
            result = num2 * num1
        if data[i] == '/':
            result = num2 / num1
        stack.append(result)

print(format(result, ".2f"))
