import sys
input = sys.stdin.readline

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ls = a+b
ls.sort()
print(*ls)