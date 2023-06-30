n = int(input())
list = []

for _ in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = x1+10, y1+10

    for x in range(x1, x2):
        for y in range(y1, y2):
            if [x, x+1, y, y+1] not in list:
                list.append([x, x+1, y, y+1])

print(len(list))