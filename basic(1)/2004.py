import sys

n, m = map(int, sys.stdin.readline().split())


def count_num(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


# 빼주는 이유? (n-m)!이랑 m!은 빼주어야 하기 때문에
two_count = count_num(n, 2) - count_num(m, 2) - count_num(n - m, 2)
five_count = count_num(n, 5) - count_num(m, 5) - count_num(n - m, 5)

print(min(two_count, five_count))  # 2와 5의 짝을 세줄려면 더 작은 갯수를 가진 것을 판단
