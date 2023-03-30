n = int(input())


def recursive(n):
    if n < 2:
        return 1
    return n * recursive(n-1)


print(recursive(n))