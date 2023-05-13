# 17103번 - 골드바흐 파티션

import sys

input = sys.stdin.readline

prime = []
max = 1000001
check = [False for i in range(max)]
check[0] = True
check[1] = True
for i in range(2, max):
    if not check[i]:
        prime.append(i)
        for j in range(i + i, max, i):
            check[j] = True

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for j in prime:
        if j > n / 2:
            print(cnt)
            break
        if not check[n - j]:
            cnt += 1
