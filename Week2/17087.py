# 17087번 - 숨바꼭질 6

import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n, s = map(int, input().split())
pos = list(map(int, input().split()))
pos = [abs(x - s) for x in pos]
if n == 1:
    print(pos[0])
    exit()
d_max = gcd(pos[0], pos[1])
for j in range(2, len(pos)):
    d_max = gcd(d_max, pos[j])
print(d_max)
