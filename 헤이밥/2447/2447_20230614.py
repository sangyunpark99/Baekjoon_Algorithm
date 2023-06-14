n = int(input())


def solution(n):
    if n == 3:
        return ['***', '* *', '***']

    stars = solution(n // 3)
    arr = []

    for star in stars:
        arr.append(star * 3)
    for star in stars:
        arr.append(star + ' ' * (n // 3) + star)
    for star in stars:
        arr.append(star * 3)

    return arr


print(*solution(n), sep="\n")
