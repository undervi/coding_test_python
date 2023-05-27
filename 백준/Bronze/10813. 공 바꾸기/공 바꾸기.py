import sys

n, m = map(int, sys.stdin.readline().split())

result = []
for i in range(1, n+1):
    result.append(str(i))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i_value, j_value = result[i-1], result[j-1]
    result[i-1], result[j-1] = j_value, i_value
    
print(' '.join(result))