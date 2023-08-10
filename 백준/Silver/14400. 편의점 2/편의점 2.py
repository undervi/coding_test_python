import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

mid_x = sorted(points, key=lambda x: x[0])[n//2][0]
mid_y = sorted(points, key=lambda x: x[1])[n//2][1]

dis = 0
for x, y in points:
    dis += (abs(mid_x-x) + abs(mid_y-y))
    
print(dis)