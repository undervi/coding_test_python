import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
result = 0

for _ in range(n):
    words.append(input().strip())

for _ in range(m):
    check = input().strip()
    if check in words:
        result += 1

print(result)