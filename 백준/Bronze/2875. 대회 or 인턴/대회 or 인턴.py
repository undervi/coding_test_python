import math
n, m, k = map(int, input().split())
result = 0

if n // 2 >= m:
  result = m
  n -= 2*m
  m = 0
else:
  result = n // 2
  m -= n // 2
  n %= 2

if k <= n+m:
  print(result)
else:
  print(result - math.ceil((k - (n+m)) / 3))