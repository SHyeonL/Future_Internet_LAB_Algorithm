# 1929 - 소수 구하기

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
prime = []
check = [False for i in range(n + 1)]
for i in range(2, n + 1):
    if not check[i]:
        prime.append(i)
        for j in range(i + i, n + 1, i):
            check[j] = True

for i in prime:
    if i >= m:
        print(i)
