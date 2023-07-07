import sys
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
    x, y = map(int, input().split())
    table.append([x, y])

table.sort(key=lambda x: (x[1], x[0]))

for t in table:
    print(t[0], t[1])