import sys
input = sys.stdin.readline

input()
ls = list(map(int, input().split()))
ls.sort()
print(*ls)