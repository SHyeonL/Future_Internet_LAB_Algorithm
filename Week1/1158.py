# 1158 - 요세푸스 문제
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

people = deque()
for i in range(1, n + 1):
    people.append(i)
cnt = 1
ans = []
while True:
    if not people:
        break
    if cnt == k:
        ans.append(people.popleft())
        cnt = 1
    else:
        people.append(people.popleft())
        cnt += 1

print(str(ans).replace('[', '<').replace(']', '>'))
# replace를 활용하여 출력문을 조절하자~~!!
