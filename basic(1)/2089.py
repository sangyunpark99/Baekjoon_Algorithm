n = int(input())

res = ''

if not n:
    print('0')

while n:
    if n %(-2): # -2로 나누었을때 나머지가 존재하는 경우
        res = '1' + res
        n = n // -2 + 1
    else: # -2로 나누었을때 나머지가 존재하지 않는 경우
        res = '0' + res
        n //= -2 # -2로 나눠주어야 한다.

print(res)
