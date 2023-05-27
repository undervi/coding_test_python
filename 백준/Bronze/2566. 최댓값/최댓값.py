import sys

max_num = 0
max_row, max_col = 0, 0
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

for row in range(9):
    for col in range(9):
        if table[row][col] >= max_num:
            max_num = table[row][col]
            max_row, max_col = row + 1, col + 1

print(max_num)
print(max_row, max_col)