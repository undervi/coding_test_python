import sys
input = sys.stdin.readline

k = int(input())
result = []

for _ in range(k):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop()

print(sum(result))