import sys
input = sys.stdin.readline

from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

arr.sort()
for x in list(combinations(arr, 7)):
    if sum(x) == 100:
        print("\n".join(map(str, x)))
        break