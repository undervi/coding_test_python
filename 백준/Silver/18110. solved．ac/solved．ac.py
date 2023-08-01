def _round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

if n > 0:
    remove_num = _round(n*0.15)
    start, end = remove_num, n-remove_num
    avg = _round(sum(arr[start:end]) / (n-2*remove_num))
else:
    avg = 0
print(avg)
