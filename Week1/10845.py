import sys

input = sys.stdin.readline

m = int(input())
queue = []
for i in range(m):
    cmd = list(input().split())
    if cmd[0] == 'push':
        queue.append(cmd[1])
    if cmd[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    if cmd[0] == 'size':
        print(len(queue))
    if cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    if cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
