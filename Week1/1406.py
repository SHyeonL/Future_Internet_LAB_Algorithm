import sys

input = sys.stdin.readline

left_stk = list(input().strip())
right_stk = []
m = int(input())

for i in range(m):
    a = list(input().split())
    if a[0] == 'L':
        if left_stk:
            right_stk.append(left_stk.pop())
    if a[0] == 'D':
        if right_stk:
            left_stk.append(right_stk.pop())
    if a[0] == 'B':
        if left_stk:
            left_stk.pop()
    if a[0] == 'P':
        left_stk.append(a[1])

left_stk.extend(reversed(right_stk))
print(''.join(left_stk))
