n = int(input())
table = [[] for _ in range(n)]

for i in range(n):
    a, b = input().split()
    table[i] = [int(a), b, i]

table.sort(key=lambda x: (x[0], x[2]))

for t in table:
  print(t[0], t[1])