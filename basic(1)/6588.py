import sys

primes = []
prime = [True] * 1000001
for i in range(2, int(1000000**0.5)+1):
    if prime[i]:
        for j in range(2*i, 1000001, i): # 배수인경우 False
            prime[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    flag = False
    for i in range(3, n//2+1, 2): # 홀수 이므로 2씩 더해준다.
        if prime[i] and prime[n-i]: # 소수인 경우
            print(f'{n} = {i} + {n-i}')
            flag = True
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")