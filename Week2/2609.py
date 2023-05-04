import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return g * (a / g) * (b / g)


a, b = map(int, input().split())
print(gcd(a, b))
print(int(lcm(a, b)))
