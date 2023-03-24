# 10866번 - 덱
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deq = deque()
for i in range(n):
    a = list(input().split())
    if a[0] == "push_front":
        deq.appendleft(a[1])
    elif a[0] == "push_back":
        deq.append(a[1])
    elif a[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif a[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(deq))
    elif a[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif a[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
