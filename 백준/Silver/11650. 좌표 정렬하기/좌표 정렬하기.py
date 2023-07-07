import sys
input = sys.stdin.readline

n = int(input().strip())
table = []

for _ in range(n):
  table.append(list(map(int, input().split())))

table.sort(key = lambda x: (x[0], x[1]))

for t in table:
    print(t[0], t[1])