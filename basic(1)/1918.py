s = list(input())
stack = []
ans = ''

for word in s:
    if word.isalpha(): # 알파벳인 경우
        ans += word
    else:
        if word == '(':
            stack.append(word)
        elif word == '*' or word == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(word)
        elif word == '+' or word == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(word)
        elif word == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop() # 여는 괄호 빼주기

while stack:
    ans += stack.pop()

print(ans)