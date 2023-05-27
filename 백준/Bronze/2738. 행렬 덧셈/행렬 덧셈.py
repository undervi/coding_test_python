import sys

n, m = map(int, sys.stdin.readline().split())

A = []
B = []
result = []

for _ in range(n):
    in_array = list(map(int, sys.stdin.readline().split()))
    A.append(in_array)

for _ in range(n):
    in_array = list(map(int, sys.stdin.readline().split()))
    B.append(in_array)
  
for i in range(n):
    array = []  
    for j in range(m):    
        array.append(str(A[i][j] + B[i][j]))
    result.append(array)

for r in result:
    print(' '.join(r))