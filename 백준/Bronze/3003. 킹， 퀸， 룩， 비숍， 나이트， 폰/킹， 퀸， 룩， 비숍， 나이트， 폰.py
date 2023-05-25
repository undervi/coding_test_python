import sys

array = [1, 1, 2, 2, 2, 8]
input = list(map(int, sys.stdin.readline().split()))
result = ""

for i in range(6):
    result += (str(array[i] - input[i]) + " ")

print(result.rstrip())