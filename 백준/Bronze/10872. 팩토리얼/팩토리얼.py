import sys
n = int(sys.stdin.readline())
result = 1

while(n >= 2):
  result *= n
  n -= 1

print(result)