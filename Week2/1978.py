# 1978번 - 소수 찾기

import sys
import math

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in num:
    tmp = 2
    flag = False
    if i == 1:
        continue
    if i == 2 or i == 3:
        cnt += 1
        continue
    while tmp <= int(math.sqrt(i)):
        if i % tmp == 0:
            flag = True
            break
        tmp += 1
    if flag is False:
        cnt += 1
print(cnt)
