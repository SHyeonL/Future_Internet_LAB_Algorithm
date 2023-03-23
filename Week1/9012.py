import sys

input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    x = list(input().strip())
    for j in range(len(x)):
        if x[j] == '(':
            stack.append(x[j])
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
        if j == len(x) - 1:
            if stack:
                print('NO')
            else:
                print('YES')
            stack.clear()
