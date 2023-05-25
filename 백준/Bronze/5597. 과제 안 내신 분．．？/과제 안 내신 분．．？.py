import sys

array = []
for _ in range(28):
    num = sys.stdin.readline().rstrip()
    array.append(num)

for i in range(1, 31):
    if str(i) not in array:
      print(i)