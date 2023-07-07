import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sites = dict()

for _ in range(n):
    a, b = input().split()
    sites[a] = b
  
for _ in range(m):
    print(sites[input().rstrip()])