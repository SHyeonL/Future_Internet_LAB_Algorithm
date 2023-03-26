# 17299번 - 오등큰수
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, (input().split())))
freq = [0 for _ in range(max(s) + 1)]
ans = [0 for _ in range(n)]
stack = []
for i in range(n):
    freq[s[i]] += 1
stack.append(0)
for i in range(1, n):
    if not stack:
        stack.append(i)
    while stack and freq[s[stack[-1]]] < freq[s[i]]:
        ans[stack[-1]] = s[i]
        stack.pop()
    stack.append(i)
while stack:
    ans[stack[-1]] = -1
    stack.pop()
print(*ans)
