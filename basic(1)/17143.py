s = list(input())

flag = False # 괄호가 열려있는지 여부

middle = ''
ans = ''

# 괄호가 열려있는 상태인지의 여부에따라 값이 달라진다.
for word in s:
    if not flag: # 괄호가 열려있지 않다면
        if word == '<': # 괄호를 만났다면
            middle += word # 괄호 추가
            flag = True # flag False로 초기화

        elif word == ' ': # 띄워쓰기를 만났다면
            middle += word
            ans += middle # 지금까지 기록해놓은 문자 정답에 추가
            middle = ''

        else: # 문자를 만났다면
            middle = word + middle # 순서를 바꿔서 저장

    elif flag:  # 괄호가 열려있다면
        if word == '>':  # 닫는 괄호를 만난다면
            middle += word
            flag = False
            ans += middle
            middle = ''
        else: # 닫는 괄호를 만나기 전까지
            middle += word # 순차적으로 더해주기

print(ans + middle)
