s = list(input())


# 1로 만드는 경우
def makeOne(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1

    cnt += 1

    return cnt // 2


print(makeOne(s))
