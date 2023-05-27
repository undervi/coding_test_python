import sys

n, m = map(int, sys.stdin.readline().split())
result = ['0'] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for l in range(i-1, j):
        result[l] = str(k)

print(' '.join(result))