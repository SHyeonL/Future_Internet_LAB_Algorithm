import sys

input = sys.stdin.readline

m = 0
n = int(input())
ans = ''
stack = []
for i in range(n):
    x = int(input())
    if x > m:
        while x > m:
            m += 1
            stack.append(m)
            ans += '+'
        stack.pop()
        ans += '-'
    else:
        found = False
        if stack:
            top = stack.pop()
            ans += '-'
            if x == top:
                found = True
        if not found:
            print("NO")
            exit()
for i in ans:
    print(i)
