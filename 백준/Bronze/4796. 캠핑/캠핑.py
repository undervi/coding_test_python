import sys
input = sys.stdin.readline
cnt = 1

while True:
    l, p, v = map(int, input().split())

    if l+p+v == 0:
        break

    print("Case "+str(cnt)+":", l * (v // p) + min(v % p, l))
    cnt += 1