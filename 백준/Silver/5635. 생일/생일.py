import sys
input = sys.stdin.readline

n = int(input())
arr = [ input().split() for _ in range(n)]

arr.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(arr[-1][0], arr[0][0], sep="\n")