import sys
h, m = map(int, sys.stdin.readline().split())

min = h*60 + m - 45

if min < 0:
    min = (24 * 60) + min

new_h = min // 60
new_m = min % 60

print(new_h, new_m)