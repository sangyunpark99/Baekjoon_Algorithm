# 재귀로 풀기
def star(n):
    if n == 3: # 3인 경우
        return ['***', '* *', '***']

    stars = star(n//3)
    arr = []
    for s in stars: # 첫째줄
        arr.append(s * 3)
    for s in stars:
        arr.append(s + ' '*(n//3) + s)
    for s in stars:
        arr.append(s * 3)

    return arr # 최종 결과

n = int(input())
print(*star(n), sep='\n')