# 2004번 - 조합 0의 개수

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

two = 0
five = 0
i = 5
while i <= n:
    five += n // i
    i *= 5
i = 5
while i <= n - m:
    five -= (n - m) // i
    i *= 5
i = 5
while i <= m:
    five -= m // i
    i *= 5
i = 2
while i <= n:
    two += n // i
    i *= 2
i = 2
while i <= (n - m):
    two -= (n - m) // i
    i *= 2
i = 2
while i <= m:
    two -= m // i
    i *= 2

print(min(two, five))
# 조합의 경우, 분자의 팩토리얼 0의 개수를 구한 후, 분모의 팩토리얼 0의 개수를 빼주면 됨
# 이 때는 5의 개수가 2의 개수보다 많은 경우가 존재할 수 있으므로 비교 필요
