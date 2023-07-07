import sys
input = sys.stdin.readline

n = int(input())
ls = [0] * 10001

for _ in range(n):
    num = int(input())
    ls[num] += 1

for i in range(1, 10001):
    if ls[i] != 0:
        for _ in range(ls[i]):
            print(i)