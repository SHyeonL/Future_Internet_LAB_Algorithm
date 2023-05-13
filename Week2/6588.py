# 6588번 - 골드바흐의 추측

import sys

input = sys.stdin.readline

prime = []
max = 1000001
check = [False for i in range(max)]
for i in range(2, max):
    if not check[i]:
        prime.append(i)
        for j in range(i + i, max, i):
            check[j] = True

while True:
    n = int(input())
    if n == 0 or n < 6:
        exit()
    for i in range(1, n):
        if prime[i] > n:
            print("Goldbach's conjecture is wrong.")
            break
        if not check[n - prime[i]]:
            print(n, "=", prime[i], "+", n - prime[i], sep=" ")
            break
