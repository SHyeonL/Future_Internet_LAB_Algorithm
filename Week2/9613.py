# 9613번 - GCD 합

import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())

for i in range(t):
    data = list(map(int, input().split()))
    gcd_sum = 0
    for j in range(data[0]):
        for k in range(j + 1, data[0]):
            gcd_sum += gcd(data[j + 1], data[k + 1])
    print(gcd_sum)
