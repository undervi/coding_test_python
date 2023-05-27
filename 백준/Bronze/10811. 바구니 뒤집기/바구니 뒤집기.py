import sys

n, m = map(int, sys.stdin.readline().split())

result = []
for i in range(1, n+1):
    result.append(str(i))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    
    change = []
    for l in range(i-1, j):
        change.append(result[l])
    change.reverse()

    k = 0
    for l in range(i-1, j):
        result[l] = change[k]
        k += 1

print(' '.join(result))