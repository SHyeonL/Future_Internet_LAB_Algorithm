import sys

input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    x = input()
    for j in range(len(x)):
        if x[j] == ' ' or j == len(x) - 1:
            while stack:
                print(stack.pop(), end='')
            if j == len(x) - 1:
                print('\n', end='')
            else:
                print(' ', end='')
        else:
            stack.append(x[j])
