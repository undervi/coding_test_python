import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_money = 999999999
single_money = 999999999

for _ in range(m):
    set, single = map(int, input().split())
    set_money = min(set_money, set*(n//6), single*(n-(n%6)))
    single_money = min(single_money, (n%6)*single, set)

print(set_money+single_money)