# 1676번 - 팩토리얼 0의 개수

import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
i = 5
while i <= n:
    cnt += n // i
    i *= 5
print(cnt)

# 팩토리얼을 실제로 계산하여 0의 개수를 구하기에는 숫자가 너무 크다
# 소인수분해의 특징을 이용하여 2x5의 개수를 구하자. (결론적으로는 5의 개수만 구하면 됨)
