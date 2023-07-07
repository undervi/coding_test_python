import sys
input = sys.stdin.readline

input()
ls = list(map(int, input().split()))
print(max(ls)*min(ls)) 