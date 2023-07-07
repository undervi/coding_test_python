import sys
input = sys.stdin.readline

def Euclidean(a, b):
    r = b % a
    if r == 0:
        return a
    return Euclidean(r, a)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())  
    r = Euclidean(max(x, y), min(x, y))
    print(r * (x//r) * (y//r))