import sys

for _ in range(100):
    ans = [0] * 4
    sentence = sys.stdin.readline().rstrip('\n')

    if not sentence:
        break

    for word in sentence:
        if word.isupper():
            ans[1] += 1
        elif word.islower():
            ans[0] += 1
        elif word.isspace():
            ans[3] += 1
        elif not word.isalpha():
            ans[2] += 1
    print(*ans)