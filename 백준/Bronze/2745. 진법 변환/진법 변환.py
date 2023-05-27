import sys

n, b = sys.stdin.readline().rstrip().split()
b = int(b)
result = 0
digit = 0

for x in range(len(n)-1, -1, -1):
  if n[x].isdigit():
      num = int(n[x])
  else:
      num = ord(n[x]) - 55

  result += ((b**digit) * num)
  digit += 1

print(result)