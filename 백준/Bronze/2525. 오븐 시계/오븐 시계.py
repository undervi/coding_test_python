h, m = map(int, input().split())
plus = int(input())

min = h * 60 + m + plus

if min >= 1440:
    min -= 1440

new_h = min // 60
new_m = min % 60

print(new_h, new_m)