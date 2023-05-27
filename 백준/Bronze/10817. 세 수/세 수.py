import sys

array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[1])