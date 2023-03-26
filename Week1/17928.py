# 17298번 - 오큰수
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, (input().split())))
stack = []
ans = [0 for i in range(n)]

stack.append(0)
for i in range(1, n):
    if not stack:
        s.append(i)
    while stack and s[stack[-1]] < s[i]:
        ans[stack[-1]] = s[i]
        stack.pop()
    stack.append(i)
while stack:
    ans[stack[-1]] = -1
    stack.pop()
print(*ans)
