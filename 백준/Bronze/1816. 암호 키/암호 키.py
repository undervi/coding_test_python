import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    result = "YES"

    for i in range(2, 1_000_001):
        if num % i == 0:
            result = "NO"
            break

    print(result)
