import sys
input = sys.stdin.readline

n = int(input())
arr = []
max_height = 0
max_x = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

    if y > max_height:
        max_x.clear()
    if y >= max_height: 
        max_height = y
        max_x.append(x)

arr.sort(key=lambda x: x[0])


# 왼쪽 -> y가 커지면! y*(y가 커진 후 x- 시작x) 더하기
left_area = 0
x, y = arr[0][0], arr[0][1]
for i in range(n):
    if arr[i][1] > y:
        left_area += (arr[i][0] - x) * y
        x, y = arr[i][0], arr[i][1]
    if arr[i][1] == max_height:
        break


# 오른쪽
right_area = 0
x, y = arr[n-1][0], arr[n-1][1]
for i in range(n-1, 0, -1):
    if arr[i][1] > y:
        right_area += (x-arr[i][0]) * y
        x, y = arr[i][0], arr[i][1]
    if arr[i][1] == max_height:
        break

# 중앙
cnt = 1
if len(max_x) > 1:
    cnt += max(max_x) - min(max_x)

print(left_area + right_area + max_height * cnt)