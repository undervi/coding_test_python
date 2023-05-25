import sys
a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
    print(10000 + (1000 * a))
elif a == b or a == c:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
else:
    print(max(a, b, c) * 100)