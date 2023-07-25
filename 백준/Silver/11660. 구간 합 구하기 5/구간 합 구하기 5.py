import sys
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for y in range(n):
    for x in range(n):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    answer = prefix[y2][x2] - prefix[y1-1][x2] - prefix[y2][x1-1] + prefix[y1-1][x1-1]
    print(answer)