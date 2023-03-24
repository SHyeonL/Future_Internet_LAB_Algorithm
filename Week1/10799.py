# 10799번 - 쇠막대기
import sys

input = sys.stdin.readline

s = list(input().strip())
i = 0
cnt = 0
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        if i - stack[-1] == 1:
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)
